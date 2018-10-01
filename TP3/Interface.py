from tkinter import *
from TP3.Parser import *
import hashlib

class Authentication:

    def __init__(self):
        self._interface = Tk()
        self._credentials_file = 'credentials.csv'

        # Declaration d'une nouvelle instance de parseur
        self._Parser = Parser()


        # Labels contenant les infos a rentrer
        self._ConLabel = Label(self._interface, text='Connection Interface').grid(row=0)
        self._LoginLabel = Label(self._interface, text='Login:').grid(row=1, column=0)
        self._PwdLabel = Label(self._interface, text='Password:').grid(row=2, column=0)

        # Bouton pour la validation du choix
        self._BAuth = Button(self._interface, text='Validate', command=self._check_connection()).grid(row=2, column=2)

        # Champ ou le login sera ecrit
        self._LoginEntry = StringVar()
        self._LoginEntry.set('Empty')
        self._Login = Entry(self._interface, textvariable=str, width=30)
        self._Login.grid(row=1, column=1)

        # Champ ou le login sera ecrit
        self._PwdEntry = StringVar()
        self._PwdEntry.set('Empty')
        self._Pwd = Entry(self._interface, textvariable=str, width=30)
        self._Pwd.grid(row=2, column=1)

        self._interface.title('Authentication')


    def loop(self):
        ## Affiche le graphique
        self._interface.mainloop()


    def _check_connection(self):
        #if
        _credentials = self._Parser.read_file(self._credentials_file)
        _credentials = _credentials.split(',')

        ## on verifie que les labels ne sont pas vides
        if not self._LoginEntry.get() and not self._PwdEntry.get():
            if self._LoginEntry.get() == _credentials[0] and self._PwdEntry.get() == _credentials[1]:
                _window = Tk()
                _label = Label(_window, text='Vous etes bien authentifies !').pack()
                _window.mainloop()
            else:
                _window = Tk()
                _label = Label(_window, text='Les informations saisies sont incorrectes !').pack()
                _window.mainloop()


