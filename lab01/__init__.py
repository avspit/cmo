import sys
import numpy as np
from util import func1

def init_xy(N):
    x_arr = np.zeros(N)
    y_arr = np.zeros(N)
    return x_arr, y_arr

def uniformSearchMethod(N=1, a=0, b=1):
    """
    Метод равномерного перебора

    Параметры
    ---------
    N : количество отрезков
    a : интервал ОТ
    b : интервал ДО
    """

    name = "Метод равномерного перебора"
    print(name)
    x_arr, y_arr = init_xy(N)
    v_x = 0
    v_y = 0
    step = (b - a) / N
    f_min = sys.maxsize
    for i in range(1, N+1, 1):
        x = (a + i * step) - step / 2
        f_val = func1(x)
        if (f_val < f_min):
            f_min = f_val
            v_x = x
            v_y = f_min

        x_arr[i-1] = x
        y_arr[i-1] = f_val

    print("Результат: v =", f_min)
    return x_arr, y_arr, v_x, v_y, name

def dichotomyMethod(N=1, a=0, b=1):
    """
    Метод дихотомии

    Параметры
    ---------
    N : количество отрезков
    a : интервал ОТ
    b : интервал ДО
    """

    print("Метод дихотомии")


