#importation des librairies
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
import requests
import random

class PageJeu(tk.Frame): # Création de la classe PageJeu qui hérite de la classe Frame
    def __init__(self, parent):# Constructeur de la classe
        super().__init__(parent) # Appel du constructeur de la classe parente
        self.parent = parent # Définition de l'attribut parent
        self.colorBg = "#87CEEB"
        self.config(bg=self.colorBg) # Configuration de la couleur de fond
        self.apiUrl = "http://192.168.2.15:3000/api/recuperer-verbe-aleatoirement" # Définition de l'URL de l'API
        self.infinitif = "" # Définition de l'attribut infinitif
        self.preterit = "" # Définition de l'attribut prétérit
        self.partPass = ""  # Définition de l'attribut participe passé
        self.champInfinitif = ""
        self.champPreterite = ""
        self.champPartPass = ""
        self.recupererVerbe() # Appel de la méthode récupérerVerbe
        self.createWidgets() # Appel de la méthode createWidgets
        self.randomVerbe() # Appel de la méthode randomVerbe

    # Méthode pour créer les widgets
    def createWidgets(self):
        # Création des widgets
        explicationLabel = tk.Label(self, text="Saisissez les temps manquants", font=("Helvetica", 15), bg=self.colorBg)
        explicationLabel.grid(row=0, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        infinitifInstruction = tk.Label(self, text="Infinitif", font=("Helvetica", 15), bg=self.colorBg)
        infinitifInstruction.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        self.champInfinitif = tk.Entry(self, width=15, font=("Helvetica", 15))
        self.champInfinitif.grid(row=10, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        preteriteInstruction = tk.Label(self, text="Prétérite", font=("Helvetica", 15), bg=self.colorBg)  
        preteriteInstruction.grid(row=15, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        self.champPreterite = tk.Entry(self, width=15, font=("Helvetica", 15))
        self.champPreterite.grid(row=20, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        partPassInstruction = tk.Label(self, text="Participe passé", font=("Helvetica", 15), bg=self.colorBg    )
        partPassInstruction.grid(row=25, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        self.champPartPass = tk.Entry(self, width=15, font=("Helvetica", 15))
        self.champPartPass.grid(row=30, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        boutonValider = tk.Button(self, width=15, text="Valider", font=("Helvetica", 15), command=lambda: self.verifierReponse(self.champInfinitif, self.champPreterite, self.champPartPass))
        boutonValider.grid(row=35, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        quitterBoutton = tk.Button(self, text= "Quitter", width=15, command=self.confirmationQuitter)
        quitterBoutton.grid(row=40, column=1, columnspan=2, sticky=tk.NSEW, pady=5)

    # Méthode pour confirmer la fermeture de l'application
    def confirmationQuitter(self):
        reponse = messagebox.askyesno('Quitter', 'Voulez-vous vraiment quitter ?') # Affichage d'une boîte de dialogue
        if reponse: # Si la réponse est oui
            self.master.quit() # Fermeture de l'application

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
        if 'data' in reponseJson and len(reponseJson['data']) > 0:
            verbe = reponseJson['data'][0]
            self.infinitif = verbe.get('infinitif', '')
            self.preterit = verbe.get('preterit', '')
            self.partPass = verbe.get('participe_passe', '')

    def randomVerbe(self):
        verbeRandom = random.choice([self.infinitif, self.preterit, self.partPass]) # Choix aléatoire d'un verbe   
        # Si le verbe aléatoire est l'infinitif, on affiche l'infinitif dans le champ correspondant
        if verbeRandom == self.infinitif:
            self.champInfinitif.insert(0, self.infinitif) # Insertion de l'infinitif dans le champ correspondant

        # Si le verbe aléatoire est le prétérit, on affiche le prétérit dans le champ correspondant    
        elif verbeRandom == self.preterit:
            self.champPreterite.insert(0, self.preterit) # Insertion du prétérit dans le champ correspondant
            
        # Si le verbe aléatoire est le participe passé, on affiche le participe passé dans le champ correspondant
        elif verbeRandom == self.partPass:
            self.champPartPass.insert(0, self.partPass) # Insertion du participe passé dans le champ correspondant

    def changerVerbe(self):
        self.recupererVerbe()
        for widget in self.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, END)  
                self.randomVerbe()

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
