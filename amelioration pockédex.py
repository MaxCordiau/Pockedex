import tkinter as tk
from tkinter import messagebox
import random

class PokedexApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pokédex")
        self.master.geometry("600x400")
        self.pokemon_types = ["Feu", "Eau", "Plante"]  # Types de Pokémon possibles

        # Couleurs pour les types de Pokémon
        self.type_colors = {"Feu": "#FF5733", "Eau": "#3399FF", "Plante": "#33CC33"}

        # Initialisation de la liste des Pokémon
        self.pokemon_list = []

        # Création des widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels et Entries pour ajouter un nouveau Pokémon
        lbl_name = tk.Label(self.master, text="Nom du Pokémon:", font=("Arial", 12))
        lbl_name.place(x=50, y=50)
        self.entry_name = tk.Entry(self.master, font=("Arial", 12))
        self.entry_name.place(x=50, y=80)

        lbl_type = tk.Label(self.master, text="Type du Pokémon:", font=("Arial", 12))
        lbl_type.place(x=50, y=120)
        self.entry_type = tk.Entry(self.master, font=("Arial", 12))
        self.entry_type.place(x=50, y=150)

        lbl_abilities = tk.Label(self.master, text="Capacités du Pokémon (séparées par des virgules):", font=("Arial", 12))
        lbl_abilities.place(x=50, y=190)
        self.entry_abilities = tk.Entry(self.master, font=("Arial", 12))
        self.entry_abilities.place(x=50, y=220)

        # Bouton pour ajouter un nouveau Pokémon
        btn_add_pokemon = tk.Button(self.master, text="Ajouter Pokémon", font=("Arial", 12), command=self.add_new_pokemon)
        btn_add_pokemon.place(x=50, y=260)

        # Bouton pour combattre
        btn_fight = tk.Button(self.master, text="Combattre", font=("Arial", 12), command=self.start_combat)
        btn_fight.place(x=50, y=300)

        # Liste des Pokémon
        self.listbox_pokemon = tk.Listbox(self.master, font=("Arial", 12), width=25)
        self.listbox_pokemon.place(x=300, y=50)

        # Chargement des données depuis le fichier
        self.load_data()

    def load_data(self):
        try:
            with open("pokemon.txt", "r") as file:
                for line in file:
                    if line.strip():
                        try:
                            nom, type_, capacites = line.strip().split(",", 2)
                            self.pokemon_list.append({"nom": nom, "type": type_, "capacites": capacites.split(",")})
                            self.listbox_pokemon.insert(tk.END, nom)
                            self.listbox_pokemon.itemconfig(tk.END, bg=self.type_colors.get(type_, "white"))
                        except ValueError:
                            messagebox.showwarning("Format de ligne incorrect", f"Ignorer la ligne mal formatée : {line.strip()}")
        except FileNotFoundError:
            messagebox.showwarning("Fichier introuvable", "Le fichier de sauvegarde 'pokemon.txt' n'existe pas.")

    def save_data(self):
        with open("pokemon.txt", "w") as file:
            for pokemon in self.pokemon_list:
                line = ",".join([pokemon["nom"], pokemon["type"], ",".join(pokemon["capacites"])]) + "\n"
                file.write(line)

    def add_new_pokemon(self):
        nom = self.entry_name.get()
        type_ = self.entry_type.get()
        capacites = self.entry_abilities.get().split(",")
        new_pokemon = {"nom": nom, "type": type_, "capacites": capacites}
        self.pokemon_list.append(new_pokemon)
        self.listbox_pokemon.insert(tk.END, nom)
        self.listbox_pokemon.itemconfig(tk.END, bg=self.type_colors.get(type_, "white"))

        # Sauvegarder les données après l'ajout
        self.save_data()

    def start_combat(self):
        if len(self.listbox_pokemon.curselection()) != 2:
            messagebox.showerror("Erreur", "Veuillez sélectionner exactement deux Pokémon pour le combat.")
            return

        index1, index2 = self.listbox_pokemon.curselection()
        pokemon1 = self.pokemon_list[index1]
        pokemon2 = self.pokemon_list[index2]

        winner = self.determine_winner(pokemon1, pokemon2)
        if winner is None:
            messagebox.showinfo("Résultat", "Match nul ! Les deux Pokémon ont des types et des capacités équivalentes.")
        else:
            messagebox.showinfo("Résultat", f"Le Pokémon gagnant est {winner['nom']} de type {winner['type']} !")

    def determine_winner(self, pokemon1, pokemon2):
        type1 = pokemon1["type"]
        type2 = pokemon2["type"]

        # Définissez les forces et les faiblesses de chaque type de Pokémon
        type_strengths = {"Feu": "Plante", "Eau": "Feu", "Plante": "Eau"}

        # Vérifiez les forces et les faiblesses pour déterminer le gagnant
        if type1 == type2:
            return None  # Match nul
        elif type2 in type_strengths.get(type1, []):
            return pokemon1
        else:
            return pokemon2

def main():
    root = tk.Tk()
    app = PokedexApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

