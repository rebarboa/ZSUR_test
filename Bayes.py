import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as mvnorm
from plotPlt import plot_o, plot_dot

## bayesuv klasifikator ##


def bayes(x, classR, coordinates, mi):
    probability = list()
    class_div = [list() for i in range(len(classR))]

    cov_matrix = [np.array([[0, 0], [0, 0]], dtype='float64') for i in range(len(classR))]
    for i in range(len(classR)):
        for j in range(len(classR[i])):
            dist_x = classR[i][j][0] - mi[i][0]
            dist_y = classR[i][j][1] - mi[i][1]
            cov_temp = np.array([[dist_x * dist_x, dist_x * dist_y], [dist_x * dist_y, dist_y * dist_y]])
            cov_matrix[i] += cov_temp
        cov_matrix[i] = cov_matrix[i] / len(classR[i])

    for i in range(len(classR)):
        prob_temp = len(classR[i]) / len(x)
        probability.append(prob_temp)
    # print(probability)

    for i in range(len(coordinates)):
        class_prob = list()
        mult_prob = list()
        for j in range(len(classR)):
            class_prob.append(mvnorm.pdf(coordinates[i], mean=mi[j], cov=cov_matrix[j]))
            mult_prob.append(class_prob[j] * probability[j])
        prob_max = max(mult_prob)
        prob_idx = mult_prob.index(prob_max)
        class_div[prob_idx].append(coordinates[i])
    plot_dot(classR, class_div)
    plot_o(classR)

    plt.title('Bayesův klasifikátor')
    plt.show()
