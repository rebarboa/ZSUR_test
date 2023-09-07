import numpy as np
import matplotlib.pyplot as plt


## vektorova kvantizace ##
from plotPlt import plot_o, plot_dot


def vq(classR, coordinates, mi):
    class_temp = [list() for i in range(len(classR))]
    dist = list()
    min_dist = list()
    min_mi = list()

    for i in range(len(coordinates)):  # minimum
        distL = list()
        for j in range(len(mi)):
            distL.append(np.linalg.norm(coordinates[i] - mi[j]))
        dist.append(distL)
        min_dist.append(min(dist[i]))  # minimalni distance
        min_mi.append(dist[i].index(min_dist[i]))  # index minimalni distance mi

    for i in range(len(min_mi)):
        class_temp[min_mi[i]].append(coordinates[i])

    plot_dot(classR, class_temp)
    plot_o(classR)
    plt.title('Vektorova kvantizace')
    plt.show()
