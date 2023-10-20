import tkinter as tk
from tkinter import *
from PageAccueil import PageAccueil
from PageJeu import PageJeu
from tkinter import messagebox



class Application(tk.Tk):
   def __init__(self, title, width, height):
        super().__init__()

        # Configuration de la fenêtre
        self.title(title)
        self.maxsize(width, height)
        self.minsize(width, height)
        self.config(bg = "#87CEEB")
        self.page_accueil = PageAccueil(self)


        self.page_accueil.pack()
        
        
