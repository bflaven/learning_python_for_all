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
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/000_jupyter_notebooks/stage_fmm_maksim/002_stage_cat_cat_maksim_tomic_day_to_day_2

# lancer le programme
streamlit run 005_maksim_nba_streamlit.py




"""

import streamlit as st

# Configuration de la page
st.set_page_config(page_title="NBA Player Selector", page_icon="🏀")

# Dictionnaire des joueurs avec leurs informations
players = {
    "Lebron James": {"country": "USA", "team": "Lakers", "image": "https://cdn.nba.com/headshots/nba/latest/1040x760/2544.png"},
    "Rudy Gobert": {"country": "France", "team": "Timberwolves", "image": "https://cdn.nba.com/headshots/nba/latest/1040x760/203497.png"},
    "Nikola Jokic": {"country": "Serbie", "team": "Denver", "image": "https://cdn.nba.com/headshots/nba/latest/1040x760/203999.png"},
    "Giannis Antetokounmpo": {"country": "Grèce", "team": "Bucks", "image": "https://cdn.nba.com/headshots/nba/latest/1040x760/203507.png"},
    "Denis Schröder": {"country": "Allemagne", "team": "Pistons", "image": "https://cdn.nba.com/headshots/nba/latest/1040x760/203471.png"}
}

# Titre de l'application
st.title("🏀 NBA Player Selector")

# Sélecteur de joueur
selected_player = st.selectbox("Sélectionnez un joueur :", list(players.keys()))

# Affichage des informations
if selected_player:
    player_info = players[selected_player]
    st.write(f"**Nationalité :** {player_info['country']}")
    st.write(f"**Équipe actuelle :** {player_info['team']}")
    st.image(player_info["image"], width=300)


