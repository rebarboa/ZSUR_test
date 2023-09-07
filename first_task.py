import numpy as np
import matplotlib.pyplot as plt
import random


#### ukol 1 #####
## metoda shlukove hladiny ##
def cluster_analysis(x):
    count = 0
    T = np.zeros((len(x) - 1, len(x) - 1), dtype=float)
    for i in range(len(x) - 1):
        for j in range(len(x) - 1):
            T[i][j] = np.linalg.norm(x[i] - x[j])  # rozdeleni dat
    h = np.zeros(len(x) - 2, dtype=float)

    while True:
        minT = np.min(T[np.nonzero(T)])  # nutno vyradit nuly na uhlopricce
        indx = np.where(T == minT)
        dimension = np.shape(T)
        h[count] = minT

        for i in range(dimension[0]):
            T[indx[0][0]][i] = min(T[indx[0][0]][i], T[indx[1][0]][i])
            T[i][indx[0][0]] = min(T[i][indx[0][0]], T[i][indx[1][0]])
        T = np.delete(T, indx[1][0], 0)  # smazani radku a sloupcu
        T = np.delete(T, indx[1][0], 1)  # smazani radku a sloupcu
        dimension = np.shape(T)
        count += 1

        if dimension[0] == 0 or dimension[0] == 1:
            break
    plt.plot(h, 'bo')
    # plt.title('cluster analysis ')
    plt.show()


## metoda retezove mapy ##
def chain_map(x):
    new_x = list()
    shuff = np.random.permutation(x)  # nutne data zamichat
    new_x.append(shuff[0])
    first_x = new_x[0]  # vybrání startovacího obrazu
    print('Chain map first = ', first_x)
    shuff = np.delete(shuff, 0, 0)  # odstraneni startovaciho obrazu

    for i in range(1, len(shuff) + 1):
        temp = 500
        for j in range(len(shuff)):  # pomoci euklidovske normy vypocet nejblizsiho souseda
            dist = np.linalg.norm(new_x[i - 1] - shuff[j])
            # print(dist)
            if dist < temp:
                indx = j
                temp = dist
        new_x.append(shuff[indx])
        shuff = np.delete(shuff, indx, 0)

    x1 = list()
    x2 = list()
    for i in range(len(x)):
        x1.append(np.array([new_x[i][0]]))
        x2.append(np.array([new_x[i][1]]))
    plt.plot(x1, x2, 'bo-')
    plt.title('chain map')
    plt.show()


## MAXIMIN ##
def maxmin(x):
    nList = list()
    dist = list()
    min_dist = list()
    x1_list = list()
    x2_list = list()
    q = 1  # zvolim konstanty 0.5, 1, 0.09, 1.5

    indx = random.randint(0, len(x) - 1)  # vybrani nahodneho indexu
    print('Pocatecni bod pro MAXMIN', x[indx])  # pocatecni bod
    x1 = x[indx]
    nList.append(x1)  # zaradim x1 do noveho listu
    x.pop(indx)  # vyradim x1 z puvodniho listu

    temp = 0.001
    for i in range(len(x)):  # nalezeni nejvzdalenejsiho
        distF = np.linalg.norm(nList[0] - x[i])
        # print(dist)
        if distF > temp:
            temp_indx = i
            temp = distF

    x2 = x[temp_indx]
    nList.append(x2)  # zaradim x2 do noveho listu
    x.pop(temp_indx)  # vyradim x2 z puvodniho

    while True:  # maximum z minim
        for i in range(len(x)):
            distL = list()
            for j in range(len(nList)):
                distL.append(np.linalg.norm(x[i] - nList[j]))
            dist.append(distL)
            min_dist.append(min(dist[i]))  # minimalni distance

        max_dist = max(min_dist)  # max z min
        indx_max = min_dist.index(max_dist)

        count = 0
        for k in range(len(nList)):
            for l in range(k + 1, len(nList)):
                count += np.linalg.norm(nList[k] - nList[l])

        mean = (count / (len(nList)))  # soucet vydeleny poctem -> prumer
        trh = q * mean

        if max_dist > trh:  # porovnani
            nList.append(x[indx_max])
            x.pop(indx_max)

        else:
            break
    for i in range(len(x)):
        x1_list.append(np.array([x[i][0]]))
        x2_list.append(np.array([x[i][1]]))

    print('q = ', q, ', stredy = ', nList, ', pocet = ', len(nList))  # hodnota q,  stredy, pocet stredu
    plt.figure()
    plt.plot(x1_list, x2_list, 'bo')
    for i in range(len(nList)):
        plt.plot(nList[i][0], nList[i][1], 'ro')  # vykresleni stredu
    plt.title('MAXMIN')
    plt.show()
