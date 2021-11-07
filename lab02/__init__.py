import numpy as np

def ArmijoLineSearch(f, xk, pk, gfk, phi0, alpha0, rho=0.5, c1=1e-4):
    """Minimize over alpha, the function ``f(xₖ + αpₖ)``.
    α > 0 is assumed to be a descent direction.

    Parameters
    --------------------
    f : callable
        Function to be minimized.
    xk : array
        Current point.
    pk : array
        Search direction.
    gfk : array
        Gradient of `f` at point `xk`.
    phi0 : float
        Value of `f` at point `xk`.
    alpha0 : scalar
        Value of `alpha` at the start of the optimization.
    rho : float, optional
        Value of alpha shrinkage factor.
    c1 : float, optional
        Value to control stopping criterion.

    Returns
    --------------------
    alpha : scalar
        Value of `alpha` at the end of the optimization.
    phi : float
        Value of `f` at the new point `x_{k+1}`.
    """
    derphi0 = np.dot(gfk, pk)
    phi_a0 = f(xk + alpha0 * pk)

    while not phi_a0 <= phi0 + c1 * alpha0 * derphi0:
        alpha0 = alpha0 * rho
        phi_a0 = f(xk + alpha0 * pk)

    return alpha0, phi_a0

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

    # initialize x, f(x), and -f'(x)
    xk = x0
    fk = func(xk)
    gfk = fprime(xk)
    gfk_norm = np.linalg.norm(gfk)
    pk = -gfk
    # initialize number of steps, save x and f(x)
    num_iter = 0
    curve_x = [xk]
    curve_y = [fk]
    # take steps
    while gfk_norm > tol and num_iter < max_iter:
        # calculate new x, f(x), and -f'(x)

        if rule == 'armijo':
            alpha, fk = ArmijoLineSearch(func, xk, pk, gfk, fk, alpha0=alpha)
        elif rule == 'constant':
            alpha = 0.1

        xk = xk + alpha * pk
        fk = func(xk)
        pk = -fprime(xk)
        # increase number of steps by 1, save new x and f(x)
        num_iter += 1
        curve_x.append(xk)
        curve_y.append(fk)
    # print results
    if num_iter == max_iter:
        print('Градиентный спуск не сходится')
    else:
        print('Результат:\n  y = {:.4f}\n  x = {:.4f}'.format(fk, xk))
    print(num_iter)

    return np.array(curve_x), np.array(curve_y)

