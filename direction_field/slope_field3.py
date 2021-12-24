import numpy as np
import matplotlib.pyplot as plt


def plot1():
    nx, ny = .3, .3
    x = np.arange(-3, 3, nx)
    y = np.arange(-2, 2, ny)
    X, Y = np.meshgrid(x, y)

    plt.plot(X, Y, marker=".", color='k', linestyle='none')
    plt.xticks(x, rotation='45')
    plt.yticks(y)
    plt.title('grid plot with points, Single Colour')
    plt.show()

def plot2():
    nx, ny = .3, .3
    x = np.arange(-3, 3, nx)
    y = np.arange(-2, 2, ny)

    # rectangular grid with points
    X, Y = np.meshgrid(x, y)

    # derivative
    dy = X + np.sin(Y)
    dx = np.ones(dy.shape)

    # plot
    plt.quiver(X, Y, dx, dy, color='purple')
    plt.title('Direction Field for y\'(x) = x + sin(y)')
    plt.show()

def plot3():
    nx, ny = .3, .3
    x = np.arange(-3, 3, nx)
    y = np.arange(-2, 2, ny)
    X, Y = np.meshgrid(x, y)

    dy = X + np.sin(Y)
    dx = np.ones(dy.shape)

    # normalize arrows
    dyu = dy /np.sqrt(dx**2 + dy**2)
    dxu = dx /np.sqrt(dx**2 + dy**2)

    # plot
    plt.quiver(X, Y, dxu, dyu, color='purple')
    plt.title('Normalized Direction Field for y\'(x) = x + sin(y)')
    plt.show()

def plot4():
    nx, ny = .3, .3
    x = np.arange(-3, 3, nx)
    y = np.arange(-2, 2, ny)

    # rectangular grid with points
    X, Y = np.meshgrid(x, y)

    # derivative
    dy = X + np.sin(Y)
    dx = np.ones(dy.shape)

    # normalize arrows
    dyu = dy /np.sqrt(dx**2 + dy**2)
    dxu = dx /np.sqrt(dx**2 + dy**2)

    # plot
    plt.quiver(X, Y, dxu, dyu, color='teal', headaxislength=2, headlength=0,
               pivot='middle', scale=10, linewidth=.2, units='xy', width = .02, headwidth=1)
    plt.title('Normalized Direction Field for y\'(x) = x + sin(y) without arrows')
    plt.show()

def plot5():
    nx, ny = .5, .5
    x = np.arange(-3, 5, nx)
    y = np.arange(-3, 5, ny)
    X, Y = np.meshgrid(x, y)

    dy = X**2 - Y
    dx = np.ones(dy.shape)
    dyu = dy /np.sqrt(dx**2 + dy**2)
    dxu = dx /np.sqrt(dx**2 + dy**2)

    plt.quiver(X, Y, dxu, dyu, color='purple')
    plt.title('Normalized Direction Field for y\'(x) = x^2 - y')
    plt.show()

plot1()
plot2()
plot3()
plot4()
plot5()
