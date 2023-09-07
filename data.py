## nacteni dat ##

import numpy as np
import matplotlib.pyplot as plt


# nacteni data
def load_data():
    x = list()
    with open('data.txt', 'r', encoding='UTF-8') as f:
        rline = f.readline()
        wline = []
        while rline:
            rline = str.split(rline)
            wline.append([float(rline[0]), float(rline[1])])
            rline = f.readline()

    for i in range(len(wline)):
        x.append(np.array([wline[i][0], wline[i][1]]))
    return x


## vykresleni dat
def plot_data(x):
    first = list()
    second = list()
    for i in range(len(x)):
        first.append(np.array(x[i][0]))
        second.append(np.array(x[i][1]))
    plt.figure()
    plt.plot(first, second, 'bo')
    plt.title('vykresleni dat')
    plt.show()
