import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PageJeu import PageJeu

class PageAccueil(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.createWidgets()
        self.config(bg = "#87CEEB")
        self.pack(fill=BOTH, expand=True)

    def createWidgets(self):
        explicationLabel = tk.Label(self, text="Nous allons vous donner un verbe irrégulier \nVous allez devoir le conjuger a l'infinitif, au prétérit et au passé-composé\n \n Bonne chance ! ", font=("Helvetica", 15), bg= "#87CEEB" )
        explicationLabel.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW, pady=30, padx=85)

        demarrerBoutton = tk.Button(self, text = "Start", height=5, width=10, command=self.afficherPageJeu, font=("Helvetica", 10))
        demarrerBoutton.grid(row=9, column=1, columnspan=20,pady=55, ipadx=20)

        quitterBoutton = tk.Button(self, text= "Quitter", height=5, width=10, command=self.confirmationQuitter,font=("Helvetica", 10))
        quitterBoutton.grid(row=30, column=1, columnspan=30,pady=15,ipadx=20)

    def afficherPageJeu(self):
        self.pack_forget()
        self.page_jeu = PageJeu(self.master)

    def confirmationQuitter(self):
        reponse = messagebox.askyesno('Quitter', 'Voulez-vous vraiment quitter ?')
        if reponse:
            self.master.quit()