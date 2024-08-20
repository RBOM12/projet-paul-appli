from tkinter import *
from tkinter.messagebox import showinfo

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()
bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()


def recupere():
    showinfo("Alerte", entree.get())
def recupere1():
    showinfo("Alerte", entree1.get())

value = StringVar()
value.set("Valeur")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()
bouton1 = Button(fenetre, text="Valider", command=recupere)
bouton1.pack(side=RIGHT)

value2 = StringVar()
value2.set("rien")
entree1 = Entry(fenetre, textvariable=value2, width=30)
entree1.pack()

bouton = Button(fenetre, text="Valider", command=recupere1)
bouton.pack()
fenetre.mainloop()
# bouton de sortie
