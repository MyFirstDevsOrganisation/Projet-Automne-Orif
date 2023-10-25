#importation des librairies
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
import random

class PageJeu(tk.Frame): # Création de la classe PageJeu qui hérite de la classe Frame
    def __init__(self, parent):# Constructeur de la classe
        super().__init__(parent) # Appel du constructeur de la classe parente
        self.parent = parent # Définition de l'attribut parent
        self.config(bg="#87CEEB") # Configuration de la couleur de fond
        self.apiUrl = "http://192.168.2.15:3000/api/recuperer-verbe-aleatoirement" # Définition de l'URL de l'API
        self.infinitif = "" # Définition de l'attribut infinitif
        self.preterit = "" # Définition de l'attribut prétérit
        self.partPass = ""  # Définition de l'attribut participe passé
        self.recupererVerbe() # Appel de la méthode récupérerVerbe
        self.createWidgets() # Appel de la méthode createWidgets
    # Méthode pour créer les widgets
    def createWidgets(self):
        
        verbeRandom = random.choice([self.infinitif, self.preterit, self.partPass]) # Choix aléatoire d'un verbe

        # Création des widgets
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
        
        boutonValider = tk.Button(self, width=15, text="Valider", font=("Helvetica", 15), command=lambda: self.verifierReponse(champInfinitif, champPreterite, champPartPass))
        boutonValider.grid(row=35, column=1, columnspan=2, sticky=tk.NSEW, pady=20)
        
        quitterBoutton = tk.Button(self, text= "Quitter", width=15, command=self.confirmationQuitter)
        quitterBoutton.grid(row=40, column=1, columnspan=2, sticky=tk.NSEW, pady=5)

        # Si le verbe aléatoire est l'infinitif, on affiche l'infinitif dans le champ correspondant
        if verbeRandom == self.infinitif:
            champInfinitif.insert(0, self.infinitif) # Insertion de l'infinitif dans le champ correspondant

        # Si le verbe aléatoire est le prétérit, on affiche le prétérit dans le champ correspondant    
        elif verbeRandom == self.preterit:
            champPreterite.insert(0, self.preterit) # Insertion du prétérit dans le champ correspondant
            
        # Si le verbe aléatoire est le participe passé, on affiche le participe passé dans le champ correspondant
        elif verbeRandom == self.partPass:
            champPartPass.insert(0, self.partPass) # Insertion du participe passé dans le champ correspondant
            
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
        # Si le JSON contient des données
        if 'data' in reponseJson and len(reponseJson['data']) > 0: # Si le JSON contient des données
            verbe = reponseJson['data'][0]# Récupération du premier verbe
            self.infinitif = verbe.get('infinitif', '')# Récupération de l'infinitif
            self.preterit = verbe.get('preterit', '')# Récupération du prétérit
            self.partPass = verbe.get('participe_passe', '')# Récupération du participe passé
     
  
    # Méthode pour vérifier la réponse
    def verifierReponse(self, champInfinitif, champPreterite, champPartPass):
        # Récupération des réponses
        reponseInfinitif = str.lower(champInfinitif.get()) # Récupération de la réponse de l'infinitif et changement en minuscule
        reponsePreterite = str.lower(champPreterite.get()) # Récupération de la réponse du preterit et changement en minuscule
        reponsePartPass = str.lower(champPartPass.get()) # Récupération de la réponse du participe passé et changement en minuscule
        print(self.infinitif, self.preterit, self.partPass) # Affichage des réponses dans la console
        if reponseInfinitif == self.infinitif and reponsePreterite == self.preterit and reponsePartPass == self.partPass: # Si toutes les réponses sont correctes
            messagebox.showinfo("Bravo", "Bonne réponse") # Affichage d'une boîte de dialogue
            self.parent.config(bg="green") # Changement de la couleur de fond