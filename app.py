# app.py
import streamlit as st
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

st.title("Générateur d'Histoires Personnalisées")

st.write("Entrez quelques détails et laissez l'IA créer une histoire personnalisée pour vous.")

# Entrées utilisateur pour l'histoire
character_name = st.text_input("Nom du personnage principal :", "Alice")
setting = st.text_input("Lieu de l'histoire :", "dans une forêt enchantée")
genre = st.selectbox("Genre de l'histoire :", ["Aventure", "Mystère", "Fantaisie", "Horreur", "Comédie"])
prompt = st.text_area("Début de l'histoire :", "Un jour, Alice se promenait...")

if st.button("Générer l'histoire"):
    # Appel à la nouvelle API OpenAI pour générer l'histoire
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Utiliser un modèle compatible
            messages=[
                {"role": "system", "content": "Tu es un narrateur d'histoires."},
                {"role": "user", "content": f"{prompt} {character_name} {setting} {genre}"}
            ],
            max_tokens=150,
            temperature=0.7
        )
        story = response['choices'][0]['message']['content']
        st.write(f"Voici votre histoire :\n\n{story}")

    except Exception as e:
        st.error(f"Erreur lors de la génération de l'histoire : {str(e)}")
