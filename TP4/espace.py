from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = plt.axes(projection='3d')


#matrice_constante = np.linspace(0.3, 0.8, 10)
X = np.arange(-1, 1, 1)
print(X)
Y = np.linspace(0.5, 0.6, 10)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)

Z = np.sin(R)
ax.plot_surface(X, Y, R, rstride=1, cstride=1, cmap='hot')
plt.show()