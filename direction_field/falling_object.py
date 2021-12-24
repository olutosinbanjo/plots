import numpy as np
import matplotlib.pyplot as plt


nt, nv = 1, 1
t = np.arange(1, 11, nt)
v = np.arange(40, 61, nv)

# rectangular grid with points
T, V = np.meshgrid(t, v)

# derivative
dv = 9.8 - (V / 5)
dt = np.ones(dv.shape)

def direction_field():
    plt.quiver(T, V, dt, dv, color='black', headaxislength=5, headlength=0,
                pivot='middle', scale=2, linewidth=.2, units='xy', width = .05, headwidth=1)
    plt.title('Direction Field for v\'(t) = 9.8 - v/5')
    plt.show()

def direction_equilibrium():
    zero_index = np.where(dv == 0) # get index of zero elements
    equilibrium_solution = V[zero_index] # get the values of V which makes dv == 0

    # Plot equilibrium position
    plt.axhline(y=equilibrium_solution[0], color='black', linestyle='-')

    # Plot direction field
    plt.quiver(T, V, dt, dv, color='black', headaxislength=5, headlength=0,
                pivot='middle', scale=2, linewidth=.2, units='xy', width = .05, headwidth=1)
    plt.title('Direction Field and Equilibrium Solution for v\'(t) = 9.8 - v/5')
    plt.show()

direction_field()
direction_equilibrium()
