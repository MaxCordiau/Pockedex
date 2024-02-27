import tkinter as tk
from tkinter import messagebox
import random

class PokedexApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pokédex")
        self.master.geometry("600x400")
        self.master.configure(bg="#440000")  # Couleur de fond foncée

        self.pokemon_types = ["Feu", "Eau", "Plante"]  # Types de Pokémon possibles

        # Couleurs pour les types de Pokémon
        self.type_colors = {"Feu": "#FFCC66", "Eau": "#66CCFF", "Plante": "#99FF99"}

        # Initialisation de la liste des Pokémon
        self.pokemon_list = []

        # Création des widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels et Entries pour ajouter un nouveau Pokémon
        lbl_name = tk.Label(self.master, text="Nom du Pokémon:", font=("Arial", 12), bg="#440000", fg="white")
        lbl_name.place(x=50, y=50)
        self.entry_name = tk.Entry(self.master, font=("Arial", 12))
        self.entry_name.place(x=50, y=80)

        lbl_type = tk.Label(self.master, text="Type du Pokémon:", font=("Arial", 12), bg="#440000", fg="white")
        lbl_type.place(x=50, y=120)
        self.entry_type = tk.Entry(self.master, font=("Arial", 12))
        self.entry_type.place(x=50, y=150)

        lbl_abilities = tk.Label(self.master, text="Capacités du Pokémon (séparées par des virgules):", font=("Arial", 12), bg="#440000", fg="white")
        lbl_abilities.place(x=50, y=190)
        self.entry_abilities = tk.Entry(self.master, font=("Arial", 12))
        self.entry_abilities.place(x=50, y=220)

        # Bouton pour ajouter un nouveau Pokémon
        btn_add_pokemon = tk.Button(self.master, text="Ajouter Pokémon", font=("Arial", 12), command=self.add_new_pokemon, bg="#FFD700")  # Or
        btn_add_pokemon.place(x=50, y=260)

        # Bouton pour supprimer un Pokémon
        btn_remove_pokemon = tk.Button(self.master, text="Supprimer Pokémon", font=("Arial", 12), command=self.remove_selected_pokemon, bg="#FF6347")  # Tomate
        btn_remove_pokemon.place(x=200, y=260)

        # Bouton pour combattre
        btn_fight = tk.Button(self.master, text="Combattre", font=("Arial", 12), command=self.start_combat, bg="#FFA07A")  # Saumon
        btn_fight.place(x=50, y=300)

        # Bouton pour créer un Pokémon aléatoire
        btn_random_pokemon = tk.Button(self.master, text="Créer Pokémon aléatoire", font=("Arial", 12), command=self.create_random_pokemon, bg="#20B2AA")  # Bleu vert
        btn_random_pokemon.place(x=50, y=340)

        # Liste des Pokémon
        self.listbox_pokemon = tk.Listbox(self.master, font=("Arial", 12), width=25)
        self.listbox_pokemon.place(x=300, y=50)

        btn_display_stats = tk.Button(self.master, text="Afficher les statistiques", font=("Arial", 12), command=self.display_stats, bg="#98FB98")  # Vert clair
        btn_display_stats.place(x=50, y=380)
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

    def remove_selected_pokemon(self):
        # Récupérer l'index du Pokémon sélectionné
        index = self.listbox_pokemon.curselection()
        if index:
            index = int(index[0])
            # Supprimer le Pokémon de la liste et de la Listbox
            del self.pokemon_list[index]
            self.listbox_pokemon.delete(index)
            # Sauvegarder les données après la suppression
            self.save_data()
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un Pokémon à supprimer.")

    def display_stats(self):
        selected_index = self.listbox_pokemon.curselection()
        if len(selected_index) != 1:
            messagebox.showerror("Erreur", "Veuillez sélectionner un Pokémon pour afficher ses statistiques.")
            return

        index = selected_index[0]
        pokemon = self.pokemon_list[index]
        messagebox.showinfo("Statistiques du Pokémon", f"Nom: {pokemon['nom']}\nType: {pokemon['type']}\nCapacités: {', '.join(pokemon['capacites'])}")

    def start_combat(self):
        selected_index = self.listbox_pokemon.curselection()
        if len(selected_index) != 1:
            messagebox.showerror("Erreur", "Veuillez sélectionner un Pokémon pour le combat.")
            return

        index = selected_index[0]
        player_pokemon = self.pokemon_list[index]

        # L'ordinateur choisit un Pokémon aléatoire
        computer_pokemon = random.choice(self.pokemon_list)

        # Affichage des Pokémon choisis
        messagebox.showinfo("Combat", f"Votre Pokémon: {player_pokemon['nom']}\nPokémon de l'ordinateur: {computer_pokemon['nom']}")

        # Processus de combat
        player_hp = 100
        computer_hp = 100

        while player_hp > 0 and computer_hp > 0:
            # Attaque du joueur
            player_attack = random.choice(player_pokemon['capacites'])
            player_damage = random.randint(10, 30)
            computer_hp -= player_damage
            messagebox.showinfo("Combat", f"Votre Pokémon lance {player_attack} et inflige {player_damage} dégâts!")
            messagebox.showinfo("Combat", f"Points de vie restants de l'ordinateur: {computer_hp}")

            # Attaque de l'ordinateur
            computer_attack = random.choice(computer_pokemon['capacites'])
            computer_damage = random.randint(10, 30)
            player_hp -= computer_damage
            messagebox.showinfo("Combat", f"Le Pokémon de l'ordinateur lance {computer_attack} et inflige {computer_damage} dégâts!")
            messagebox.showinfo("Combat", f"Vos points de vie restants: {player_hp}")

        # Détermination du gagnant
        if player_hp <= 0:
            messagebox.showinfo("Combat", "Votre Pokémon a été vaincu. L'ordinateur gagne!")
        elif computer_hp <= 0:
            messagebox.showinfo("Combat", "Le Pokémon de l'ordinateur a été vaincu. Vous gagnez!")
        else:
            messagebox.showinfo("Combat", "Le combat se termine par une égalité!")

    def create_random_pokemon(self):
        # Générer un Pokémon aléatoire
        random_name = random.choice(["Bulbizarre", "Salamèche", "Carapuce", "Pikachu", "Rondoudou", "Mewtwo", "Dracaufeu", "Tortank", "Herbizarre", "Magicarpe"])
        random_type = random.choice(self.pokemon_types)
        random_abilities = random.sample(["Charge", "Vive-Attaque", "Lance-Flammes", "Hydrocanon", "Éclair", "Amnésie", "Soin", "Trempette", "Fouet Lianes", "Danse-Fleur"], random.randint(1, 3))

        # Ajouter le Pokémon à la liste et à la listebox
        self.pokemon_list.append({"nom": random_name, "type": random_type, "capacites": random_abilities})
        self.listbox_pokemon.insert(tk.END, random_name)
        self.listbox_pokemon.itemconfig(tk.END, bg=self.type_colors.get(random_type, "white"))

        # Sauvegarder les données après l'ajout
        self.save_data()

def main():
    root = tk.Tk()
    app = PokedexApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
