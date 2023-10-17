from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()
fenetre.title("Révision des verbes en Anglais")


fenetre.maxsize(800,600)
fenetre.minsize(400,400)


def quitter():
    reponse = askokcancel("quitter", "Etes-vous sûr de vouloir quitter ?")
    print(reponse)

    if reponse:
        fenetre.destroy()
demarrer = Button (fenetre, text = "Start", height=5, width=10)

demarrer.pack()
quitter = Button(fenetre, text='Quitter', command=quitter, height=5, width=10)

quitter.pack()

fenetre.mainloop()
