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
streamlit run 003_maksim_balkans_streamlit.py




"""

import streamlit as st

# Informations des pays
countries_info = {
    "Serbie": {"capitale": "Belgrade", "population": "6,649,236", "drapeau": "🇷🇸"},
    "Macédoine": {"capitale": "Skopje", "population": "2,083,374", "drapeau": "🇲🇰"},
    "Croatie": {"capitale": "Zagreb", "population": "3,871,833", "drapeau": "🇭🇷"},
    "Grèce": {"capitale": "Athènes", "population": "10,423,454", "drapeau": "🇬🇷"},
    "Bosnie-Herzégovine": {"capitale": "Sarajevo", "population": "3,280,819", "drapeau": "🇧🇦"}
}

# Configuration de la page
st.set_page_config(page_title="Explorateur de Pays", page_icon="🌍")

# Titre de l'application avec logo
st.title("Explorateur de Pays 🌍")

# Menu déroulant pour sélectionner un pays
selected_country = st.selectbox("Sélectionner un pays", options=["Sélectionner un pays"] + list(countries_info.keys()))

# Afficher les informations du pays sélectionné
if selected_country in countries_info:
    country_info = countries_info[selected_country]
    st.write(f"**Pays:** {selected_country}")
    st.write(f"**Capitale:** {country_info['capitale']}")
    st.write(f"**Population:** {country_info['population']}")
    st.write(f"**Drapeau:** {country_info['drapeau']}")
else:
    st.write("Veuillez sélectionner un pays pour voir ses informations.")






