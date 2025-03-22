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
streamlit run 002_maksim_balkans_streamlit.py




"""

import streamlit as st
import os

app_name = 'Flag Explorer'
logo = os.path.join('images', 'globe.png')  # Replace with the path to your logo image file
st.set_page_config(page_title=app_name, page_icon=logo)

countries = ['Serbie', 'Macédoine', 'Croatie', 'Grèce', 'Bosnie-Herzégovine']
flags_folder = 'flags'  # Replace with the path to your flags folder
selected_country = ''
country_info = {'Serbie': ('Србија', 'Belgrade', '7.03 million', os.path.join(flags_folder, 'serbia.jpg')),
                'Macédoine': ('Македонија', 'Skopje', '2.1 million', os.path.join(flags_folder, 
'north_macedonia.jpg')),
                'Croatie': ('Hrvatska', 'Zagreb', '4.26 million', os.path.join(flags_folder, 'croatia.jpg')),
                'Grèce': ('Ελλάδα', 'Athens', '10.5 million', os.path.join(flags_folder, 'greece.jpg')),
                'Bosnie-Herzégovine': ('Bosna i Hercegovina', 'Sarajevo', '3.5 million', os.path.join(flags_folder, 
'bosnia_and_herzegovina.jpg'))}


def display_country_info(country):
    name, capital, population, flag = country_info[country]
    st.title(name)
    st.subheader('Capitale : ' + capital)
    st.subheader('Population : ' + str(population))
    if flag:
        st.image(flag)

st.markdown('# ' + app_name)
selected_country = st.selectbox("Sélectionner un pays", countries, key='country')
if selected_country != '':
    display_country_info(selected_country)





