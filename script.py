import yaml
import sys

# Fonction pour extraire les intents d'un fichier YAML
def extract_intents_from_file(file_path):
    try:
        # Charger le contenu YAML depuis le fichier
        with open(file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        intents = []
        
        # Vérifier si 'nlu' existe dans le YAML
        if data and 'nlu' in data:
            for item in data['nlu']:
                if 'intent' in item:
                    intents.append(item['intent'])
        return intents
    except yaml.YAMLError as e:
        print(f"Erreur lors du chargement du fichier {file_path} : {e}")
        return []
    except FileNotFoundError:
        print(f"Fichier {file_path} non trouvé.")
        return []

# Vérifier si des fichiers sont fournis en arguments
if len(sys.argv) < 2:
    print("Veuillez spécifier au moins un fichier YAML en argument.")
    print("Exemple : python extract_intents.py nlu1.yml nlu2.yml nlu3.yml")
    sys.exit(1)

# Extraire les intents de chaque fichier fourni
all_intents = []
for file_path in sys.argv[1:]:
    intents = extract_intents_from_file(file_path)
    all_intents.extend(intents)

# Supprimer les doublons (si applicable)
all_intents = list(set(all_intents))

# Afficher les intents
print("Liste des intents extraits :")
for intent in sorted(all_intents):  # Tri pour un affichage plus clair
    print(intent)

# Sauvegarder dans un fichier
with open("intents_extraits.txt", "w", encoding="utf-8") as f:
    for intent in sorted(all_intents):
        f.write(intent + "\n")
print("\nIntents sauvegardés dans 'intents_extraits.txt'")