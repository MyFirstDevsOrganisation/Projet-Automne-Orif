# Importation des librairies
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PageJeu import PageJeu

# Création de la classe PageAccueil qui hérite de la classe Frame
class PageAccueil(tk.Frame):
    def __init__(self, parent): # Constructeur de la classe
        super().__init__(parent) # Appel du constructeur de la classe parente

        self.createWidgets() # Appel de la méthode createWidgets
        self.config(bg = "#87CEEB") # Configuration de la couleur de fond
        self.pack(fill=BOTH, expand=True) # Configuration de l'agencement des widgets

    # Méthode pour créer les widgets
    def createWidgets(self):
        # Création du label d'explication
        explicationLabel = tk.Label(self, text="Nous allons vous donner un verbe irrégulier \nVous allez devoir le conjuger a l'infinitif, au prétérit et au passé-composé\n \n Bonne chance ! ", font=("Helvetica", 15), bg= "#87CEEB" ) 
        explicationLabel.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW, pady=30, padx=85) 

        # Création du bouton pour démarrer le jeu
        demarrerBoutton = tk.Button(self, text = "Start", height=5, width=10, command=self.afficherPageJeu, font=("Helvetica", 10))
        demarrerBoutton.grid(row=9, column=1, columnspan=20,pady=55, ipadx=20)
        
        # Création du bouton pour quitter le jeu
        quitterBoutton = tk.Button(self, text= "Quitter", height=5, width=10, command=self.confirmationQuitter,font=("Helvetica", 10))
        quitterBoutton.grid(row=30, column=1, columnspan=30,pady=15,ipadx=20)

    # Méthode pour afficher la page du jeu
    def afficherPageJeu(self):
        self.pack_forget() # Suppression de la page d'accueil
        self.page_jeu = PageJeu(self.master) # Création de la page du jeu
        self.page_jeu.pack() # Affichage de la page du jeu

    # Méthode pour confirmer la fermeture de l'application
    def confirmationQuitter(self):
        reponse = messagebox.askyesno('Quitter', 'Voulez-vous vraiment quitter ?') # Affichage d'une boîte de dialogue
        if reponse: # Si la réponse est oui
            self.master.quit() # Fermeture de l'application