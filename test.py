import tkinter as tk
from tkinter import messagebox
import random

class PokedexApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pokédex")
        self.master.geometry("750x680")

        background_image_path = "C:/Users/marce/Desktop/LaPlateforme/Python/Tkinter/Projet/Pockedex/pokedex.png"


        # Charger l'image d'arrière-plan
        self.background_image = tk.PhotoImage(file=background_image_path)

        # Créer un canevas pour afficher l'image d'arrière-plan
        self.canvas = tk.Canvas(self.master, width=750, height=680)
        self.canvas.pack(side="top", fill="both", expand=True)

        # Ajouter l'image d'arrière-plan au canevas
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        self.master.configure(bg="#440000")  # Couleur de fond foncée

        self.pokemon_types = ["Feu", "Eau", "Plante"]  # Types de Pokémon possibles

        # Couleurs pour les types de Pokémon
        self.type_colors = {"Feu": "#FFCC66", "Eau": "#66CCFF", "Plante": "#99FF99"}

        # Initialisation de la liste des Pokémon
        self.pokemon_list = []

        # Création des widgets
        self.create_widgets()

    def create_widgets(self):
        # Frame pour les entrées de données
        frame_data = tk.Frame(self.canvas, width=300, height=500, bg="white")
        frame_data.place(x=50, y=50)

        # Labels et Entries pour ajouter un nouveau Pokémon
        lbl_name = tk.Label(frame_data, text="Nom du Pokémon:", font=("Arial", 12), bg="white", fg="black")
        lbl_name.place(x=10, y=10)
        self.entry_name = tk.Entry(frame_data, font=("Arial", 12))
        self.entry_name.place(x=10, y=40)

        lbl_type = tk.Label(frame_data, text="Type du Pokémon:", font=("Arial", 12), bg="white", fg="black")
        lbl_type.place(x=10, y=80)
        self.entry_type = tk.Entry(frame_data, font=("Arial", 12))
        self.entry_type.place(x=10, y=110)

        lbl_abilities = tk.Label(frame_data, text="Capacités du Pokémon (séparées par des virgules):", font=("Arial", 12), bg="white", fg="black")
        lbl_abilities.place(x=10, y=150)
        self.entry_abilities = tk.Entry(frame_data, font=("Arial", 12))
        self.entry_abilities.place(x=10, y=180)

        # Label et Entry pour la vie du Pokémon
        lbl_hp = tk.Label(frame_data, text="Vie du Pokémon:", font=("Arial", 12), bg="white", fg="black")
        lbl_hp.place(x=10, y=220)
        self.entry_hp = tk.Entry(frame_data, font=("Arial", 12))
        self.entry_hp.place(x=10, y=250)

        # Bouton pour ajouter un nouveau Pokémon
        btn_add_pokemon = tk.Button(frame_data, text="Ajouter Pokémon", font=("Arial", 12), command=self.add_new_pokemon, bg="#FFD700")  # Or
        btn_add_pokemon.place(x=10, y=290)

        # Bouton pour supprimer un Pokémon
        btn_remove_pokemon = tk.Button(frame_data, text="Supprimer Pokémon", font=("Arial", 12), command=self.remove_selected_pokemon, bg="#FF6347")  # Tomate
        btn_remove_pokemon.place(x=10, y=330)

        # Frame pour la liste des Pokémon
        frame_list = tk.Frame(self.canvas, width=300, height=300, bg="green")
        frame_list.place(x=370, y=50)

        # Liste des Pokémon
        self.listbox_pokemon = tk.Listbox(frame_list, font=("Arial", 12), width=25, height=15)
        self.listbox_pokemon.place(x=10, y=10)

        btn_display_stats = tk.Button(frame_list, text="Afficher les statistiques", font=("Arial", 12), command=self.display_stats, bg="#98FB98")  # Vert clair
        btn_display_stats.place(x=10, y=270)

        # Chargement des données depuis le fichier
        self.load_data()

    def load_data(self):
        try:
            with open("pokemon.txt", "r") as file:
                for line in file:
                    if line.strip():
                        try:
                            nom, type_, capacites, hp = line.strip().split(",", 3)
                            self.pokemon_list.append({"nom": nom, "type": type_, "capacites": capacites.split(","), "hp": int(hp)})
                            self.listbox_pokemon.insert(tk.END, nom + " (HP: " + str(hp) + ")")
                            self.listbox_pokemon.itemconfig(tk.END, bg=self.type_colors.get(type_, "white"))
                        except ValueError:
                            messagebox.showwarning("Format de ligne incorrect", f"Ignorer la ligne mal formatée : {line.strip()}")
        except FileNotFoundError:
            messagebox.showwarning("Fichier introuvable", "Le fichier de sauvegarde 'pokemon.txt' n'existe pas.")

    def save_data(self):
        with open("pokemon.txt", "w") as file:
            for pokemon in self.pokemon_list:
                line = ",".join([pokemon["nom"], pokemon["type"], ",".join(pokemon["capacites"]), str(pokemon["hp"])]) + "\n"
                file.write(line)

    def add_new_pokemon(self):
        nom = self.entry_name.get()
        type_ = self.entry_type.get()
        capacites = self.entry_abilities.get().split(",")
        hp = int(self.entry_hp.get())
        new_pokemon = {"nom": nom, "type": type_, "capacites": capacites, "hp": hp}
        self.pokemon_list.append(new_pokemon)
        self.listbox_pokemon.insert(tk.END, nom + " (HP: " + str(hp) + ")")
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
        messagebox.showinfo("Statistiques du Pokémon", f"Nom: {pokemon['nom']}\nType: {pokemon['type']}\nCapacités: {', '.join(pokemon['capacites'])}\nVie: {pokemon['hp']}")

    def start_combat(self):
        selected_index = self.listbox_pokemon.curselection()
        if len(selected_index) != 1:
            messagebox.showerror("Erreur", "Veuillez sélectionner un Pokémon pour le combat.")
            return

        index = selected_index[0]
        player_pokemon = self.pokemon_list[index]

        # Filtrer la liste des Pokémon disponibles pour l'ordinateur
        computer_pokemon = random.choice([pokemon for pokemon in self.pokemon_list if pokemon != player_pokemon])

        # Affichage des Pokémon choisis
        messagebox.showinfo("Combat", f"Votre Pokémon: {player_pokemon['nom']} (HP: {player_pokemon['hp']})\nPokémon de l'ordinateur: {computer_pokemon['nom']} (HP: {computer_pokemon['hp']})")

        # Processus de combat
        player_hp = player_pokemon['hp']
        computer_hp = computer_pokemon['hp']

        while player_hp > 0 and computer_hp > 0:
            # Attaque du joueur
            player_attack = random.choice(player_pokemon['capacites'])
            player_damage = random.randint(10, 30)
            computer_hp -= player_damage
            player_pokemon['hp'] = player_hp  # Mettre à jour la vie du joueur
            self.update_listbox_hp()  # Mettre à jour la liste des Pokémon avec la nouvelle vie
            messagebox.showinfo("Combat", f"Votre Pokémon lance {player_attack} et inflige {player_damage} dégâts!")
            messagebox.showinfo("Combat", f"Points de vie restants de l'ordinateur: {computer_hp}")

            # Attaque de l'ordinateur
            computer_attack = random.choice(computer_pokemon['capacites'])
            computer_damage = random.randint(10, 30)
            player_hp -= computer_damage
            computer_pokemon['hp'] = computer_hp  # Mettre à jour la vie de l'ordinateur
            self.update_listbox_hp()  # Mettre à jour la liste des Pokémon avec la nouvelle vie
            messagebox.showinfo("Combat", f"Le Pokémon de l'ordinateur lance {computer_attack} et inflige {computer_damage} dégâts!")
            messagebox.showinfo("Combat", f"Vos points de vie restants: {player_hp}")

        # Détermination du gagnant et suppression du perdant
        if player_hp <= 0:
            messagebox.showinfo("Combat", "Votre Pokémon a été vaincu. L'ordinateur gagne!")
            self.remove_pokemon(player_pokemon)
        elif computer_hp <= 0:
            messagebox.showinfo("Combat", "Le Pokémon de l'ordinateur a été vaincu. Vous gagnez!")
            self.remove_pokemon(computer_pokemon)
        else:
            messagebox.showinfo("Combat", "Le combat se termine par une égalité!")

    def create_random_pokemon(self):
        # Générer un Pokémon aléatoire
        random_name = random.choice(["Bulbizarre", "Salamèche", "Carapuce", "Pikachu", "Rondoudou", "Mewtwo", "Dracaufeu", "Tortank", "Herbizarre", "Magicarpe"])
        random_type = random.choice(self.pokemon_types)
        random_abilities = random.sample(["Charge", "Vive-Attaque", "Lance-Flammes", "Hydrocanon", "Éclair", "Amnésie", "Soin", "Trempette", "Fouet Lianes", "Danse-Fleur"], random.randint(1, 3))
        random_hp = random.randint(50, 150)

        # Ajouter le Pokémon à la liste et à la listebox
        self.pokemon_list.append({"nom": random_name, "type": random_type, "capacites": random_abilities, "hp": random_hp})
        self.listbox_pokemon.insert(tk.END, random_name + " (HP: " + str(random_hp) + ")")
        self.listbox_pokemon.itemconfig(tk.END, bg=self.type_colors.get(random_type, "white"))

        # Sauvegarder les données après l'ajout
        self.save_data()

    def update_listbox_hp(self):
        # Met à jour la liste des Pokémon avec leurs points de vie actuels
        self.listbox_pokemon.delete(0, tk.END)
        for pokemon in self.pokemon_list:
            self.listbox_pokemon.insert(tk.END, f"{pokemon['nom']} (HP: {pokemon['hp']})")
            self.listbox_pokemon.itemconfig(tk.END, bg=self.type_colors.get(pokemon['type'], "white"))

    def remove_pokemon(self, pokemon):
        # Supprime un Pokémon de la liste
        self.pokemon_list.remove(pokemon)
        self.update_listbox_hp()  # Met à jour la liste des Pokémon après la suppression
        self.save_data()  # Sauvegarde les données après la suppression

def main():
    root = tk.Tk()
    app = PokedexApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()