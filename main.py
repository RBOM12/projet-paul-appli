import tkinter as tk
from tkinter import ttk

from calculations import submit_form
from ui import afficher_resultat

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Formulaires pour Oeil Gauche et Oeil Droit")
root.geometry("600x400")

def create_oeil_form(container, oeil_label):
    # Label pour le type d'oeil (gauche ou droit)
    label = ttk.Label(container, text=f"Formulaire Oeil {oeil_label}")
    label.grid(row=0, column=0, columnspan=2, pady=10)


    # Champs pour la puissance de l'oeil
    ttk.Label(container, text="XL:").grid(row=1, column=0, sticky=tk.W)
    xl_entry = ttk.Entry(container)
    xl_entry.grid(row=1, column=1)
    xl_entry.insert(0, "1")

    ttk.Label(container, text="YL:").grid(row=2, column=0, sticky=tk.W)
    yl_entry = ttk.Entry(container)
    yl_entry.grid(row=2, column=1)
    yl_entry.insert(0, "1")

    ttk.Label(container, text="ZL:").grid(row=3, column=0, sticky=tk.W)
    zl_entry = ttk.Entry(container)
    zl_entry.grid(row=3, column=1)
    zl_entry.insert(0, "1")

    # Champs pour le DHIV
    ttk.Label(container, text="DHIV:").grid(row=4, column=0, sticky=tk.W)
    dhiv_entry = ttk.Entry(container)
    dhiv_entry.grid(row=4, column=1)
    dhiv_entry.insert(0, "1")

    # Champs pour le diamètre de la pupille
    ttk.Label(container, text="Diamètre de la pupille:").grid(row=5, column=0, sticky=tk.W)
    diametre_entry = ttk.Entry(container)
    diametre_entry.grid(row=5, column=1)
    diametre_entry.insert(0, "1")

    # Champs pour le recouvrement
    ttk.Label(container, text="Recouvrement:").grid(row=6, column=0, sticky=tk.W)
    recouvrement_entry = ttk.Entry(container)
    recouvrement_entry.grid(row=6, column=1)
    recouvrement_entry.insert(0, "1")

    # Champs pour la kératométrie
    ttk.Label(container, text="K1:").grid(row=7, column=0, sticky=tk.W)
    k1_entry = ttk.Entry(container)
    k1_entry.grid(row=7, column=1)
    k1_entry.insert(0, "1")

    ttk.Label(container, text="X°:").grid(row=8, column=0, sticky=tk.W)
    x_entry = ttk.Entry(container)
    x_entry.grid(row=8, column=1)
    x_entry.insert(0, "1")

    ttk.Label(container, text="K2:").grid(row=9, column=0, sticky=tk.W)
    k2_entry = ttk.Entry(container)
    k2_entry.grid(row=9, column=1)
    k2_entry.insert(0, "1")

    ttk.Label(container, text="Y°:").grid(row=10, column=0, sticky=tk.W)
    y_entry = ttk.Entry(container)
    y_entry.grid(row=10, column=1)
    y_entry.insert(0, "1")


    ttk.Label(container, text="Excentricité").grid(row=11, column=0, sticky=tk.W)
    excentricite_entry = ttk.Entry(container)
    excentricite_entry.grid(row=11, column=1)
    excentricite_entry.insert(0, "1")


    return {
        "XL": xl_entry,
        "YL": yl_entry,
        "ZL": zl_entry,
        "DHIV": dhiv_entry,
        "diametre_pupille": diametre_entry,
        "recouvrement": recouvrement_entry,
        "K1": k1_entry,
        "X": x_entry,
        "K2": k2_entry,
        "Y": y_entry,
        "Excentricité": excentricite_entry,
    }

# Cadre pour l'oeil gauche
frame_gauche = ttk.Frame(root)
frame_gauche.grid(row=0, column=0, padx=25, pady=25)

# Cadre pour l'oeil droit
frame_droit = ttk.Frame(root)
frame_droit.grid(row=0, column=1, padx=25, pady=25)

# Créer les formulaires
form_gauche = create_oeil_form(frame_gauche, "Gauche")
form_droit = create_oeil_form(frame_droit, "Droit")

# Exemple d'utilisation avec le formulaire de l'œil gauche
submit_button = ttk.Button(frame_gauche, text="Soumettre", command=lambda: submit_form(form_gauche))
submit_button.grid(row=12, column=0, columnspan=2, pady=10)
# Exemple d'utilisation avec le formulaire de l'œil droit
submit_button = ttk.Button(frame_droit, text="Soumettre", command=lambda: submit_form(form_droit))
submit_button.grid(row=12, column=0, columnspan=2, pady=10)

frame_bas = ttk.Frame(root)
frame_bas.grid(row=1, column=0, columnspan=2)
submit_button = ttk.Button(frame_bas, text="Soumettre", command=lambda: afficher_resultat())
submit_button.grid(row=14, column=4, columnspan=2, pady=10)


# Démarrer l'application
root.mainloop()
