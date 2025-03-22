# 001_maksim_football_team_rating.py

#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
[env]
# Conda Environment
conda create --name nba_app python=3.9.13
conda info --envs
source activate nba_app
conda deactivate


# BURN AFTER READING
source activate nba_app

# if needed to remove
conda env remove -n [NAME_OF_THE_CONDA_ENVIRONMENT]
conda env remove -n nba_app

# install packages
python -m pip install streamlit 
python -m pip install streamlit

# chemin
cd /Users/brunoflaven/Documents/02_copy/stage_cat_cat_maksim_tomic/_stage_cat_cat_maksim_tomic_day_to_day_5

# lancer le programme
streamlit run 001_maksim_balkans_streamlit.py




"""

import streamlit as st
from PIL import Image, UnidentifiedImageError
import os

# Configuration de la page
st.set_page_config(page_title="Découvrez les Balkans", page_icon="🌍", layout="centered")

# Logo de l'application
logo_path = "path/to/your/logo.jpg"  # Remplacez par le chemin de votre logo
try:
    logo = Image.open(logo_path)
    st.image(logo, width=100)
except (FileNotFoundError, UnidentifiedImageError) as e:
    st.success('Il faut bien vérifier que les drapeaux existent dans le répertoire "flags" avec les noms corrects.')

# Titre de l'application
st.title("Découvrez les Balkans")

# Données des pays
countries = {
    "Serbie": {"capitale": "Belgrade", "population": "6,67 millions", "drapeau": "flags/serbia.jpg"},
    "Macédoine": {"capitale": "Skopje", "population": "2,08 millions", "drapeau": "flags/north_macedonia.jpg"},
    "Croatie": {"capitale": "Zagreb", "population": "4,06 millions", "drapeau": "flags/croatia.jpg"},
    "Grèce": {"capitale": "Athènes", "population": "10,42 millions", "drapeau": "flags/greece.jpg"},
    "Bosnie-Herzégovine": {"capitale": "Sarajevo", "population": "3,83 millions", "drapeau": "flags/bosnia_and_herzegovina.jpg"}
}

# Sélection du pays
selected_country = st.selectbox("Sélectionner un pays", options=["Sélectionner un pays"] + list(countries.keys()))

# Affichage des informations du pays sélectionné
if selected_country and selected_country != "Sélectionner un pays":
    country_info = countries[selected_country]
    st.write(f"**Capitale:** {country_info['capitale']}")
    st.write(f"**Population:** {country_info['population']}")

    # Chargement et affichage du drapeau
    try:
        flag_image = Image.open(country_info['drapeau'])
        st.image(flag_image, caption=f"Drapeau de {selected_country}", width=200)
    except (FileNotFoundError, UnidentifiedImageError) as e:
        st.error(f"Impossible de charger le drapeau de {selected_country}. Veuillez vérifier le chemin du fichier.")
else:
    st.write("Sélectionner un pays pour voir les informations.")



