from matplotlib import pyplot as plt

from create_raster import raster
from data import load_data, plot_data
from first_task import cluster_analysis, chain_map, maxmin
from lin_dis_fc import rosenblatt, const, const_2
from nearest_neighbor import nearest_neighbor, two_nearest_neighbors
from plotPlt import plot_o
from second_task import kmeans, bin
from third_task import ite_opt
from Bayes import bayes
from vq import vq


def main():
    x = load_data()
    plot_data(x)

    #### 1. ukol ####
    cluster_analysis(x)
    chain_map(x)
    maxmin(x)

    #### 2. ukol ####
    R = 3 #zjisteny pocet trid
    list_classK, mi = kmeans(x, R)  # metoda k-means
    list_class, mi = bin(x, R)  # nerovnomerne binarni deleni

    #### 3. ukol ####
    list_class_ite, mi_ite = ite_opt(list_class, mi)  # iterativni optimalizace
    plot_o(list_class_ite)
    plt.title('Iterativni optimalizace')
    plt.show()

    #### 4. ukol ####
    coordinates = raster()
    ## a) ##
    bayes(x, list_class, coordinates, mi)  # bayesovsky klasifikator
    ## b) ##
    vq(list_class, coordinates, mi)
    ## c) ##
    nearest_neighbor(list_class, coordinates)  # klasifikator podle nejblizsiho souseda
    two_nearest_neighbors(list_class, coordinates)  # klasifikator podle dvou nejblizsich sousedu
    ## d) ##
    rosenblatt(x, coordinates, list_class)  # Rosebnblattuv algoritmus
    const(x, list_class, coordinates)  # Metoda konstantnich prirustku
    const_2(x, list_class, coordinates)  # Upravena metoda konstatnich prirustku


if __name__ == "__main__":
    main()
