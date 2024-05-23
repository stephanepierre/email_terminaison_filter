# Email Termination Filter

## Description

Ce projet traite un fichier CSV contenant des adresses email, des noms de sociétés et des URL de sites web. Il trie les adresses email par terminaison (par exemple, .fr, .com, .be) et crée des fichiers Excel et CSV distincts pour chaque terminaison d'email. Chaque fichier contient un maximum de 249 lignes de contacts. Les adresses email avec d'autres terminaisons sont regroupées dans des fichiers séparés.

## Prérequis

- Python 3.x
- Pandas
- Python-dotenv

## Installation des dépendances

1. Assurez-vous d'avoir Python installé sur votre machine.
2. Installez les dépendances nécessaires en utilisant `pip` :

    ```bash
    pip install pandas python-dotenv
    ```

## Configuration

1. Créez un fichier `.env` à la racine de votre projet.
2. Ajoutez le chemin d'accès à votre fichier CSV dans le fichier `.env` :

    ```env
    CSV_FILE_PATH=chemin/vers/votre/fichier.csv
    ```

## Utilisation

1. Placez votre fichier CSV à l'emplacement spécifié dans le fichier `.env`.
2. Exécutez le script `main.py` :

    ```bash
    python main.py
    ```

3. Les fichiers générés seront enregistrés dans le répertoire `email_terminations`.

## Exemple de structure de répertoire

email-termination-filter/  
│  
├── .env  
├── README.md  
├── main.py  
├── email_terminations/  
│ ├── emails_fr_1.xlsx  
│ ├── emails_fr_1.csv  
│ ├── emails_com_1.xlsx  
│ ├── emails_com_1.csv  
│ ├── emails_be_1.xlsx  
│ ├── emails_be_1.csv  
│ ├── emails_autres_1.xlsx  
│ ├── emails_autres_1.csv  
│ └── ... (autres fichiers générés)  
│  
└── requirements.txt  