import tkinter as tk
from tkinter import ttk
from calculations import submit_form, valeurxs  # Assurez-vous que ces modules existent
from gestion_pdf import lien_pdf  # Assurez-vous que ces modules existent

gauche = 0
droit = 1

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Formulaires pour Oeil Gauche et Oeil Droit")
root.state('zoomed')  # Ouvrir en plein écran

# Configuration du style
style = ttk.Style(root)
style.configure('TLabel', font=('Arial', 12), padding=5)
style.configure('TButton', font=('Arial', 12), padding=5)
style.configure('TEntry', font=('Arial', 12), padding=5)
style.configure('TCombobox', font=('Arial', 12))

# Fonction pour basculer vers la nouvelle page
def open_new_page():
    root.withdraw()  # Cacher la page principale
    new_page.deiconify()  # Montrer la nouvelle page

# Fonction pour revenir à la page principale
def return_to_main_page():
    new_page.withdraw()  # Cacher la nouvelle page
    root.deiconify()  # Montrer la page principale

# Création de la nouvelle page
new_page = tk.Toplevel(root)
new_page.title("Évaluation")
new_page.state('zoomed')  # Ouvrir en plein écran
new_page.withdraw()  # Cacher la nouvelle page au démarrage

# Cadre principal pour centrer le contenu sur la nouvelle page
center_frame = ttk.Frame(new_page)
center_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Configuration du redimensionnement dynamique
new_page.grid_columnconfigure(0, weight=1)
new_page.grid_rowconfigure(0, weight=1)
center_frame.grid_columnconfigure(0, weight=1)

# Liste des critères avec les menus déroulants
criteria = {
    "PSC": "PSC",
    "Tonus": "Tonus",
    "Hauteur du prisme de larme": "Hauteur du prisme de larme",
    "Grade lipide": "Grade lipide",
    "Grade charge lacrymale": "Grade charge lacrymale"
}

# Options pour les menus déroulants
options = ["un peu", "normal", "beaucoup"]
option_values = {"un peu": 0, "normal": 1, "beaucoup": 2}

# Stockage des valeurs sélectionnées
selected_values = {}

# Créer les labels et menus déroulants
for i, (key, label_text) in enumerate(criteria.items()):
    ttk.Label(center_frame, text=label_text).grid(row=i, column=0, padx=10, pady=10, sticky="e")
    selected_values[key] = tk.StringVar(value=options[1])  # Valeur par défaut: "normal"
    combo = ttk.Combobox(center_frame, textvariable=selected_values[key], values=options, state="readonly")
    combo.grid(row=i, column=1, padx=10, pady=10, sticky="w")

# Bouton pour revenir à la page principale
back_button = ttk.Button(center_frame, text="Retour", command=return_to_main_page)
back_button.grid(row=len(criteria), column=0, columnspan=2, pady=20)

# Cadre principal avec Canvas pour le défilement
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew")

canvas = tk.Canvas(main_frame)
canvas.grid(row=0, column=0, sticky="nsew")

# Configurer le redimensionnement dynamique pour les colonnes et les lignes
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

def create_oeil_form(container, oeil_label):
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.grid(row=1, column=0, sticky="nsew")
    scrollbar.grid(row=1, column=1, sticky="ns")

    # Label pour le type d'oeil (gauche ou droit)
    label = ttk.Label(scrollable_frame, text=f"Formulaire Oeil {oeil_label}", font=('Arial', 14, 'bold'))
    label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

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
        ttk.Label(scrollable_frame, text=label_text).grid(row=i, column=0, sticky=tk.W)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
        entry.insert(0, default_value)
        entries[label_text.strip(':')] = entry

    scrollable_frame.grid_columnconfigure(1, weight=1)

    return entries

# Cadre pour l'oeil gauche
frame_gauche = ttk.LabelFrame(main_frame, text="Oeil Gauche", padding=(20, 10))
frame_gauche.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Cadre pour l'oeil droit
frame_droit = ttk.LabelFrame(main_frame, text="Oeil Droit", padding=(20, 10))
frame_droit.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Configurer le redimensionnement dynamique pour les colonnes et les lignes dans le cadre défilant
frame_gauche.grid_columnconfigure(0, weight=1)
frame_gauche.grid_rowconfigure(1, weight=1)
frame_droit.grid_columnconfigure(0, weight=1)
frame_droit.grid_rowconfigure(1, weight=1)

# Créer les formulaires
form_gauche = create_oeil_form(frame_gauche, "Gauche")
form_droit = create_oeil_form(frame_droit, "Droit")

# Cadre en bas pour les boutons
frame_bas = ttk.Frame(root)
frame_bas.grid(row=1, column=0, pady=20, sticky="ew")
frame_bas.grid_columnconfigure(0, weight=1)

# Configurer le redimensionnement dynamique pour la ligne des boutons
root.grid_rowconfigure(1, weight=0)

# Bouton pour soumettre le formulaire
submit_button = ttk.Button(center_frame, text="Soumettre", command=lambda: submit_form_all())
submit_button.grid(row=len(criteria), column=1, columnspan=2, pady=20)

# Bouton pour afficher le résultat
result_button = ttk.Button(frame_bas, text="Afficher résultat", command=lambda: afficher_resultat())
result_button.grid(row=0, column=1, padx=10)

# Bouton pour ouvrir la nouvelle page depuis la page principale
open_button = ttk.Button(frame_bas, text="Évaluer les critères", command=open_new_page)
open_button.grid(row=0, column=2, padx=10)

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
    result_button.pack(side=tk.BOTTOM, padx=20, pady=10)

    pdf_button = ttk.Button(result_window, text="Enregistrer en PDF", command=lambda: lien_pdf(datag, datad))
    pdf_button.pack(side=tk.BOTTOM, padx=20, pady=10)

def submit_form_all():
    submit_form(form_gauche, gauche)
    submit_form(form_droit, droit)

# Démarrer l'application
root.mainloop()
