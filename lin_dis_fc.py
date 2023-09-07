import numpy as np
import matplotlib.pyplot as plt

from plotPlt import plot_dot, plot_o


def edit(classR, x):
    w = [list() for i in range(len(classR))]
    q = list()
    for i in range(len(classR)):
        for j in range(len(x)):
            if (x[j] == classR[i]).all(axis=1).any():
                w[i].append(1.0)
            else:
                w[i].append(-1.0)
    for i in range(len(classR)):  # urceni pocatecniho q
        q.append(np.array([1, 2, 3], dtype='float64'))
        # q.append(np.array([1, 1, 1], dtype='float64'))

    return w, q


def edit2(classR, q, coordinates):
    class_temp = [list() for i in range(len(classR) + 1)]
    for i in range(len(coordinates)):
        g = list()
        s = list()
        for j in range(len(classR)):
            g.append(0)
            for k in range(len(classR)):
                g[j] = g[j] + np.dot([1, coordinates[i][0], coordinates[i][1]], q[j])
        for j in range(len(g)):
            s.append(g[j] > 0)
        if s.count(True) == 1:
            classF = s.index(True)
        else:
            classF = len(classR)
        class_temp[classF].append(coordinates[i])
    return class_temp


## rosenblatt ##
def rosenblatt(x, coordinates, classR):
    w, q = edit(classR, x)
    d = 0

    temp_c = []
    ft = True
    for i in range(len(classR)):
        temp = 0
        while ft:
            temp += 1
            ft = False
            for j in range(len(x)):
                q_temp = np.matmul(np.array([1, x[j][0], x[j][1]], dtype='float64'), q[i]) * w[i][j]

                if q_temp < d:
                    q[i] += np.array([1, x[j][0], x[j][1]], dtype='float64') * w[i][j]
                    ft = True
        ft = True
        temp_c.append(temp)

    class_temp = edit2(classR, q, coordinates)

    plot_dot(classR, class_temp)
    plot_o(classR)
    plt.title('Rosenblattuv algoritmus')
    plt.show()
    # print(temp_c)


## metoda konstantnich prirustku ##
def const(x, classR, coordinates):
    b = 1
    d = 1
    w, q = edit(classR, x)
    temp_c = []
    ft = True
    for i in range(len(classR)):
        temp = 0
        while ft:
            temp += 1
            ft = False
            for j in range(len(x)):
                q_temp = np.matmul(np.array([1, x[j][0], x[j][1]], dtype='float64'), q[i]) * w[i][j]
                c_temp = b / np.linalg.norm(x[j][0] + x[j][1])
                if q_temp < d:
                    q[i] += np.array([1, x[j][0], x[j][1]], dtype='float64') * c_temp * w[i][j]
                    ft = True
        ft = True
        temp_c.append(temp)
    print(temp_c, 'beta = ', b, 'delta = ', d)
    class_temp = edit2(classR, q, coordinates)

    plot_dot(classR, class_temp)
    plot_o(classR)
    plt.title('Metoda konstantnich prirustku')
    plt.show()


# upravena metoda konstantnich prirustku
def const_2(x, classR, coordinates):
    b = 1
    d = 1
    w, q = edit(classR, x)
    temp_c = []
    ft = True
    for i in range(len(classR)):
        temp = 0
        while ft:
            temp += 1
            ft = False
            for j in range(len(x)):
                q_temp = np.matmul(np.array([1, x[j][0], x[j][1]], dtype='float64'), q[i]) * w[i][j]
                c_temp = b / np.linalg.norm(x[j][0] + x[j][1])
                while q_temp < d:
                    q[i] += np.array([1, x[j][0], x[j][1]], dtype='float64') * c_temp * w[i][j]
                    q_temp = np.matmul(np.array([1, x[j][0], x[j][1]], dtype='float64'), q[i]) * w[i][j]
                    ft = True
        ft = True
        temp_c.append(temp)
    # print(temp_c)

    class_temp = edit2(classR, q, coordinates)

    plot_dot(classR, class_temp)
    plot_o(classR)
    plt.title('Upravena metoda konstantnich prirustku')
    plt.show()
