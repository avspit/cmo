import sys
from util import func1

def uniformSearchMethod(N=1, a=0, b=1):
    """
    Метод равномерного перебора

    Параметры
    ---------
    N : количество отрезков
    a : интервал ОТ
    b : интервал ДО
    """

    print("Метод равномерного перебора")
    step = (b - a) / N
    f_min = sys.maxsize
    for i in range(1, N+1, 1):
        x = (a + i * step) - step / 2
        f_val = func1(x)
        if (f_val < f_min):
            f_min = f_val
    print("Результат: v =", f_min)






