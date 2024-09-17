# Générateur d'Histoires Personnalisées

Ce projet est une application qui génère des histoires personnalisées basées sur les préférences et les entrées de l'utilisateur. L'application utilise l'API OpenAI pour créer des histoires uniques à partir des invites fournies par l'utilisateur.

## Description

L'application permet aux utilisateurs d'entrer des détails tels que le nom du personnage principal, le lieu de l'histoire, le genre, et le début de l'histoire. Elle utilise ensuite un modèle de langage d'OpenAI pour générer la suite de l'histoire.

## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/TatianaT13/generateur-histoires.git
   cd generateur-histoires
   ```
   Créer un environnement virtuel et activer-le :

```
python -m venv env
source env/bin/activate  # Sur Windows: env\Scripts\activate
````

Installer les dépendances :

```
pip install -r requirements.txt
````

Configurer l'API OpenAI :

Obtenez une clé API sur OpenAI .

Crée un fichier config.pyet ajoute ta clé API :
# config.py
OPENAI_API_KEY = 'ta_clé_api_ici'

# Utilisation
Pour lancer l'application, exécutez la commande suivante :

```
streamlit run app.py
````

Cela ouvrira l'application dans votre navigateur. Entre les détails pour ton histoire et clique sur "Générer l'histoire" pour voir le résultat.