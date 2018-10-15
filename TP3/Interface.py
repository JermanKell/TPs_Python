from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from TP3.Parser import *
from TP3.EncDecode import *
import hashlib

class Authentication:

    def __init__(self):
        self._interface = Tk()
        self._credentials_file = 'credentials.txt'

        # Declaration d'une nouvelle instance de parseur
        self._Parser = Parser()
        self._EncDec = EncoDecode()


        # Champ ou le login sera ecrit (Connexion)
        self._LoginEntry = StringVar()
        self._Login = Entry(self._interface, textvariable=self._LoginEntry, width=30)
        self._Login.grid(row=1, column=1)

        # Champ ou le login sera ecrit (connexion)
        self._PwdEntry = StringVar()
        self._Pwd = Entry(self._interface, textvariable=self._PwdEntry, width=30, show='*')
        self._Pwd.grid(row=2, column=1)

        ## Champs pour l'enregistrement du compte
        self._SULoginEntry = StringVar()
        self._SULogin = Entry(self._interface, textvariable=self._SULoginEntry, width=30)
        self._SULogin.grid(row=5, column=1)

        self._SUPwdEntry = StringVar()
        self._SUPwd = Entry(self._interface, textvariable=self._SUPwdEntry, width=30, show='*')
        self._SUPwd.grid(row=6, column=1)


        # Labels contenant les infos a rentrer
        self._ConLabel = Label(self._interface, text='Connection Interface').grid(row=0, column=0)

        self._connectionState = StringVar()
        self._connectionState.set("Not connected")
        self._ConnectionState = Label(self._interface, textvariable=self._connectionState).grid(row=0, column=2)

        self._LoginLabel = Label(self._interface, text='Login:').grid(row=1, column=0)
        self._PwdLabel = Label(self._interface, text='Password:').grid(row=2, column=0)

        # Labels pour l'enregistrement du compte
        self._SignUpLabel = Label(self._interface, text='Sign up').grid(row=4)
        self._SULoginLabel = Label(self._interface, text='Login:').grid(row=5, column=0)
        self._SUPwdLabel = Label(self._interface, text='Password:').grid(row=6, column=0)

        # Bouton pour la validation du choix
        self._BAuth = Button(self._interface, text='Validate', command=lambda: self._check_connection()).grid(row=2, column=2)

        ## Rajout du mot-cle lambda
        self._BSignUp = Button(self._interface, text='Sign Up', command=lambda: self._register_account()).grid(row=6, column=2)

        menubar = Menu(self._interface)
        self._interface.config(menu=menubar)

        modemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Mode", menu=modemenu)

        modemenu.add_command(label='File processing', command=self._fileprocess)

        self._interface.title('Authentication')


    def loop(self):
        ## Affiche le graphique
        self._interface.mainloop()

    def _check_connection(self):
        _credentials = self._Parser.read_file(self._credentials_file)
        _credentials_auth = "poly" + self._LoginEntry.get() + self._PwdEntry.get()
        _credentials_auth = hashlib.sha256(_credentials_auth.encode()).hexdigest()

        ## on verifie que les labels ne sont pas vides
        if _credentials_auth == _credentials:
            self._EncDec.setKey(_credentials_auth)
            messagebox.showinfo("Info", 'You are connected !')
            self._connectionState.set(self._LoginEntry.get())
            self._UserPwd = self._PwdEntry.get()

        else:
            messagebox.showerror("Error", 'Wrong connection info !')

        # Vide le contenu du label saisi par l'utilisateur
        self._LoginEntry.set("")
        self._PwdEntry.set("")

    def _register_account(self):
        # On encode le couple et on ajoute une partie fixe
        _crendentials_aut = "poly" + self._SULoginEntry.get() + self._SUPwdEntry.get()
        _crendentials_aut = hashlib.sha256(_crendentials_aut.encode()).hexdigest()

        _result = self._Parser.write_file(self._credentials_file, _crendentials_aut)

        if _result == 1:
            messagebox.showinfo("Info", 'You have created your account !')
        else:
            messagebox.showerror("Error", "An error occured during the signup !")

        # Supprime le contenu de ce qui a ete tape par l'utilisateur
        self._SULoginEntry.set("")
        self._SUPwdEntry.set("")


    def _fileprocess(self):
        if self._connectionState.get() != "Not connected":
            window = Tk()
            window.title("File processing")

            self._FileToOpenPath = NONE
            self._FileToSavePath = NONE

            # Methodes anonymes a lancer par l'appli
            def selectfile():
                dialog = filedialog.askopenfilename(title="Select a file", filetypes=[('Text files', '.txt')])
                self._FileToOpenPath = dialog
                messagebox.showinfo("Info", "File to open: " + self._FileToOpenPath)

            def savefile():
                dialog = filedialog.asksaveasfile(title="Save as ...", filetypes=[('Text files', '.txt')])
                self._FileToSavePath = dialog.name
                messagebox.showinfo("Info", "File to save: " + self._FileToSavePath)

            def encode():
                _dataToEncode = None

                if self._FileToOpenPath is not None and self._FileToSavePath is not None:
                    _dataToEncode = self._Parser.read_file(self._FileToOpenPath)
                    if _dataToEncode is not None:
                        _encData = self._EncDec.Encode(_dataToEncode)
                        self._Parser.write_file(self._FileToSavePath, _encData)
                else:
                    messagebox.showerror("Error", "Unable to process on a non existing file!")

            def decode():
                _dataToDecode = None

                if self._FileToOpenPath is not None and self._FileToSavePath is not None:
                    _dataToDecode = self._Parser.read_file(self._FileToOpenPath)
                    if _dataToDecode is not None:
                        __decData = self._EncDec.Decode(_dataToDecode)
                        self._Parser.write_file(self._FileToSavePath, __decData)

                else:
                    messagebox.showerror("Error", "Unable to process on a non existing file!")

            window.title("Files processing")
            labelStart = Label(window, text='Select a file to encrypt').grid(row=0)
            openFileButton = Button(window, text="Open file", command=selectfile).grid(row=1, column=0)

            labelEnd = Label(window, text='Select the destination file').grid(row=3)
            saveFileButton = Button(window, text="Save file", command=savefile).grid(row=4, column=0)

            EncButton = Button(window, text="To encode!", command=encode).grid(row=8, column=0)
            DecButton = Button(window, text="To decode!", command=decode).grid(row=8, column=1)

            # Affichage et traitement du graphique
            window.mainloop()

        else: messagebox.showerror("Error", "You must be connected to run this feature!")
