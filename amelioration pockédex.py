import tkinter as tk
from tkinter import messagebox
import random

class PokedexApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pokédex")
        self.master.geometry("600x400")

        # Initialisation de la liste des Pokémon
        self.pokemon_list = []

        # Création des widgets
        self.create_widgets()

        # Charger les données depuis le fichier lors du démarrage de l'application
        self.load_data()

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

        # Bouton pour supprimer un Pokémon sélectionné
        btn_remove_pokemon = tk.Button(self.master, text="Supprimer Pokémon", font=("Arial", 12), command=self.remove_selected_pokemon)
        btn_remove_pokemon.place(x=50, y=300)

        # Bouton pour créer un Pokémon aléatoire
        btn_random_pokemon = tk.Button(self.master, text="Créer Pokémon aléatoire", font=("Arial", 12), command=self.create_random_pokemon)
        btn_random_pokemon.place(x=50, y=340)

        # Liste des Pokémon
        self.listbox_pokemon = tk.Listbox(self.master, font=("Arial", 12), width=25)
        self.listbox_pokemon.place(x=300, y=50)

        # Afficher les Pokémon dans la Listbox
        self.listbox_pokemon.bind("<<ListboxSelect>>", self.show_pokemon_info)

    def load_data(self):
        try:
            with open("pokemon.txt", "r") as file:
                for line in file:
                    # Ignorer les lignes vides ou mal formatées
                    if line.strip():
                        try:
                            nom, type_, capacites = line.strip().split(",", 2)
                            self.pokemon_list.append({"nom": nom, "type": type_, "capacites": capacites.split(",")})
                            self.listbox_pokemon.insert(tk.END, nom)
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

        # Sauvegarder les données après l'ajout
        self.save_data()

    def remove_selected_pokemon(self):
        index = self.listbox_pokemon.curselection()[0]
        self.listbox_pokemon.delete(index)
        del self.pokemon_list[index]

        # Sauvegarder les données après la suppression
        self.save_data()

    def create_random_pokemon(self):
        # Liste de noms, types et capacités possibles
        names = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle", "Jigglypuff", "Snorlax", "Gyarados", "Eevee", "Mewtwo", "Dragonite"]
        types_ = ["Feu", "Eau", "Plante", "Electrique", "Poison", "Vol", "Psy", "Insecte", "Roche", "Acier"]
        abilities = ["Charge", "Vive-Attaque", "Lance-Flammes", "Hydrocanon", "Tonnerre", "Tranch'Herbe", "Morsure", "Poing-Eclair", "Brouillard", "Bomb'Beurk"]

        # Générer un Pokémon aléatoire
        random_name = random.choice(names)
        random_type = random.choice(types_)
        random_abilities = random.sample(abilities, random.randint(1, 3))  # Choisir aléatoirement jusqu'à 3 capacités

        # Ajouter le Pokémon à la liste et à la listebox
        self.pokemon_list.append({"nom": random_name, "type": random_type, "capacites": random_abilities})
        self.listbox_pokemon.insert(tk.END, random_name)

        # Sauvegarder les données après l'ajout
        self.save_data()

    def show_pokemon_info(self, event):
        index = self.listbox_pokemon.curselection()[0]
        selected_pokemon = self.pokemon_list[index]
        messagebox.showinfo("Informations Pokémon", f"Nom: {selected_pokemon['nom']}\nType: {selected_pokemon['type']}\nCapacités: {', '.join(selected_pokemon['capacites'])}")

def main():
    root = tk.Tk()
    app = PokedexApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
