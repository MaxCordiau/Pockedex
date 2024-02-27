# import tkinter as tk
# from tkinter import messagebox

# class PokemonBuilder:
#     def __init__(self, fenetre):
#         self.fenetre = fenetre
#         self.liste_pokemon = []
#         self.create_widgets()

#     def create_widgets(self):
#         # Labels and Entry Widgets
#         labels = ["Nom", "Type", "Attaque", "Force", "Faiblesses"]
#         self.entries = {}
#         for label in labels:
#             lbl = tk.Label(self.fenetre, text=label)
#             lbl.pack()
#             entry = tk.Entry(self.fenetre)
#             entry.pack()
#             self.entries[label.lower()] = entry

#         # Buttons
#         btn_add = tk.Button(self.fenetre, text="Ajouter", command=self.ajouter_pokemon)
#         btn_add.pack()

#         btn_save = tk.Button(self.fenetre, text="Sauvegarder", command=self.sauvegarder)
#         btn_save.pack()

#         btn_load = tk.Button(self.fenetre, text="Charger", command=self.charger)
#         btn_load.pack()

#         # Pokemon List
#         self.listbox_pokemon = tk.Listbox(self.fenetre)
#         self.listbox_pokemon.pack()

#     def ajouter_pokemon(self):
#         pokemon = {}
#         for label, entry in self.entries.items():
#             pokemon[label.capitalize()] = entry.get()  # Capitalize keys
#             entry.delete(0, tk.END)  # Clearing entry after adding
#         self.liste_pokemon.append(pokemon)
#         self.update_listbox()

#     def update_listbox(self):
#         self.listbox_pokemon.delete(0, tk.END)
#         for pokemon in self.liste_pokemon:
#             self.listbox_pokemon.insert(tk.END, pokemon["Nom"])

#     def sauvegarder(self):
#         try:
#             with open("pokemon.txt", "w") as fichier:
#                 for pokemon in self.liste_pokemon:
#                     ligne = ",".join(pokemon.values()) + "\n"
#                     fichier.write(ligne)
#             messagebox.showinfo("Sauvegarde", "Les pokémons ont été sauvegardés dans 'pokemon.txt'")
#         except Exception as e:
#             messagebox.showerror("Erreur", f"Une erreur s'est produite lors de la sauvegarde : {e}")

    

#     def charger(self):
#         try:
#             with open("pokemon.txt", "r") as fichier:
#                 self.liste_pokemon = []
#                 for ligne in fichier:
#                     valeurs = ligne.strip().split(",")
#                     pokemon = {
#                         "Nom": valeurs[0],
#                         "Type": valeurs[1],
#                         "Attaque": valeurs[2],
#                         "Force": valeurs[3],
#                         "Faiblesses": valeurs[4]
#                     }
#                     self.liste_pokemon.append(pokemon)
#                 self.update_listbox()
#             messagebox.showinfo("Chargement", "Les pokémons ont été chargés depuis 'pokemon.txt'")
#         except FileNotFoundError:
#             messagebox.showwarning("Chargement", "Aucun fichier de sauvegarde trouvé")
#         except Exception as e:
#             messagebox.showerror("Erreur", f"Une erreur s'est produite lors du chargement : {e}")


# if __name__ == "__main__":
#     fenetre = tk.Tk()
#     fenetre.title("Pokédex")
#     fenetre.geometry("400x600")
#     app = PokemonBuilder(fenetre)
#     fenetre.mainloop()

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
