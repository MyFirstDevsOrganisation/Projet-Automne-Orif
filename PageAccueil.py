import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PageJeu import PageJeu
#from Application import Application

class PageAccueil(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.createWidgets()

    def createWidgets(self):
        explicationLabel = tk.Label(self, text="Choisissez le type de verbe que vous voulez reviser", font=("Helvetica", 15), bg='#87CEEB')
        explicationLabel.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW, pady=30)

        demarrerBoutton = tk.Button(self, text = "Start", height=5, width=10, command=self.afficherPageJeu)
        demarrerBoutton.grid(row=9, column=1, columnspan=2)

        quitterBoutton = tk.Button(self, text= "Quitter", height=5, width=10, command=self.confirmationQuitter)
        quitterBoutton.grid(row=12, column=1, columnspan=2)

    def afficherPageJeu(self):
        self.pack_forget()
        self.page_jeu = PageJeu(self.master)
        self.page_jeu.pack()

    def confirmationQuitter(self):
        reponse = messagebox.askyesno('Quitter', 'Voulez-vous vraiment quitter ?')
        if reponse:
            self.master.quit()