# Orif section informatique
# Exercice de groupe
# Projet Automne 
# Le programme est conçu pour réviser les verbes irréguliers en anglais sous forme de formulaire
#
# Auteurs : Dylan Diaz, Romain Howald, Loris Bayard, Grégoire Fischer, Nedeljko Mathieu (consultant/Observateur), Fabien Ducris (Contrôleur)
# Date   : 27.10.23

# import des librairies
import tkinter as tk
from tkinter import *
from Application import Application

if __name__ == "__main__": # Si le fichier est exécuté directement
   app = Application("Revision des verbes en Anglais", 800, 600, 400, 300) # Création de l'application
   app.mainloop() # Lancement de l'application
