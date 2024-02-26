import tkinter as tk
from tkinter import messagebox
from tkinter import Listbox
from tkinter import ttk
from tkinter import Button
import pickle

fenetre = tk.Tk()
fenetre.title("Pokédex")
fenetre.geometry("1080x1920")


# nom
nom = tk.Label(fenetre, text="Nom")
nom.pack()
nom_entry = tk.Entry(fenetre)
nom_entry.pack()
# type
type = tk.Label(fenetre, text="type")
type.pack()
type_entry = tk.Entry(fenetre)
type_entry.pack()
# attaque
attaque = tk.Label(fenetre, text="attaque")
attaque.pack()
attaque_entry = tk.Entry(fenetre)
attaque_entry.pack()
# force
force = tk.Label(fenetre, text="force")
force.pack()
force_entry = tk.Entry(fenetre)
force_entry.pack()
# faiblesses
faiblesses = tk.Label(fenetre, text="faiblesses")
faiblesses.pack()
faiblesses_entry = tk.Entry(fenetre)
faiblesses_entry.pack()



class Pokemon_builder:
    def __init__(self, nom, vie, attaque):
        self.nom = nom
        self.vie = vie
        self.attaque = attaque

    def pokemeon_entry(self, nom, type, attaque, force, faiblesses):
        self.nom = nom_entry.get()
        self.type= type_entry.get()
        self.attaque= attaque_entry.get()
        self.force= force_entry.get()
        self.faiblesses= faiblesses_entry.get()
    
    def sauvegarder_pokemon():
        pokemon = dict(
            nom=nom_entry.get(),
            type=type_entry.get(),
            attaque=attaque_entry.get(),
            force=force_entry.get(),
            faiblesses=faiblesses_entry.get()
        )
    def sauvegarder():
        with open("pokemon.txt", "wb") as fichier:
            pickle.dump(liste_pokemon, fichier)
            messagebox.showinfo("Sauvegarde", "Le pokémon à était sauvegardée")
    def charger():
        with open("pokemon.txt", "rb") as fichier:
            sav_pokemon = pickle.load(fichier)
            messagebox.showinfo("Chargement", "Le pokémon à était chargée")

        liste_pokemon.append(Pokemon_builder.pokemeon_entry)
        liste_pokemon.insert(tk.END, Pokemon_builder.pokemeon_entry)
        sauvegarder = tk.Button(text="Sauvegarder", command=Pokemon_builder.sauvegarder_pokemon)
        sauvegarder.pack()




    # def afficher():
    #     for pokemon in liste_pokemon:
    #         liste_pokemon.insert(tk.END, pokemon)
    #     liste_pokemon.pack()


boutton_ajouter = tk.Button(fenetre, text="Ajouter", command=Pokemon_builder.pokemeon_entry)
boutton_ajouter.pack()

boutton_sauvegarder = tk.Button(fenetre, text="Sauvegarder", command=Pokemon_builder.sauvegarder)
boutton_sauvegarder.pack()

boutton_charger = tk.Button(fenetre, text="Charger", command=Pokemon_builder.charger)
boutton_charger.pack()

# afficher la liste des pockemon
# boutton_afficher = tk.Button(fenetre, text="Afficher", command=Pokemon_builder.afficher)
# boutton_afficher.pack()
tk.Listbox(fenetre)

# liste
liste_pokemon = Listbox(fenetre)
# liste_pokemon.insert(1, "Python")
liste_pokemon.pack()

# liste_pokemon = [
#     dict(
#         nom= "Salameche",
#         type="Feu",
#         attaque="Flammeche",
#         force="Brasier",
#         faiblesses="Eau"
#     ),
#     dict(
#         nom=nom_entry.get(),
#         type=type_entry.get(),
#         attaque=attaque_entry.get(),
#         force=force_entry.get(),
#         faiblesses=faiblesses_entry.get()
#     ),
# ]



# with open('liste_pokemon.pickle.txt', 'wb') as f:
#     pickle.dump(liste_pokemon, f, pickle.HIGHEST_PROTOCOL)

# # afficher les pockemons


# liste = tk.Listbox(fenetre)

fenetre.mainloop()
