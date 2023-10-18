import tkinter as tk
from tkinter import *
from tkinter import messagebox

class PageJeu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.createWidgets()
        self.config(bg="#87CEEB")

    def createWidgets(self):
        explicationLabel = tk.Label(self, text="Saisissez les temps manquants", font=("Helvetica", 15), bg='#87CEEB')
        explicationLabel.grid(row=0, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        infinitifInstruction = tk.Label(self, text="Infinitif", font=("Helvetica", 15), bg='#87CEEB')
        infinitifInstruction.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        champinfinitif = tk.Entry(self, width=15, font=("Helvetica", 15))
        champinfinitif.grid(row=10, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        preteriteInstruction = tk.Label(self, text="Prétérite", font=("Helvetica", 15), bg='#87CEEB')  
        preteriteInstruction.grid(row=15, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        champpreterite = tk.Entry(self, width=15, font=("Helvetica", 15))
        champpreterite.grid(row=20, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        partPassInstruction = tk.Label(self, text="Participe passé", font=("Helvetica", 15), bg='#87CEEB')
        partPassInstruction.grid(row=25, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        champpartPass = tk.Entry(self, width=15, font=("Helvetica", 15))
        champpartPass.grid(row=30, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        boutonValider = tk.Button(self, width=15, text="Valider", font=("Helvetica", 15))
        boutonValider.grid(row=35, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        quitterBoutton = tk.Button(self, text= "Quitter", width=15, command=self.confirmationQuitter)
        quitterBoutton.grid(row=40, column=1, columnspan=2, sticky=tk.NSEW, pady=5)
        
    def confirmationQuitter(self):
        reponse = messagebox.askyesno('Quitter', 'Voulez-vous vraiment quitter ?')
        if reponse:
            self.master.quit()
    