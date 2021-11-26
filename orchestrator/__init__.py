import matplotlib.pyplot as plt
from lab01 import uniformSearchMethod as usm
from lab01 import dichotomyMethod as dm
from lab01 import goldenSectionSearch as gss
from lab02 import gradientDescent as gd
from util import lab01_func_unimodal, lab02_func
import numpy as np


def init_lab01_variables():
    N = 100
    acc = 0.001
    a = -5
    b = 8
    return N, acc, a, b


def lab_01():
    """
        Лабораторная работа № 1
    """

    N, acc, a, b = init_lab01_variables()

    plt.rcParams['figure.figsize'] = [15, 4]
    fig = plt.figure(0)
    fig.canvas.set_window_title('Лабоработная работа 1')

    x_arr, y_arr, min_point_x, min_point_y, name = usm(lab01_func_unimodal, N=N, a=a, b=b)
    plt.subplot(1, 3, 1)
    plt.title(name)
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.plot(x_arr, y_arr)
    plt.plot(min_point_x, min_point_y, 'ro')

    x_arr, y_arr, min_point_x, min_point_y, name = dm(lab01_func_unimodal, acc=acc, N=N, a=a, b=b)
    plt.subplot(1, 3, 2)
    plt.title(name)
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.plot(x_arr, y_arr)
    plt.plot(min_point_x, min_point_y, 'ro')

    x_arr, y_arr, min_point_x, min_point_y, name = gss(lab01_func_unimodal, acc=acc, N=N, a=a, b=b)
    plt.subplot(1, 3, 3)
    plt.title(name)
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.plot(x_arr, y_arr)
    plt.plot(min_point_x, min_point_y, 'ro')

    plt.show()


def plotFunc(x0):
    x = np.linspace(-5, 7, 100)
    plt.plot(x, lab02_func(x))
    plt.plot(x0, lab02_func(x0), 'ro')
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')

def plotPath(xs, ys, x0):
    plotFunc(x0)
    plt.plot(xs, ys, linestyle='--', marker='o', color='coral')
    plt.plot(xs[-1], ys[-1], 'ro')


def fprime(x):
    return 2*x - 2


def lab_02():
    """
    Лабораторная работа № 2
    """

    plt.rcParams['figure.figsize'] = [15, 9]
    fig = plt.figure(0)
    fig.canvas.set_window_title('Лабоработная работа 2')

    x0 = -4

    xs, ys = gd(lab02_func, fprime, x0, alpha=0.1, rule='1dmin')
    plt.subplot(3, 1, 1)
    plt.title('Метод одномерной минимизации')
    plotPath(xs, ys, x0)
    plt.quiver(xs[:-1], ys[:-1], xs[1:] - xs[:-1], ys[1:] - ys[:-1], scale_units='xy', angles='xy', scale=1,
               color='steelblue')

    xs, ys = gd(lab02_func, fprime, x0, alpha=0.1, rule='armijo')
    plt.subplot(3, 1, 2)
    plt.title('Правило Армихо')
    plotPath(xs, ys, x0)
    plt.quiver(xs[:-1], ys[:-1], xs[1:] - xs[:-1], ys[1:] - ys[:-1], scale_units='xy', angles='xy', scale=1,
               color='steelblue')

    xs, ys = gd(lab02_func, fprime, x0, alpha=0.1, rule='constant')
    plt.subplot(3, 1, 3)
    plt.title('Постоянный параметр (постоянная альфа)')
    plotPath(xs, ys, x0)
    plt.quiver(xs[:-1], ys[:-1], xs[1:] - xs[:-1], ys[1:] - ys[:-1], scale_units='xy', angles='xy', scale=1,
               color='steelblue')

    plt.show()