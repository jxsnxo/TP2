import csv
import os

def lire_pokemon_stats(fichier_csv):
    # Vérifier si le fichier .csv existe
    if not os.path.isfile(fichier_csv):
        print(f"Le fichier {fichier_csv} n'existe pas.")
        return {}

    # Création du dictionnaire
    pokemon_stats = {}

    # Ouvrir le fichier .csv en mode lecture
    with open(fichier_csv, 'r', newline='') as csvfile:
        lire_csv = csv.reader(csvfile)

        for ligne in lire_csv:
            nom_pokemon = ligne[0]
            # Convertir stats en entiers
            stats = list(map(int, ligne[1:]))

            pokemon_stats[nom_pokemon] = stats

    return pokemon_stats

def charger_pokemon_csv(fichier_csv):
    return lire_pokemon_stats(fichier_csv)

fichier_csv = 'pokemon.csv'

# Test d'exécution
pkmn = charger_pokemon_csv(fichier_csv)

for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))
