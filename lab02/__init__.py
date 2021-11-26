import numpy as np


def ArmijoLineSearch(f, xk, pk, gfk, phi0, alpha0, rho=0.5, c1=1e-4):
    """
        Правило Армихо

        Параметры
        --------------------
        f : функция
        xk : текущая точка
        pk : направление поиска
        gfk : градиент от функции в точке `xk`.
        phi0 : значение функции в точке `xk`.
        alpha0 : значение альфы в начале оптимизации
        rho : значение альфы после деления
        c1 : условие остановки

        Возвращает
        --------------------
        alpha : значение `alpha` в конце оптимизации
        phi : значение функции в новой точке `x_{k+1}`.
    """
    derphi0 = np.dot(gfk, pk)
    phi_a0 = f(xk + alpha0 * pk)

    while not phi_a0 <= phi0 + c1 * alpha0 * derphi0:
        alpha0 = alpha0 * rho
        phi_a0 = f(xk + alpha0 * pk)

    return alpha0, phi_a0


def rule_name_by_code(rule):
    if rule == '1dmin':
        return 'Метод одномерной минимизации'
    elif rule == 'constant':
        return 'Постоянный параметр (постоянная альфа)'
    elif rule == 'armijo':
        return 'Правило Армихо'
    else:
        return ''


def gradientDescent(func, fprime, x0, alpha, tol=1e-5, max_iter=1000, rule='1dmin'):
    """
        Лабораторная работа № 1

        Параметры
        ---------
        rule : правило расчета альфы, доступные значения:
            armijo - правило Армихо
            constant - постоянный параметр (постоянная альфа)
            1dmin - Метод одномерной минимизации
    """

    # инициализируем x, f(x), and -f'(x)
    xk = x0
    fk = func(xk)
    gfk = fprime(xk)
    gfk_norm = np.linalg.norm(gfk)
    pk = -gfk
    # инициализируем количество шагов, сохраняем x и f(x)
    num_iter = 0
    curve_x = [xk]
    curve_y = [fk]

    while gfk_norm > tol and num_iter < max_iter:
        # рассчитываем новый x, f(x) и -f'(x)

        if rule == 'armijo':
            alpha, fk = ArmijoLineSearch(func, xk, pk, gfk, fk, alpha0=alpha)
        elif rule == 'constant':
            alpha = 0.1

        xk = xk + alpha * pk
        fk = func(xk)
        pk = -fprime(xk)
        # увеличиваем счетчик на 1, сохраняем новый x и f(x)
        num_iter += 1
        curve_x.append(xk)
        curve_y.append(fk)
    print('Результат (' + rule_name_by_code(rule)  + '):\n  x = {:.4f}\n  y = {:.4f}'.format(fk, xk))

    return np.array(curve_x), np.array(curve_y)

