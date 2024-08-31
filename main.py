import tkinter as tk
from tkinter import ttk
from calculations import submit_form, submit_form_deroulant  # Assurez-vous que ces modules existent
from creation_interface import create_oeil_form_deroul, create_oeil_form, afficher_resultat

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


# Bouton pour revenir à la page principale
back_button = ttk.Button(center_frame, text="Retour", command=return_to_main_page)
back_button.grid(row=6, column=0, columnspan=2, pady=20)

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


# Cadre pour l'oeil gauche
frame_gauche = ttk.LabelFrame(main_frame, text="Oeil Gauche", padding=(20, 10))
frame_gauche.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
frame_droit = ttk.LabelFrame(main_frame, text="Oeil Droit", padding=(20, 10))
frame_droit.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Cadre pour l'oeil gauche avec défilement
frame_gauche_deroulant = ttk.LabelFrame(center_frame, text="Oeil Gauche", padding=(20, 10))
frame_gauche_deroulant.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
frame_droit_deroulant = ttk.LabelFrame(center_frame, text="Oeil Droit", padding=(20, 10))
frame_droit_deroulant.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")


# Configurer le redimensionnement dynamique pour les colonnes et les lignes dans le cadre défilant
frame_gauche.grid_columnconfigure(0, weight=1)
frame_gauche.grid_rowconfigure(1, weight=1)
frame_droit.grid_columnconfigure(0, weight=1)
frame_droit.grid_rowconfigure(1, weight=1)
frame_gauche_deroulant.grid_columnconfigure(0, weight=1)
frame_gauche_deroulant.grid_rowconfigure(1, weight=1)
frame_droit_deroulant.grid_columnconfigure(0, weight=1)
frame_droit_deroulant.grid_rowconfigure(1, weight=1)


# Créer les formulaires
form_gauche = create_oeil_form(frame_gauche, "Gauche")
form_droit = create_oeil_form(frame_droit, "Droit")
form_gauche_deroulant = create_oeil_form_deroul(frame_gauche_deroulant, "Gauche")
form_droit_deroulant = create_oeil_form_deroul(frame_droit_deroulant, "Droit")
# Cadre en bas pour les boutons
frame_bas = ttk.Frame(root)
frame_bas.grid(row=1, column=0, pady=20, sticky="ew")
frame_bas.grid_columnconfigure(0, weight=1)

# Configurer le redimensionnement dynamique pour la ligne des boutons
root.grid_rowconfigure(1, weight=0)

# Bouton pour soumettre le formulaire
submit_button = ttk.Button(center_frame, text="Soumettre", command=lambda: submit_form_all())
submit_button.grid(row=6, column=1, columnspan=2, pady=20)

# Bouton pour afficher le résultat
result_button = ttk.Button(center_frame, text="Afficher résultat", command=lambda: afficher_resultat(root))
result_button.grid(row=6, column=2, padx=10)

# Bouton pour ouvrir la nouvelle page depuis la page principale
open_button = ttk.Button(frame_bas, text="Évaluer les critères", command=open_new_page)
open_button.grid(row=0, column=2, padx=10)



def submit_form_all():
    submit_form_deroulant(form_gauche_deroulant, gauche)
    submit_form_deroulant(form_droit_deroulant, droit)
    submit_form(form_gauche, gauche)
    submit_form(form_droit, droit)

# Démarrer l'application
root.mainloop()
