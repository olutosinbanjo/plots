import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

fig = plt.figure()

def vf(x, t):
    dx = np.zeros(2)
    dx[0] = 1.0
    dx[1] = x[0] ** 2 - x[0] - 2.0
    return dx

# Solution curves
t0 = 0.0
tEnd = 10.0

# Vector field
X, Y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-10, 10, 20))
U = 1.0
V = X ** 2 - X - 2
# Normalize arrows
N = np.sqrt(U ** 2 + V ** 2)
U = U / N
V = V / N
plt.quiver(X, Y, U, V, angles="xy")

t = np.linspace(t0, tEnd, 100)
for y0 in np.linspace(-5.0, 0.0, 10):
    y_initial = [y0, -10.0]
    y = odeint(vf, y_initial, t)
    plt.plot(y[:, 0], y[:, 1], "-")

plt.xlim([-5, 5])
plt.ylim([-10, 10])
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")


