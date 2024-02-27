import tkinter as tk
from tkinter import messagebox
import random

class PokedexApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pokédex")
        self.master.geometry("750x680")
        self.master.configure(bg="#440000")  

        self.pokemon_types = ["Feu", "Eau", "Plante"]  
        self.type_colors = {"Feu": "#FFCC66", "Eau": "#66CCFF", "Plante": "#99FF99"}

        self.pokemon_list = []

        self.create_widgets()

    def create_widgets(self):
        lbl_name = tk.Label(self.master, text="Nom du Pokémon:", font=("Arial", 12), bg="#440000", fg="white")
        lbl_name.grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = tk.Entry(self.master, font=("Arial", 12))
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        lbl_type = tk.Label(self.master, text="Type du Pokémon:", font=("Arial", 12), bg="#440000", fg="white")
        lbl_type.grid(row=1, column=0, padx=10, pady=10)
        self.entry_type = tk.Entry(self.master, font=("Arial", 12))
        self.entry_type.grid(row=1, column=1, padx=10, pady=10)

        lbl_abilities = tk.Label(self.master, text="Capacités du Pokémon (séparées par des virgules):", font=("Arial", 12), bg="#440000", fg="white")
        lbl_abilities.grid(row=2, column=0, padx=10, pady=10)
        self.entry_abilities = tk.Entry(self.master, font=("Arial", 12))
        self.entry_abilities.grid(row=2, column=1, padx=10, pady=10)

        lbl_hp = tk.Label(self.master, text="Vie du Pokémon:", font=("Arial", 12), bg="#440000", fg="white")
        lbl_hp.grid(row=3, column=0, padx=10, pady=10)
        self.entry_hp = tk.Entry(self.master, font=("Arial", 12))
        self.entry_hp.grid(row=3, column=1, padx=10, pady=10)

        btn_add_pokemon = tk.Button(self.master, text="Ajouter Pokémon", font=("Arial", 12), command=self.add_new_pokemon, bg="#FFD700")
        btn_add_pokemon.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        btn_remove_pokemon = tk.Button(self.master, text="Supprimer Pokémon", font=("Arial", 12), command=self.remove_selected_pokemon, bg="#FF6347")
        btn_remove_pokemon.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        btn_fight = tk.Button(self.master, text="Combattre", font=("Arial", 12), command=self.start_combat, bg="#FFA07A")
        btn_fight.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        btn_random_pokemon = tk.Button(self.master, text="Créer Pokémon aléatoire", font=("Arial", 12), command=self.create_random_pokemon, bg="#20B2AA")
        btn_random_pokemon.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        btn_display_stats = tk.Button(self.master, text="Afficher les statistiques", font=("Arial", 12), command=self.display_stats, bg="#98FB98")
        btn_display_stats.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        self.listbox_pokemon = tk.Listbox(self.master, font=("Arial", 12), width=45)
        self.listbox_pokemon.grid(row=0, column=2, rowspan=9, padx=10, pady=10)

        self.load_data()

    def load_data(self):
        try:
            with open("pokemon.txt", "r") as file:
                for line in file:
                    if line.strip():
                        try:
                            nom, type_, capacites, hp, niveau = line.strip().split(",", 4)
                            self.pokemon_list.append({"nom": nom, "type": type_, "capacites": capacites.split(","), "hp": int(hp), "niveau": int(niveau)})
                            self.listbox_pokemon.insert(tk.END, f"{nom} (Niveau: {niveau}, HP: {hp})")
                            self.listbox_pokemon.itemconfig(tk.END, bg=self.type_colors.get(type_, "white"))
                        except ValueError:
                            messagebox.showwarning("Format de ligne incorrect", f"Ignorer la ligne mal formatée : {line.strip()}")
        except FileNotFoundError:
            messagebox.showwarning("Fichier introuvable", "Le fichier de sauvegarde 'pokemon.txt' n'existe pas.")

    def save_data(self):
        with open("pokemon.txt", "w") as file:
            for pokemon in self.pokemon_list:
                line = ",".join([pokemon["nom"], pokemon["type"], ",".join(pokemon["capacites"]), str(pokemon["hp"]), str(pokemon["niveau"])]) + "\n"
                file.write(line)

    def add_new_pokemon(self):
        nom = self.entry_name.get()
        type_ = self.entry_type.get()
        capacites = self.entry_abilities.get().split(",")
        hp = int(self.entry_hp.get())
        new_pokemon = {"nom": nom, "type": type_, "capacites": capacites, "hp": hp, "niveau": 1}
        self.pokemon_list.append(new_pokemon)
        self.listbox_pokemon.insert(tk.END, f"{nom} (Niveau: 1, HP: {hp})")
        self.listbox_pokemon.itemconfig(tk.END, bg=self.type_colors.get(type_, "white"))
        self.save_data()

    def remove_selected_pokemon(self):
        index = self.listbox_pokemon.curselection()
        if index:
            index = int(index[0])
            del self.pokemon_list[index]
            self.listbox_pokemon.delete(index)
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
        messagebox.showinfo("Statistiques du Pokémon", f"Nom: {pokemon['nom']}\nType: {pokemon['type']}\nCapacités: {', '.join(pokemon['capacites'])}\nNiveau: {pokemon['niveau']}\nVie: {pokemon['hp']}")

    def start_combat(self):
        selected_index = self.listbox_pokemon.curselection()
        if len(selected_index) != 1:
            messagebox.showerror("Erreur", "Veuillez sélectionner un Pokémon pour le combat.")
            return

        index = selected_index[0]
        player_pokemon = self.pokemon_list[index]

        computer_pokemon = random.choice([pokemon for pokemon in self.pokemon_list if pokemon != player_pokemon])

        messagebox.showinfo("Combat", f"Votre Pokémon: {player_pokemon['nom']} (Niveau: {player_pokemon['niveau']}, HP: {player_pokemon['hp']})\nPokémon de l'ordinateur: {computer_pokemon['nom']} (Niveau: {computer_pokemon['niveau']}, HP: {computer_pokemon['hp']})")

        player_hp = player_pokemon['hp']
        computer_hp = computer_pokemon['hp']

        while player_hp > 0 and computer_hp > 0:
            player_attack = self.choose_attack(player_pokemon)
            player_damage = random.randint(10, 30) + (player_pokemon['niveau'] * 5)
            computer_hp -= player_damage
            player_pokemon['hp'] = player_hp
            self.update_listbox_hp()
            messagebox.showinfo("Combat", f"Votre Pokémon lance {player_attack} et inflige {player_damage} dégâts!")
            messagebox.showinfo("Combat", f"Points de vie restants de l'ordinateur: {computer_hp}")

            computer_attack = random.choice(computer_pokemon['capacites'])
            computer_damage = random.randint(10, 30) + (computer_pokemon['niveau'] * 5)
            player_hp -= computer_damage
            computer_pokemon['hp'] = computer_hp
            self.update_listbox_hp()
            messagebox.showinfo("Combat", f"Le Pokémon de l'ordinateur lance {computer_attack} et inflige {computer_damage} dégâts!")
            messagebox.showinfo("Combat", f"Vos points de vie restants: {player_hp}")

        if player_hp <= 0:
            messagebox.showinfo("Combat", "Votre Pokémon a été vaincu. L'ordinateur gagne!")
            self.remove_pokemon(player_pokemon)
        elif computer_hp <= 0:
            messagebox.showinfo("Combat", "Le Pokémon de l'ordinateur a été vaincu. Vous gagnez!")
            self.remove_pokemon(computer_pokemon)
            player_pokemon['niveau'] += 1
            self.update_listbox_hp()
        else:
            messagebox.showinfo("Combat", "Le combat se termine par une égalité!")

    def choose_attack(self, pokemon):
        attack_options = pokemon['capacites']
        
        # Création d'une fenêtre de dialogue personnalisée
        attack_dialog = tk.Toplevel(self.master)
        attack_dialog.title("Attaque")
        
        # Ajout d'une étiquette pour indiquer les options d'attaque
        lbl_attack = tk.Label(attack_dialog, text=f"Quelle attaque voulez-vous utiliser ?\nOptions: {', '.join(attack_options)}", font=("Arial", 12))
        lbl_attack.pack(padx=10, pady=10)
        
        # Fonction de gestionnaire d'événements pour chaque attaque
        def attack_handler(attack):
            attack_dialog.destroy()  # Ferme la fenêtre de dialogue
            self.attack_choice = attack
        
        # Création d'un bouton pour chaque attaque
        for attack in attack_options:
            btn_attack = tk.Button(attack_dialog, text=attack, command=lambda a=attack: attack_handler(a), font=("Arial", 12))
            btn_attack.pack(padx=10, pady=5)
        
        
    def create_random_pokemon(self):
        random_name = random.choice(["Bulbizarre", "Salamèche", "Carapuce", "Pikachu", "Rondoudou", "Mewtwo", "Dracaufeu", "Tortank", "Herbizarre", "Magicarpe"])
        random_type = random.choice(self.pokemon_types)
        random_abilities = random.sample(["Charge", "Vive-Attaque", "Lance-Flammes", "Hydrocanon", "Éclair", "Amnésie", "Soin", "Trempette", "Fouet Lianes", "Danse-Fleur"], random.randint(1, 3))
        random_hp = random.randint(50, 150)

        self.pokemon_list.append({"nom": random_name, "type": random_type, "capacites": random_abilities, "hp": random_hp, "niveau": 1})
        self.listbox_pokemon.insert(tk.END, f"{random_name} (Niveau: 1, HP: {random_hp})")
        self.listbox_pokemon.itemconfig(tk.END, bg=self.type_colors.get(random_type, "white"))
        self.save_data()

    def update_listbox_hp(self):
        self.listbox_pokemon.delete(0, tk.END)
        for pokemon in self.pokemon_list:
            self.listbox_pokemon.insert(tk.END, f"{pokemon['nom']} (Niveau: {pokemon['niveau']}, HP: {pokemon['hp']})")
            self.listbox_pokemon.itemconfig(tk.END, bg=self.type_colors.get(pokemon['type'], "white"))

    def remove_pokemon(self, pokemon):
        self.pokemon_list.remove(pokemon)
        self.update_listbox_hp()
        self.save_data()

def main():
    root = tk.Tk()
    app = PokedexApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()