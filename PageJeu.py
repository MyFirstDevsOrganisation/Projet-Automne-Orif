import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
class PageJeu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.createWidgets()
        self.config(bg="#87CEEB")
        self.infinitif = ""
        self.preterit = ""
        self.partPass = ""
        self.apiUrl = "http://192.168.7.98:3000/api/recuperer-verbe-aleatoirement"

    def createWidgets(self):
        explicationLabel = tk.Label(self, text="Saisissez les temps manquants", font=("Helvetica", 15), bg='#87CEEB')
        explicationLabel.grid(row=0, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        infinitifInstruction = tk.Label(self, text="Infinitif", font=("Helvetica", 15), bg='#87CEEB')
        infinitifInstruction.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        champInfinitif = tk.Entry(self, width=15, font=("Helvetica", 15))
        champInfinitif.grid(row=10, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        preteriteInstruction = tk.Label(self, text="Prétérite", font=("Helvetica", 15), bg='#87CEEB')  
        preteriteInstruction.grid(row=15, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        champPreterite = tk.Entry(self, width=15, font=("Helvetica", 15))
        champPreterite.grid(row=20, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        partPassInstruction = tk.Label(self, text="Participe passé", font=("Helvetica", 15), bg='#87CEEB')
        partPassInstruction.grid(row=25, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        champPartPass = tk.Entry(self, width=15, font=("Helvetica", 15))
        champPartPass.grid(row=30, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        boutonValider = tk.Button(self, width=15, text="Valider", font=("Helvetica", 15))
        boutonValider.grid(row=35, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        quitterBoutton = tk.Button(self, text= "Quitter", width=15, command=self.confirmationQuitter)
        quitterBoutton.grid(row=40, column=1, columnspan=2, sticky=tk.NSEW, pady=5)
        
    def confirmationQuitter(self):
        reponse = messagebox.askyesno('Quitter', 'Voulez-vous vraiment quitter ?')
        if reponse:
            self.master.quit()

    # Méthode pour récupérer un verbe aléatoirement
    def recupererVerbe(self):
        headers = {
            'x-api-key': '-jIPpeeKh+6nvRF',  # Clé de l'API
            'Content-Type': 'application/json',  # Type de contenu
        }
        # Appel de l'API
        reponse = requests.get(self.apiUrl,headers=headers)
        # Récupération du JSON
        reponseJson = reponse.json()
        # Si le JSON contient des données
        if 'data' in reponseJson and len(reponseJson['data']) > 0: # Si le JSON contient des données
            verbe = reponseJson['data'][0]# Récupération du premier verbe
            self.infinitif = verbe.get('infinitif', '')# Récupération de l'infinitif
            self.preterit = verbe.get('preterit', '')# Récupération du prétérit
            self.partPass = verbe.get('participe_passe', '')# Récupération du participe passé
     
  


    