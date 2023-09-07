import numpy as np


### 3. ukol ###
## iterativni oprimalizace ##

def ite_opt(list_class, mi):
    J = list()
    mi_n = list()
    J2 = list()

    for i in range(len(list_class)):
        count = 0
        for j in range(len(list_class[i])):
            count += np.linalg.norm(list_class[i][j] - mi[i])
            count = count / len(list_class[i])
            J.append(count)
    s = np.zeros((len(list_class)))
    for i in range(len(list_class)):
        count = 0
        for j in range(len(list_class[i])):
            count = 1 + count
        s[i] = count

    while True:
        for i in range(len(list_class)):
            for j in range(len(list_class[i])):
                if len(list_class[i]) > j:
                    A = list()
                    Ai = s[i] / (s[i] - 1) * np.linalg.norm(list_class[i][j] - mi[i])
                    for k in range(len(list_class)):
                        Aj = s[k] / (s[k] - 1) * np.linalg.norm(list_class[i][j] - mi[k])
                        A.append(Aj)
                    A.pop(A.index(A[i]))
                    At = min(A)
                    if Ai > At:
                        x_N = list_class[i].pop(j)
                        list_class[A.index(At)].append(x_N)

        for i in range(len(list_class)):
            count = 0
            for j in range(len(list_class[i])):
                sum_count = len(list_class[i])
                count += 1 / sum_count * list_class[i][j]
            mi_n.append(count)
        for i in range(len(list_class)):
            count = 0
            for j in range(len(list_class[i])):
                count += np.linalg.norm(list_class[i][j] - mi[i])
                count = count / len(list_class[i])
            J2.append(count)

        if J2 == J:
            return list_class, mi
        else:
            J = J2
