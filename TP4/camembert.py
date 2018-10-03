import matplotlib.pyplot as plt

fruits = 'Orange', 'Cherry', 'Blueberry', 'Apple'
nb_morceaux = [171, 144, 423, 272]
couleurs_fruits = ['orange', 'red', 'blue', 'yellow']
explode = (0, 0.1, 0.1, 0)

plt.pie(nb_morceaux, explode=explode, labels=fruits, colors=couleurs_fruits,
        autopct='%1.2f%%', shadow=True, startangle=30)

plt.show()