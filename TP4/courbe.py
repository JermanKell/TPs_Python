import numpy as np
import matplotlib.pyplot as plt

matrice_random = np.random.rand(100)
plt.plot(matrice_random, label='aléatoire')

matrice_constante = np.linspace(0, 1, 100)
plt.plot(matrice_constante, label='constante', linestyle='dashed', linewidth=1)


points = 100    #nb de points
f = 2    #nb de cycle sinusoidal
matrice_compteur = np.arange(points)
y = np.sin(2 * np.pi * f * matrice_compteur / points)
matrice_pondere = np.add(np.ones(points), y)/2
plt.plot(matrice_compteur, matrice_pondere, label='sinusoidal', marker='+', markersize=5, linestyle='None')

plt.xlabel('indice')
plt.ylabel('valeur')
plt.title("Un titre")
plt.legend()

plt.annotate('centre', xy=(50, 0.5), xytext=(75, 1.15),arrowprops=dict(facecolor='red', shrink=0.01), )

plt.ylim(0, 1.25)
plt.show()