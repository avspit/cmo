import matplotlib.pyplot as plt
from lab01 import uniformSearchMethod as usm
from lab01 import dichotomyMethod as dm
from lab01 import goldenSectionSearch as gss
from util import func_unimodal

def lab_01(N, acc, a, b):
    plt.rcParams['figure.figsize'] = [15, 4]
    fig = plt.figure(0)
    fig.canvas.set_window_title('Лабоработная работа 1')

    x_arr, y_arr, min_point_x, min_point_y, name = usm(func_unimodal, N=N, a=a, b=b)
    plt.subplot(1, 3, 1)
    plt.title(name)
    plt.plot(x_arr, y_arr)
    plt.scatter(min_point_x, min_point_y, color="red")

    x_arr, y_arr, min_point_x, min_point_y, name = dm(func_unimodal, acc=acc, N=N, a=a, b=b)
    plt.subplot(1, 3, 2)
    plt.title(name)
    plt.plot(x_arr, y_arr)
    plt.scatter(min_point_x, min_point_y, color="red")

    x_arr, y_arr, min_point_x, min_point_y, name = gss(func_unimodal, acc=acc, N=N, a=a, b=b)
    plt.subplot(1, 3, 3)
    plt.title(name)
    plt.plot(x_arr, y_arr)
    plt.scatter(min_point_x, min_point_y, color="red")

    plt.show()


def lab_02():
    plt.rcParams['figure.figsize'] = [15, 4]
    fig = plt.figure(0)
    fig.canvas.set_window_title('Лабоработная работа 2')

    plt.show()