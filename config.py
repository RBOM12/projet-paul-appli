import tkinter as tk

# Créer la fenêtre principale
root = tk.Tk()
root.title("Grille modifiable")

# Définir les dimensions de la grille
rows, columns = 5, 5  # Par exemple, une grille 5x5

# Créer une liste pour stocker les références aux Entry
entries = []

# Préremplir la grille avec des Entry
for i in range(rows):
    row_entries = []  # Stocker les entrées de la ligne actuelle
    for j in range(columns):
        entry = tk.Entry(root, borderwidth=2, relief="solid", justify="center")
        entry.grid(row=i, column=j, padx=5, pady=5)
        entry.insert(0, f"R{i}C{j}")  # Préremplir avec du texte
        row_entries.append(entry)  # Ajouter l'Entry à la liste de la ligne
    entries.append(row_entries)  # Ajouter la ligne à la liste principale

# Fonction pour modifier une valeur dans la grille
def modify_entry(row, column, new_value):
    entries[row][column].delete(0, tk.END)  # Supprimer le texte existant
    entries[row][column].insert(0, new_value)  # Insérer la nouvelle valeur

# Exemple d'utilisation : modifier l'Entry à la position (2, 3)
modify_entry(2, 3, "Modifié!")

# Lancer la boucle principale
root.mainloop()