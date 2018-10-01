#!/usr/bin/python
#  -*- coding: utf-8 -*-
import tkinter as tk

# Chaine qui contient l'operation a faire
operation = []

# Ensemble des operandes utilises pour les calculs
symbolArray = ['+', '-', '*', '/']


# Ajout du chiffre dans le calcul
def nb_op(number):
    operation.append(number)
    result.configure(text=operation)


# Ajout de l'operande dans la chaine de caracteres et calcul
def symbol_op(symbol):
    if symbol == '=':
        try:
            calculation = eval("".join(operation))
            result.configure(text=calculation)
            operation.clear()
            operation.append(str(calculation))
        except SyntaxError:
            result.configure(text='Error')
            operation.clear()

    else:
        if len(operation) > 0 and operation[len(operation) - 1] in symbolArray and symbol:
            operation[len(operation) - 1] = symbol
        else:
            if len(operation) == 0 and (symbol == ')' or symbol == '.'):
                None
            else:
                operation.append(symbol)

        result.configure(text=operation)


# Nettoie l'affichage et supprime l'operation a faire
def reset_display():
    operation.clear()
    result.configure(text='')


# Declaration d'une fenetre graphique
calculator = tk.Tk()
calculator.title('Calculator')

# Ecran qui va afficher le resultat
result = tk.Label(calculator, text='')
result.grid(row=0, columnspan=4)

# Declaration des boutons et de leur positionnement dans la fenetre graphique
b1 = tk.Button(calculator, text="1", command=lambda: nb_op('1'))
b1.grid(row=1, column=0)

b2 = tk.Button(calculator, text="2", command=lambda: nb_op('2'))
b2.grid(row=1, column=1)

b3 = tk.Button(calculator, text="3", command=lambda: nb_op('3'))
b3.grid(row=1, column=2)

b4 = tk.Button(calculator, text="4", command=lambda: nb_op('4'))
b4.grid(row=2, column=0)

b5 = tk.Button(calculator, text="5", command=lambda: nb_op('5'))
b5.grid(row=2, column=1)

b6 = tk.Button(calculator, text="6", command=lambda: nb_op('6'))
b6.grid(row=2, column=2)

b7 = tk.Button(calculator, text="7", command=lambda: nb_op('7'))
b7.grid(row=3, column=0)

b8 = tk.Button(calculator, text="8", command=lambda: nb_op('8'))
b8.grid(row=3, column=1)

b9 = tk.Button(calculator, text="9", command=lambda: nb_op('9'))
b9.grid(row=3, column=2)

b0 = tk.Button(calculator, text="0", command=lambda: nb_op('0'))
b0.grid(row=4, column=0)

bEq = tk.Button(calculator, text="=", command=lambda: symbol_op('='))
bEq.grid(row=4, column=2)

bInit = tk.Button(calculator, text="C", command=lambda: reset_display())
bInit.grid(row=4, column=1)

bPlus = tk.Button(calculator, text="+", command=lambda: symbol_op('+'))
bPlus.grid(row=1, column=4)

bLess = tk.Button(calculator, text="-", command=lambda: symbol_op('-'))
bLess.grid(row=2, column=4)

bTime = tk.Button(calculator, text="*", command=lambda: symbol_op('*'))
bTime.grid(row=3, column=4)

bDivided = tk.Button(calculator, text="/", command=lambda: symbol_op('/'))
bDivided.grid(row=4, column=4)

# Affichage du graphique
calculator.mainloop()
