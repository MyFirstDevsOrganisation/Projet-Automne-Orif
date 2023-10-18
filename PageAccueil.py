import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Frame
import PageJeu



class PageAccueil(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.createWidgets()

    def createWidgets(self):
        explicationLabel = tk.Label(self, text="Choisissez le type de verbe que vous voulez reviser", font=("Helvetica", 15))
        demarrerBoutton = tk.Button(self, text = "Start", height=5, width=10, command=self.afficherPageJeu)


        explicationLabel.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW, pady=30)
        demarrerBoutton.grid(row=7, column=0, columnspan=2)


    def afficherPageJeu(self):
        self.pack_forget()
        self.page_jeu = PageJeu.PageJeu(self.master)
        self.page_jeu.pack()



