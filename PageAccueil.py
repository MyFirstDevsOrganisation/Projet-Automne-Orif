import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Frame



class PageAccueil(tk.Frame):
    def __init__(self, master):
        super().__init__(master)


        self.master = master


        self.demarrer = tk.Button(self, text = "Start", height=5, width=10)
        self.demarrer.pack()



