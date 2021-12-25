import numpy as np
from numpy import linalg as LA


def is_pos_def(x):
    """
        Проверка, является ли матрица симметричной и положительно определенной
    """
    return np.all(np.linalg.eigvals(x) > 0)


def conjugateGradientDescent(A, b):
    """
        Метод сопряженных градиентов
    """

    # символ @ идентичен dot() - это произведение массивов
    if (is_pos_def(A) == False) | (A != A.T).any():
        raise ValueError('Матрица A должна быть симметричной и положительно определенной')
    r = b
    k = 0
    x = np.zeros(A.shape[-1])
    x_steps = [x]
    y_steps = [0.5 * x @ A @ x - x @ b]
    counter = 0
    while LA.norm(r) > 1e-10 :
        if k == 0:
            p = r
        else:
            gamma = - (p @ A @ r)/(p @ A @ p)
            p = r + gamma * p
        alpha = (p @ r) / (p @ A @ p)
        x = x + alpha * p
        r = r - alpha * (A @ p)
        k =+ 1
        x_steps.append(x)
        y_steps.append(0.5 * x @ A @ x - x @ b)
        counter += 1

    print("Количество шагов: " + str(counter))

    return x, x_steps, y_steps


