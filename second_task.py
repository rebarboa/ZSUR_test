import numpy as np
import matplotlib.pyplot as plt
from plotPlt import plot_o


#### ukol 2 #####
## k-menas ##

def kmeans(x, R):
    mi = list()
    steps = 0
    for i in range(R):  # zvoleni R pocatecnich stredu mi nahodne
        indx = np.random.randint(0, len(x) - 1)
        mi.append(x[indx])

    while True:
        dist = list()
        min_dist = list()
        min_mi = list()
        list_class = [[] for i in range(R)]
        mi_n = list()

        for i in range(len(x)):  # minimum
            distL = list()
            for j in range(len(mi)):
                distL.append(np.linalg.norm(x[i] - mi[j]))
            dist.append(distL)
            min_dist.append(min(dist[i]))  # minimalni distance
            min_mi.append(dist[i].index(min_dist[i]))  # index minimalni distance mi

        for i in range(len(min_mi)):
            list_class[min_mi[i]].append(x[i])

        for i in range(len(list_class)):  # vypocet novych stredu pro kazdy shluk
            count = 0
            for j in range(len(list_class[i])):
                sum_count = len(list_class[i])
                count += 1 / sum_count * list_class[i][j]
            mi_n.append(count)

        comparison = np.array_equal(mi, mi_n)
        # print('res:', comparison)
        if comparison == True:
            # print(mi_n)
            # print('steps', steps)
            break

        else:
            mi = mi_n
            steps = steps + 1
    plot_o(list_class)

    for i in range(R):
        plt.plot(mi[i][0], mi[i][1], 'ro')  # vykresleni stredu
    plt.title('k-means')
    plt.show()

    return mi_n, list_class


## binarni deleni do ciloveho poctu trid ##
def bin(x, R):
    b = 2
    J = list()
    mi, list_class = kmeans(x, b)

    while True:
        for i in range(len(list_class)):
            count = 0
            for j in range(len(list_class[i])):
                count += np.linalg.norm(list_class[i][j] - mi[i])
            count = count / len(list_class[i])
            J.append(count)
        indx = J.index(max(J))
        mi_2, list_class2 = kmeans(list_class[indx], b)
        list_class.pop(indx)
        mi.pop(indx)

        for i in range(len(list_class2)):
            list_class.append(list_class2[i])
            mi.append(mi_2[i])

        if len(list_class) == R:
            break
    plot_o(list_class)

    for i in range(R):
        plt.plot(mi[i][0], mi[i][1], 'ro')  # vykresleni stredu
    plt.title('Nerovnomerne binarni deleni')
    plt.show()

    return list_class, mi
