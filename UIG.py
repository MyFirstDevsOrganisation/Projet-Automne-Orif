from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()
fenetre.title("Révision des verbes en Anglais")


fenetre.maxsize(800,600)
fenetre.minsize(400,400)

fenetre.config(bg = "#87CEEB")
def callback():
    if askyesno('Titre 1', 'Etes-vous sûr de vouloir quitter ?'):
        fenetre.quit
    else:
        return
demarrer = Button (fenetre, text = "Start")
demarrer.pack()
quitter = Button(fenetre, text='Quitter', command=callable)
quitter.pack()



fenetre.mainloop()
