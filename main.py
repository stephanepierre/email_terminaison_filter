import pandas as pd
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Obtenir le chemin du fichier CSV depuis la variable d'environnement
csv_file_path = os.getenv('CSV_FILE_PATH')

if csv_file_path is None:
    raise ValueError("Le chemin du fichier CSV n'est pas défini dans le fichier .env")

# Lire le fichier CSV
df = pd.read_csv(csv_file_path)

# Extraire la terminaison d'email
df['email_ending'] = df['email'].apply(lambda x: x.split('.')[-1])

# Créer un répertoire pour stocker les fichiers Excel et CSV
output_dir = 'email_terminations'
os.makedirs(output_dir, exist_ok=True)

# Fonction pour diviser un DataFrame en morceaux de taille n
def split_dataframe(df, chunk_size):
    chunks = [df[i:i + chunk_size] for i in range(0, df.shape[0], chunk_size)]
    return chunks

# Terminaisons spécifiques
specific_endings = ['fr', 'be', 'com']
max_rows = 249

for ending in specific_endings:
    ending_df = df[df['email_ending'] == ending].copy()
    ending_df.drop(columns=['email_ending'], inplace=True)
    chunks = split_dataframe(ending_df, max_rows)
    for i, chunk in enumerate(chunks):
        # Enregistrer le DataFrame au format Excel
        excel_file_path = os.path.join(output_dir, f'emails_{ending}_{i+1}.xlsx')
        chunk.to_excel(excel_file_path, index=False)
        # Enregistrer le DataFrame au format CSV
        csv_file_path = os.path.join(output_dir, f'emails_{ending}_{i+1}.csv')
        chunk.to_csv(csv_file_path, index=False)

# Fichier pour les autres terminaisons
other_df = df[~df['email_ending'].isin(specific_endings)].copy()
if not other_df.empty:
    other_df.drop(columns=['email_ending'], inplace=True)
    chunks = split_dataframe(other_df, max_rows)
    for i, chunk in enumerate(chunks):
        # Enregistrer le DataFrame au format Excel
        other_excel_file_path = os.path.join(output_dir, f'emails_autres_{i+1}.xlsx')
        chunk.to_excel(other_excel_file_path, index=False)
        # Enregistrer le DataFrame au format CSV
        other_csv_file_path = os.path.join(output_dir, f'emails_autres_{i+1}.csv')
        chunk.to_csv(other_csv_file_path, index=False)
