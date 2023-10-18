import tkinter as tk
from tkinter import *

class PageJeu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill=BOTH, expand=True)

        self.label = tk.Label(self, text="Page Jeu")
        self.label.pack(pady=10, padx=10)

        self.retour = tk.Button(self, text="Retour")
        self.retour.pack(pady=10, padx=10)