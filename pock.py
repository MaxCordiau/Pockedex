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
attaque = tk.Label(fenetre, text="Attaque")
attaque.pack()
attaque_entry = tk.Entry(fenetre)
attaque_entry.pack()
# force
force = tk.Label(fenetre, text="Force")
force.pack()
force_entry = tk.Entry(fenetre)
force_entry.pack()
# faiblesses
faiblesses = tk.Label(fenetre, text="Faiblesses")
faiblesses.pack()
faiblesses_entry = tk.Entry(fenetre)
faiblesses_entry.pack()


class pokemon_builder:
    def pokemon_entry(self, nom, type, attaque, force, faiblesses):
        self.nom = nom_entry.get()
        self.type= type_entry.get()
        self.attaque= attaque_entry.get()
        self.force= force_entry.get()
        self.faiblesses= faiblesses_entry.get()
    
    # def sauvegarder_pokemon():
    #     pokemon = dict(
    #         nom= nom_entry.get(),
    #         type= type_entry.get(),
    #         attaque= attaque_entry.get(),
    #         force= force_entry.get(),
    #         faiblesses= faiblesses_entry.get()
    #     )
    def sauvegarder():
        with open("pokemon.txt", "ab") as fichier:
            pickle.dump(liste_pokemon, fichier)
            messagebox.showinfo("Sauvegarde", "Le pokémon à était sauvegardée")
    def charger():
        with open("pokemon.txt", "rb") as fichier:
            sav_pokemon = pickle.load(fichier)
            messagebox.showinfo("Chargement", "Le pokémon à était chargée")

        liste_pokemon.append(ajouter,tk.Listbox)
        liste_pokemon.insert(tk.END, ajouter,tk.Listbox)
        # liste_pokemon.append(Listbox)
        sauvegarder = tk.Button(text="Sauvegarder", command=sauvegarder)
        sauvegarder.pack()




    # def afficher():
    #     for pokemon in liste_pokemon:
    #         liste_pokemon.insert(tk.END, pokemon)
    #     liste_pokemon.pack()

ajouter = pokemon_builder.pokemon_entry
sauvegarder = pokemon_builder.sauvegarder
charger = pokemon_builder.charger

boutton_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter)
boutton_ajouter.pack()

boutton_sauvegarder = tk.Button(fenetre, text="Sauvegarder", command=sauvegarder)
boutton_sauvegarder.pack()

boutton_charger = tk.Button(fenetre, text="Charger", command=charger)
boutton_charger.pack()

# afficher la liste des pockemon
# boutton_afficher = tk.Button(fenetre, text="Afficher", command=pokemon_builder.afficher)
# boutton_afficher.pack()
# tk.Listbox(fenetre)

# # liste
# liste_pokemon = Listbox(fenetre)
# # liste_pokemon.insert(1, "Python")
# liste_pokemon.pack()

liste_pokemon = [
    dict(
        nom= "Salameche",
        type="Feu",
        attaque="Flammeche",
        force="Brasier",
        faiblesses="Eau"
    ),
    dict(
        nom=nom_entry.get(),
        type=type_entry.get(),
        attaque=attaque_entry.get(),
        force=force_entry.get(),
        faiblesses=faiblesses_entry.get()
    ),
]
tk.Listbox(fenetre)
liste_pokemon=tk.Listbox(fenetre)
liste_pokemon.pack()
# with open('liste_pokemon.pickle.txt', 'wb') as f:
#     pickle.dump(liste_pokemon, f, pickle.HIGHEST_PROTOCOL)



# def sav_entree():
#     entree = text_read.get("1.0", tk.END)
#     date_heure = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     dictionaire[date_heure] = entree
#     list_entree.insert(tk.END, text_read, date_heure)  # Ajouter la date et heure à la Listbox
#     messagebox.showinfo("Sauvegarder", "Le document à était sauvegardée")

# # ENTREE
# text_read = tk.Text(fenetre)
# text_read.grid(row=0, column=0, columnspan=1)

# def charg_entree():
#     pass

# # LISTE
# list_sav = tk.Listbox(fenetre)
# list_sav.insert(tk.END, "")
# list_sav.grid(row=0, column=1, rowspan=1,)# padx=10, pady=10)

# list_entree = tk.Listbox(fenetre, height=10, width=20)
# list_entree.grid(row=0, column=1, padx=10, pady=10)
# list_entree.bind("<<ListboxSelect>>", charg_entree)

# # DICTIONNAIRE
# dictionaire = {}

# # BOUTON
# bouton_sav = tk.Button(fenetre, text="Sauveguarder", command=sav_entree)
# bouton_sav.grid(row=1, column=0, padx=10, pady=5)

fenetre.mainloop()
