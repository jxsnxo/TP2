import json
import csv

# Ouvrir le fichier .json en mode lecture
with open('data.json', 'r') as json_file:
    complexes = json.load(json_file)

# Ouvrir le fichier .csv en mode écriture
with open('complexes.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['reel', 'imaginaire'])

    # Ajout des nombres complexes dans le fichier .csv
    for num in complexes:
        csv_writer.writerow(num)