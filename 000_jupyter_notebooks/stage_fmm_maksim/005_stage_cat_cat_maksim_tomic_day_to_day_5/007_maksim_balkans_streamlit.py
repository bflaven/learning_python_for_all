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
streamlit run 007_maksim_balkans_streamlit.py




"""
import streamlit as st
import os

app_name = "Balkan Explorer"
logo = os.path.join("assets", "logo.png")
st.set_page_config(page_title=app_name, page_icon=logo)

countries = {
    "Serbie": {"capital": "Belgrade", "population": 7.06e+06, "flag": "flags/serbia.jpg"},
    "Macédoine": {"capital": "Skopje", "population": 2.11e+06, "flag": "flags/north_macedonia.jpg"},
    "Croatie": {"capital": "Zagreb", "population": 4.15e+06, "flag": "flags/croatia.jpg"},
    "Grèce": {"capital": "Athènes", "population": 10.76e+06, "flag": "flags/greece.jpg"},
    "Bosnie-Herzégovine": {"capital": "Sarajevo", "population": 3.58e+06, "flag": 
"flags/bosnia_and_herzegovina.jpg"}
}

def display_country(name):
    country = countries[name]
    st.write(f"Sélectionner un pays : {name}")
    st.write(" ")
    st.write(f"Capitale : {country['capital']}")
    st.write(f"Population : {country['population']}")
    st.image(country["flag"])

selected_country = st.selectbox("Sélectionner un pays", list(countries.keys()))
if selected_country:
    display_country(selected_country)






