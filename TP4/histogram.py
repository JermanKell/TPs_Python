import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#Exercice5a
x = np.random.randn(10, 4)
print(x)

colors = ['red', 'blue', 'green', 'yellow']
plt.hist(x, density=True, histtype='bar', color=colors, label=colors)

plt.show()