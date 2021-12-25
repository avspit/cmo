import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from lab01 import uniformSearchMethod as usm
from lab01 import dichotomyMethod as dm
from lab01 import goldenSectionSearch as gss
from lab02 import gradientDescent as gd
from lab03 import davidonFletcherPowell as dfp
from lab04 import conjugateGradientDescent as cgd
from util import lab01_func_unimodal, lab02_func, lab03_func
import numpy as np
#import holoviews as hv
#hv.extension('plotly')


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


def fprime(f, x):
    return (f(x + 0.01) - f(x)) / 0.01


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


def lab_03():
    """
    Лабораторная работа № 3
    """

    plt.rcParams['figure.figsize'] = [9, 8]
    fig = plt.figure(0)
    fig.canvas.set_window_title('Лабоработная работа 3')

    ax = plt.axes(projection="3d")

    x = dfp()
    X = np.linspace(0, 2, 50)
    Y = np.linspace(-2, 2, 50)
    X, Y = np.meshgrid(X, Y)
    Z = lab03_func(X, Y)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0)

    ax.scatter(x[0], x[1], lab03_func(x[0], x[1]), color="red")

    name = 'Метод Давидона-Флетчера-Пауэлла'

    ax.set_title(name);

    print('Результат (' + name + '):\n  x = {:.4f}\n  y = {:.4f}'.format(x[0], x[1]))

    plt.show()


def viz_descent(x_steps, y_steps, A, b, fig, x):
    size = 50
    x1s = np.linspace(-6, 6, size)
    x2s = np.linspace(-6, 6, size)
    x1, x2  = np.meshgrid(x1s, x2s)
    Z = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            x = np.array([x1[i,j], x2[i,j]])
            Z[i,j] = 0.5 * x @ A @ x - x @ b

    ax = plt.axes(projection="3d")
    ax.set_title('Метод сопряженных градиентов');

    surf = ax.plot_surface(x1, x2, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0)

    points = np.concatenate([np.stack(x_steps), np.array(y_steps)[:, np.newaxis]], axis=1)

    size = len(points)
    x1, x2 = np.meshgrid(points[:, 0], points[:, 1])
    Z = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            x = np.array([x1[i,j], x2[i,j]])
            Z[i,j] = 0.5 * x @ A @ x - x @ b

    ax.scatter(x[0], x[1], 0.5 * x @ A @ x - x @ b, color="red")


def lab_04():
    """
    Лабораторная работа № 4
    """

    plt.rcParams['figure.figsize'] = [15, 9]
    fig = plt.figure(0)
    fig.canvas.set_window_title('Лабоработная работа 4')

    A = np.array([[3, 2], [2, 3]])
    b = np.array([-2, 7])

    x, x_steps, y_steps = cgd(A, b)
    viz_descent(x_steps, y_steps, A, b, fig, x)

    name = 'Метод сопряженных градиентов'

    print('Результат (' + name + '):\n  x = {:.4f}\n  y = {:.4f}'.format(x[0], x[1]))

    plt.show()