# import des librairies
import tkinter as tk
from tkinter import *
from PageAccueil import PageAccueil
from PageJeu import PageJeu
from tkinter import messagebox

# Création de la classe Application qui hérite de la classe Tk
class Application(tk.Tk):
   def __init__(self, title, maxWidth, maxHeight, minWidth, minHeight): # Constructeur de la classe
        super().__init__() # Appel du constructeur de la classe parente

        # Configuration de la fenêtre
        self.title(title)
        self.maxsize(maxWidth, maxHeight)
        self.minsize(minWidth, minHeight)
        self.config(bg = "#87CEEB")
        self.page_accueil = PageAccueil(self)

         # Création du menu
        self.page_accueil.pack()