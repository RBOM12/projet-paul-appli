import tkinter as tk
from tkinter import Toplevel, ttk

from calculations import valeurxs, xs, valeurpdf
from gestion_pdf import lien_pdf



def create_oeil_form_deroul(container, oeil_label):
    """
    Crée un formulaire pour un œil avec des menus déroulants.

    Args:
        container: Le conteneur parent du formulaire.
        oeil_label: Le label de l'œil (gauche ou droit).

    Returns:
        Un dictionnaire contenant les valeurs sélectionnées pour l'œil.
    """

    # Frame principale du formulaire
    frame = ttk.Frame(container)
    frame.pack(fill="both", expand=True)

    # Label pour le type d'œil
    label = ttk.Label(frame, text=f"Formulaire Oeil {oeil_label}", font=('Arial', 14, 'bold'))
    label.pack(pady=10)

    # Liste des champs du formulaire avec leurs intitulés
    criteria = {
        "PSC": "PSC:",
        "Tonus": "Tonus:",
        "HPL": "Hauteur du prisme de larme:",
        "GL": "Grade lipide:",
        "CL": "Charge lacrymale:"
    }

    option_values_gl_cl = ["faible", "standard", "élevée"]
    option_values_hpl = ["0.2 <" ,"0.2 < X < 0.4" ," 0.40 <"]
    option_values_psc = ["lent", "standard", "rapide"]


    # Stockage des valeurs sélectionnées
    selected_values = {}

    # Création des labels et menus déroulants
    for key, label_text in criteria.items():
        ttk.Label(frame, text=label_text).pack(anchor="w")
        if label_text == "PSC:":
            selected_values[key] = tk.StringVar(value=option_values_psc[1])  # Valeur par défaut: "normal"
            combo = ttk.Combobox(frame, textvariable=selected_values[key], values=option_values_psc, state="readonly")
            combo.pack(fill="x", padx=10, pady=5)
        elif label_text == "Tonus:" or label_text == "Grade lipide:" or label_text == "Charge lacrymale:":
            selected_values[key] = tk.StringVar(value=option_values_gl_cl[1])
            combo = ttk.Combobox(frame, textvariable=selected_values[key], values=option_values_gl_cl, state="readonly")
            combo.pack(fill="x", padx=10, pady=5)
        else:
            selected_values[key] = tk.StringVar(value=option_values_hpl[1])
            combo = ttk.Combobox(frame, textvariable=selected_values[key], values=option_values_hpl, state="readonly")
            combo.pack(fill="x", padx=10, pady=5)




    return selected_values



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
    print("entries",entries)
    return entries
infocomp=""
#créer une nouvelle page pour afficher le résultat
def afficher_resultat(root):
    result_window = tk.Toplevel(root)
    result_window.title("Résultats")
    result_window.geometry("400x300")
    global infocomp




    # Collect data for PDF
    datag = {
        "xs gauche": valeurxs(0),
        "xs droit": valeurxs(1),
    }
    datad = {
        "xs gauche": valeurxs(0),
        "xs droit": valeurxs(1),
    }


    # Display results in the window
    ttk.Label(result_window, text="Résultats", font=('Arial', 14, 'bold')).pack(pady=10)
    ttk.Label(result_window, text=f"xs gauche: {valeurxs(0)}").pack(pady=5)
    ttk.Label(result_window, text=f"xs droit: {valeurxs(1)}").pack(pady=5)

    entry= ttk.Entry(result_window)
    entry.insert(0,"")
    entry.pack(pady=5)
    infocomp= entry

    # Boutons dans la fenêtre de résultats
    result_button = ttk.Button(result_window, text="Fermer", command=result_window.destroy)
    result_button.pack(side=tk.BOTTOM, padx=20, pady=10)


    # Bouton pour enregistrer en PDF
    pdf_button = ttk.Button(result_window, text="Enregistrer en PDF", command=lambda: valeurpdf(infocomp))
    pdf_button.pack(side=tk.BOTTOM, padx=20, pady=10)





