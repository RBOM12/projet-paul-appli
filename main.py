import tkinter as tk
from tkinter import ttk
from calculations import submit_form, valeurxs  # Assurez-vous que ces modules existent
from gestion_pdf import lien_pdf  # Assurez-vous que ces modules existent

gauche = 0
droit = 1

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Formulaires pour Oeil Gauche et Oeil Droit")
root.geometry("900x600")

# Configuration du style
style = ttk.Style(root)
style.configure('TLabel', font=('Arial', 12), padding=5)
style.configure('TButton', font=('Arial', 12), padding=5)
style.configure('TEntry', font=('Arial', 12), padding=5)

def create_oeil_form(container, oeil_label):
    # Label pour le type d'oeil (gauche ou droit)
    label = ttk.Label(container, text=f"Formulaire Oeil {oeil_label}", font=('Arial', 14, 'bold'))
    label.grid(row=0, column=0, columnspan=2, pady=10)

    # Liste des champs du formulaire
    fields = {
        "XL:": "1",
        "YL:": "1",
        "ZL:": "1",
        "DHIV:": "1",
        "Diamètre de la pupille:": "1",
        "Recouvrement:": "1",
        "K1:": "7.25",
        "X:": "1",
        "K2:": "6.95",
        "Y:": "1",
        "Excentricité:": "1"
    }

    entries = {}
    for i, (label_text, default_value) in enumerate(fields.items(), start=1):
        ttk.Label(container, text=label_text).grid(row=i, column=0, sticky=tk.W)
        entry = ttk.Entry(container)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, default_value)
        entries[label_text.strip(':')] = entry

    return entries

# Cadre pour l'oeil gauche
frame_gauche = ttk.LabelFrame(root, text="Oeil Gauche", padding=(20, 10))
frame_gauche.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Cadre pour l'oeil droit
frame_droit = ttk.LabelFrame(root, text="Oeil Droit", padding=(20, 10))
frame_droit.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Configurer le redimensionnement dynamique
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# Créer les formulaires
form_gauche = create_oeil_form(frame_gauche, "Gauche")
form_droit = create_oeil_form(frame_droit, "Droit")

# Cadre en bas pour les boutons
frame_bas = ttk.Frame(root)
frame_bas.grid(row=1, column=0, columnspan=2, pady=20)

# Bouton pour soumettre le formulaire
submit_button = ttk.Button(frame_bas, text="Soumettre", command=lambda: submit_form_all())
submit_button.grid(row=0, column=0, padx=10)

# Bouton pour afficher le résultat
result_button = ttk.Button(frame_bas, text="Afficher résultat", command=lambda: afficher_resultat())
result_button.grid(row=0, column=1, padx=10)

def afficher_resultat():
    result_window = tk.Toplevel(root)
    result_window.title("Résultats")
    result_window.geometry("400x300")

    # Collect data for PDF
    datag = {
        "xs gauche": valeurxs(),
        "xs droit": valeurxs(),
    }
    datad = {
        "xs gauche": valeurxs(),
        "xs droit": valeurxs(),
    }

    # Display results in the window
    ttk.Label(result_window, text="Résultats", font=('Arial', 14, 'bold')).pack(pady=10)
    ttk.Label(result_window, text=f"xs gauche: {valeurxs()}").pack(pady=5)
    ttk.Label(result_window, text=f"xs droit: {valeurxs()}").pack(pady=5)

    # Boutons dans la fenêtre de résultats
    result_button = ttk.Button(result_window, text="Fermer", command=result_window.destroy)
    result_button.pack(side=tk.LEFT, padx=20, pady=10)

    pdf_button = ttk.Button(result_window, text="Enregistrer en PDF", command=lambda: lien_pdf(datag, datad))
    pdf_button.pack(side=tk.RIGHT, padx=20, pady=10)

def submit_form_all():
    submit_form(form_gauche, gauche)
    submit_form(form_droit, droit)

# Démarrer l'application
root.mainloop()

