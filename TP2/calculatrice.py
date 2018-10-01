from tkinter import *


class Interface(Frame):

    def __init__(self, fenetre, **kwargs):
        self.resultat = StringVar()
        self.resultat.set("0")
        Frame.__init__(self, fenetre, width=800, height=600, **kwargs)
        self.pack(fill=BOTH)

        # Création de nos widgets
        self.affichage = Label(self, textvariable=self.resultat).grid(row=0)

        self.bou7 = Button(self, text='7', width=8, command=self.cliquer).grid(row=1, column=0)

        self.bou8 = Button(self, text='8', width=8, command=self.cliquer).grid(row=1, column=1)

        self.bou9 = Button(self, text='9', width=8, command=self.cliquer).grid(row=1, column=2)

        self.bou4 = Button(self, text='4', width=8, command=self.cliquer).grid(row=2, column=0)

        self.bou5 = Button(self, text='5', width=8, command=self.cliquer).grid(row=2, column=1)

        self.bou6 = Button(self, text='6', width=8, command=self.cliquer).grid(row=2, column=2)

        self.bou1 = Button(self, text='1', width=8, command=self.cliquer).grid(row=3, column=0)

        self.bou2 = Button(self, text='2', width=8, command=self.cliquer).grid(row=3, column=1)

        self.bou3 = Button(self, text='3', width=8, command=self.cliquer).grid(row=3, column=2)

        self.bouC = Button(self, text='=', width=8, command=self.cliquer).grid(row=4, column=0)

        self.bou0 = Button(self, text='0', width=8, command=self.cliquer).grid(row=4, column=1)

        self.bouQ = Button(self, text='Quitter', width=8, command=self.quit).grid(row=4, column=2)

    def cliquer(self):
        print("appuyé")
        var = self.resultat.get() + "0"
        self.resultat.set(var)