import numpy as np


## vytvoreni rastru ##

def raster():  # vytvoreni rastru
    rangexy = [[-15.0, -15.0], [18.0, 14.0]]
    c = list()

    ax_x = rangexy[0][0]
    ax_y = rangexy[0][1]

    while ax_x < rangexy[1][0]:
        ax_y = rangexy[0][1]
        while ax_y < rangexy[1][1]:
            c.append([ax_x, ax_y])
            ax_y += 0.1
        ax_x += 0.1
    return c
