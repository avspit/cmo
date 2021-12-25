from sympy import symbols

lab01_func_unimodal = lambda x: (x - 3) ** 2 # на отрезке [-5,8]
#lab01_func_unimodal = lambda x: x ** 2 # на отрезке [-1,1]
#lab01_func_unimodal = lambda x: x**2 # на отрезке [-12,5]
#lab01_func_unimodal = lambda x: math.sin(x) # на отрезке [3,5]

lab02_func = lambda x: x**2 - 2 * x - 3

x1 = symbols("x1")
x2 = symbols("x2")
lab03_func = lambda x1, x2: 100 * (x1 ** 2 - x2 ** 2) ** 2 + (x1 - 1) ** 2

