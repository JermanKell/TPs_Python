import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.misc import imresize
from scipy.ndimage import rotate

#1
tab = np.random.randint(low=-10, high=11, size=(4, 3, 2))
print('nombre de dimensions=', tab.ndim, '\ndimension=', tab.shape, '\ntaille=',
      tab.size, '\ntype des éléments=', tab.dtype, '\ntaille des éléments=', tab.itemsize,
      '\ndonnées=', tab.data)

#2
mat1 = np.arange(9).reshape(3, 3)
mat2 = np.arange(2, 11).reshape(3, 3)
matProd = np.dot(mat1, mat2)
matTranspos = np.transpose(matProd)

#3
mat = np.array([(1,2,3), (0,1,4), (5,6,0)])
det = np.linalg.det(mat)
mat_inv = np.linalg.inv(mat)
one = np.transpose(np.ones(3))
mat_sol = np.linalg.solve(mat_inv, one)
val_propre, vec_propre = np.linalg.eig(mat)

#4
def func(x, a, b, c):
    return a * np.exp(-b * x) + c
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)

y_bruit = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_bruit
plt.plot(xdata, ydata, 'b-', label='données')
popt, pcov = curve_fit(func, xdata, ydata)

plt.plot(xdata, func(xdata, *popt), 'r-', label='approche: a=%.3f, b=%.3f, c=%.3f' % tuple(popt))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#5
image = plt.imread('PyMeme.jpg', format='jpg')
fig, ax = plt.subplots(2, 2)

image2 = imresize(image, 30)

rot = rotate(image, 180, reshape=False)

ax[0][0].imshow(image)
ax[0][1].imshow(image2)
ax[1][0].imshow(rot)

plt.show()
