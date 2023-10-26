# import des librairies
import tkinter as tk
from tkinter import *
from Application import Application

if __name__ == "__main__": # Si le fichier est exécuté directement
   app = Application("Revision des verbes en Anglais", 800, 600, 400, 300) # Création de l'application
   app.mainloop() # Lancement de l'application