import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')
[x, t] = np.meshgrid(
    np.array(range(25)) / 24.0,
    np.arange(0, 575.5, 0.5) / 575 * 20 * np.pi + 4 * np.pi)
p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
change = np.sin(15 * t) / 150
u = 1 - (1 - np.mod(3.3 * t, 2 * np.pi) / np.pi)**4 / 2 + change
y = 2 * (x**2 - x)**2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p))
h = u * (x * np.cos(p) - y * np.sin(p))
c = plt.get_cmap('Reds')
surf = ax.plot_surface(r * np.cos(t),
                       r * np.sin(t),
                       h,
                       rstride=1,
                       cstride=1,
                       cmap=c,
                       linewidth=0,
                       antialiased=True)
plt.show()
