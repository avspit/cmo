import matplotlib.pyplot as plt
from lab01 import uniformSearchMethod as usm

if __name__ == '__main__':
    plt.rcParams['figure.figsize'] = [15, 5]
    x_arr, y_arr, x, y, name = usm(N=5, a=-5, b=5)
    plt.subplot(2, 4, 1)
    plt.title(name)
    plt.plot(x_arr, y_arr)
    plt.scatter(x, y, color="red")
    plt.show()
