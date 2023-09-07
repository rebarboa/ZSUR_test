import matplotlib.pyplot as plt


def plot_o(classR):
    for i in range(len(classR)):
        ax = list()
        ay = list()
        for j in range(len(classR[i])):
            ax.append(classR[i][j][0])
            ay.append(classR[i][j][1])
        plt.plot(ax, ay, 'o')


def plot_dot(classR, class_temp):
    for i in range(len(classR)):
        ax = list()
        ay = list()
        for j in range(len(class_temp[i])):
            ax.append(class_temp[i][j][0])
            ay.append(class_temp[i][j][1])
        plt.plot(ax, ay, '.')
