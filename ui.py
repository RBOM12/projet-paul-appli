import tkinter as tk
from tkinter import ttk, messagebox
from database import insert_data
import csv

class LRPGApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LRPG Optical Calculations")

        self.create_widgets()

    def create_widgets(self):
        self.labels = ["DHIV", "Compensation", "K1", "K2", "Excentricité"]
        self.entries = {}

        for idx, label in enumerate(self.labels):
            tk.Label(self, text=label).grid(row=idx, column=0, padx=10, pady=10)
            entry = tk.Entry(self)
            entry.grid(row=idx, column=1, padx=10, pady=10)
            self.entries[label] = entry

        self.calc_button = tk.Button(self, text="Calculer", command=self.calculate)
        self.calc_button.grid(row=len(self.labels), column=0, columnspan=2, pady=20)

        self.affich_button = tk.Button(self, text="Afficher", command=self.trafficker)
        self.affich_button.grid(row=len(self.labels)+3, column=0, columnspan=4, pady=20)

        self.load_csv_button = tk.Button(self, text="Charger CSV", command=self.load_csv)
        self.load_csv_button.grid(row=len(self.labels) + 1, column=0, columnspan=2, pady=20)

        self.csv_frame = tk.Frame(self)
        self.csv_frame.grid(row=len(self.labels) + 2, column=0, columnspan=2, pady=20)

    def trafficker(self):
        try:
            DHIV = float(self.entries["DHIV"].get())
            Compensation = float(self.entries["Compensation"].get())
            K1 = float(self.entries["K1"].get())
            K2 = float(self.entries["K2"].get())
            Excentricité = float(self.entries["Excentricité"].get())

            DlA = calculate_DlA(DHIV, Compensation, K1, K2, Excentricité)
            DFLRGP = calculate_DFLRGP(DHIV, Compensation, K1, K2, Excentricité)
            R0 = calculate_R0(DHIV, Compensation, K1, K2, Excentricité)
            Flexibility = calculate_flexibility(DHIV, Compensation, K1, K2, Excentricité)

            result = f"DHIV: {DHIV}\nD'Compensation: {Compensation}\nK1: {K1}\nK2: {K2}\nExcentricité: {Excentricité}"
            messagebox.showinfo("Résultats", result)

            insert_data(DHIV, Compensation, K1, K2, Excentricité, DlA, DFLRGP, R0, Flexibility)

        except ValueError as e:
            messagebox.showerror("Erreur de saisie", "Veuillez entrer des valeurs numériques valides")

    def calculate(self):
        try:
            DHIV = float(self.entries["DHIV"].get())
            Compensation = float(self.entries["Compensation"].get())
            K1 = float(self.entries["K1"].get())
            K2 = float(self.entries["K2"].get())
            Excentricité = float(self.entries["Excentricité"].get())

            DlA = calculate_DlA(DHIV, Compensation, K1, K2, Excentricité)
            DFLRGP = calculate_DFLRGP(DHIV, Compensation, K1, K2, Excentricité)
            R0 = calculate_R0(DHIV, Compensation, K1, K2, Excentricité)
            Flexibility = calculate_flexibility(DHIV, Compensation, K1, K2, Excentricité)

            result = f"DlA: {DlA}\nD'FLRGP: {DFLRGP}\nR0: {R0}\nFlexibility: {Flexibility}"
            messagebox.showinfo("Résultats", result)

            insert_data(DHIV, Compensation, K1, K2, Excentricité, DlA, DFLRGP, R0, Flexibility)

        except ValueError as e:
            messagebox.showerror("Erreur de saisie", "Veuillez entrer des valeurs numériques valides")

    def load_csv(self):
        for widget in self.csv_frame.winfo_children():
            widget.destroy()

        try:
            with open('bddpaul.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                headers = reader.fieldnames

                for idx, header in enumerate(headers):
                    tk.Label(self.csv_frame, text=header).grid(row=0, column=idx, padx=10, pady=5)

                for row_idx, row in enumerate(reader):
                    for col_idx, header in enumerate(headers):
                        tk.Label(self.csv_frame, text=row[header]).grid(row=row_idx + 1, column=col_idx, padx=10, pady=5)

        except FileNotFoundError:
            messagebox.showerror("Erreur", "Fichier CSV non trouvé")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue lors de la lecture du CSV: {e}")

