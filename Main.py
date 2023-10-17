import tkinter as tk
from tkinter import *
from PageAccueil import PageAccueil


class Application(tk.Tk):
   def __init__(self):
        super().__init__()

        self.title("Révision des verbes en Anglais")
        self.maxsize(800,600)
        self.minsize(400,400)
        self.config(bg = "#87CEEB")

        self.page_accueil = PageAccueil(self)
       

master = Application()
master.mainloop()