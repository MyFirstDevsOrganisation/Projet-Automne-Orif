import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
import requests

class PageJeu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.colorBg = "#87CEEB"
        self.config(bg=self.colorBg)
        self.apiUrl = "http://192.168.2.15:3000/api/recuperer-verbe-aleatoirement"
        self.infinitif = ""
        self.preterit = ""
        self.partPass = ""
        self.champInfinitif = ""
        self.champPreterite = ""
        self.champPartPass = ""
        self.recupererVerbe()
        self.createWidgets()

    def createWidgets(self):
        explicationLabel = tk.Label(self, text="Saisissez les temps manquants", font=("Helvetica", 15), bg=self.colorBg)
        explicationLabel.grid(row=0, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        infinitifInstruction = tk.Label(self, text="Infinitif", font=("Helvetica", 15), bg=self.colorBg)
        infinitifInstruction.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        self.champInfinitif = tk.Entry(self, width=15, font=("Helvetica", 15))
        self.champInfinitif.grid(row=10, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        self.champInfinitif.insert(0, self.infinitif)
        
        preteriteInstruction = tk.Label(self, text="Prétérite", font=("Helvetica", 15), bg=self.colorBg)  
        preteriteInstruction.grid(row=15, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        champPreterite = tk.Entry(self, width=15, font=("Helvetica", 15))
        champPreterite.grid(row=20, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        partPassInstruction = tk.Label(self, text="Participe passé", font=("Helvetica", 15), bg=self.colorBg    )
        partPassInstruction.grid(row=25, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        champPartPass = tk.Entry(self, width=15, font=("Helvetica", 15))
        champPartPass.grid(row=30, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        boutonValider = tk.Button(self, width=15, text="Valider", font=("Helvetica", 15), command=lambda: self.verifierReponse(self.champInfinitif, champPreterite, champPartPass))
        boutonValider.grid(row=35, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        quitterBoutton = tk.Button(self, text= "Quitter", width=15, command=self.confirmationQuitter)
        quitterBoutton.grid(row=40, column=1, columnspan=2, sticky=tk.NSEW, pady=5)
 
    def confirmationQuitter(self):
        reponse = messagebox.askyesno('Quitter', 'Voulez-vous vraiment quitter ?')
        if reponse:
            self.master.quit()

    def recupererVerbe(self):
        headers = {
            'x-api-key': '-jIPpeeKh+6nvRF',  
            'Content-Type': 'application/json',  
        }
        reponse = requests.get(self.apiUrl,headers=headers)
        reponseJson = reponse.json()
        if 'data' in reponseJson and len(reponseJson['data']) > 0:
            verbe = reponseJson['data'][0]
            self.infinitif = verbe.get('infinitif', '')
            self.preterit = verbe.get('preterit', '')
            self.partPass = verbe.get('participe_passe', '')

    def changerVerbe(self):
        self.recupererVerbe()
        for widget in self.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, END)
        self.champInfinitif.insert(0, self.infinitif)
        self.champPartPass.insert(0, self.partPass)
        self.champPreterite.insert(0, self.preterit)

    def verifierReponse(self, champInfinitif, champPreterite, champPartPass):
        reponseInfinitif = champInfinitif.get()
        reponsePreterite = champPreterite.get()
        reponsePartPass = champPartPass.get()

        print(self.infinitif, self.preterit, self.partPass)
        if reponseInfinitif == self.infinitif and reponsePreterite == self.preterit and reponsePartPass == self.partPass:
            self.parent.config(bg="green") 
            self.config(bg="green") 
            for widget in self.winfo_children():
                widget.configure(bg="green")
            self.after(500, self.retablirCouleur)
            self.after(500, self.changerVerbe)
        else:
            self.parent.config(bg="red") 
            self.config(bg="red") 
            for widget in self.winfo_children():
                widget.configure(bg="red")
            self.after(1000, self.retablirCouleur)

    def retablirCouleur(self):
        self.parent.config(bg=self.colorBg)
        self.config(bg=self.colorBg)
        for widget in self.winfo_children():
            widget.configure(bg=self.colorBg)
            if isinstance(widget, tk.Entry):
                widget.configure(bg="white")