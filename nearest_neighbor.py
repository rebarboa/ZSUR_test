import numpy as np
import matplotlib.pyplot as plt
from plotPlt import plot_o, plot_dot


## klasifikator podle nejblizsiho souseda ##

def nearest_neighbor(classR, coordinates):
    class_temp = [list() for i in range(len(classR))]

    for i in range(len(coordinates)):
        dist_min = np.linalg.norm(classR[0][0] - coordinates[i])
        classF = 0
        for j in range(len(classR)):
            for k in range(len(classR[j])):
                dist_s = np.linalg.norm(classR[j][k] - coordinates[i])
                if dist_min > dist_s:
                    dist_min = dist_s
                    classF = j
        class_temp[classF].append(coordinates[i])

    plot_dot(classR, class_temp)
    plot_o(classR)

    plt.title('Klasifikator podle nejblizsiho souseda')
    plt.show()


## klasifikator podle dvou nejblizsich sousedu ##

def two_nearest_neighbors(classR, coordinates):
    class_temp = [list() for i in range(len(classR))]
    for i in range(len(coordinates)):
        classF = 0
        const = 1000000000000
        for j in range(len(classR)):
            dist_min_first = np.linalg.norm(classR[0][0] - coordinates[i])
            dist_min_second = np.linalg.norm(classR[0][0] - coordinates[i])
            for k in range(len(classR[j])):
                dist_min_third = np.linalg.norm(classR[j][k] - coordinates[i])
                if dist_min_second > dist_min_third:
                    dist_min_second = dist_min_first
                    dist_min_first = dist_min_third
                else:
                    dist_min_second = dist_min_third
            dist_min_third = dist_min_first + dist_min_second
            if dist_min_third < const:
                classF = j
                const = dist_min_third
        class_temp[classF].append(coordinates[i])

    plot_dot(classR, class_temp)
    plot_o(classR)
    plt.title('Klasifikator podle dvou nejblizsich sousedu')
    plt.show()
