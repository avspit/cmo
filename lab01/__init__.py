import sys
import numpy as np


def init_xy(N):
    x_arr = np.zeros(N)
    y_arr = np.zeros(N)
    return x_arr, y_arr


def init_min_point():
    min_point_x = 0
    min_point_y = 0
    return min_point_x, min_point_y


def prepare_func(f, N, a, b):
    x_arr = np.linspace(a,b,N)
    y_arr = np.zeros(N)
    for idx, val in enumerate(x_arr):
        y_arr[idx] = f(val)
    return x_arr, y_arr


def mDichotomyMethod(f, a, b, c, acc):
    y = (a + c) / 2
    f_y = f(y)
    if (b - a) <= acc:
        return y, f_y
    else:
        f_c = f(c)
        if f_y <= f_c:
            b = c
            c = y
        else:
            z = (c + b) / 2
            f_z = f(z)
            if f_c <= f_z:
                a = y
                b = z
            else:
                a = c
                c = z
        return mDichotomyMethod(f, a, b, c, acc)


def mGoldenSectionSearch(f, acc, a, b, phi):
    if (b - a) <= acc:
        result = (a + b) / 2
        return result, f(result)
    else:
        c = (b - a) / phi
        x1 = b - c
        x2 = a + c
        y1 = f(x1)
        y2 = f(x2)
        if y1 > y2:
            return mGoldenSectionSearch(f, acc, x1, b, phi)
        else:
            return mGoldenSectionSearch(f, acc, a, x2, phi)


def printResult(val):
    print('=> Результат: {:.4f}'.format(val))


def uniformSearchMethod(f, N=50, a=0, b=1):
    """
    Метод равномерного перебора

    Параметры
    ---------
    f : функция
    N : количество интервалов
    a : интервал ОТ
    b : интервал ДО
    """

    name = "Метод равномерного перебора"
    print(name)
    x_arr, y_arr = init_xy(N)
    min_point_x, min_point_y = init_min_point()

    step = (b - a) / N
    f_min = sys.maxsize
    for i in range(1, N+1, 1):
        x = (a + i * step) - step / 2
        f_val = f(x)
        if (f_val < f_min):
            f_min = f_val
            min_point_x = x
            min_point_y = f_min

        x_arr[i-1] = x
        y_arr[i-1] = f_val

    printResult(min_point_x)
    return x_arr, y_arr, min_point_x, min_point_y, name


def dichotomyMethod(f, acc=0.01, N=50, a=0, b=1):
    """
    Метод дихотомии

    Параметры
    ---------
    f : функция
    acc : точность
    N : количество интервалов
    a : интервал ОТ
    b : интервал ДО
    """

    name = "Метод дихотомии"
    print(name)
    x_arr, y_arr = prepare_func(f, N, a, b)
    c = (a + b) / 2
    min_point_x, min_point_y = mDichotomyMethod(f, a, b, c, acc)

    printResult(min_point_x)
    return x_arr, y_arr, min_point_x, min_point_y, name


def goldenSectionSearch(f, acc=0.01, N=50, a=0, b=1):
    """
    Метод золотого сечения

    Параметры
    ---------
    f : функция
    acc : точность
    N : количество интервалов
    a : интервал ОТ
    b : интервал ДО
    """

    name = "Метод золотого сечения"
    print(name)
    x_arr, y_arr = prepare_func(f, N, a, b)

    phi = (1 + np.sqrt(5)) / 2
    min_point_x, min_point_y = mGoldenSectionSearch(f, acc, a, b, phi)

    printResult(min_point_x)
    return x_arr, y_arr, min_point_x, min_point_y, name


