#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
[env]
# Environnement Conda
# créer un environnement du nom de python_debut_segal
conda create --name python_debut_segal python=3.9.13

# liste tous les environnements
conda info --envs

# active l'environnement 
source activate python_debut_segal

# désactive l'environnement
conda deactivate

conda create --name python_firt python=3.9.13


# si nécessaire pour supprimer
conda env remove -n [NAME_OF_THE_CONDA_ENVIRONMENT]
conda env remove -n python_debut_segal
conda env remove -n python_firt



# mettre à jour conda
conda update -n base -c valeurs par défaut conda

# pour exporter les exigences
pip freeze > requirements.txt

# à installer
pip install -r requirements.txt

conda install -c conda-forge matplotlib




# [chemin]
cd /[your-path]/[your-directory]/
cd /Users/macbookair/Documents/stage_fmm/


# lancer le script "arbre-1.py"
python arbre-1.py


"""


import matplotlib.pyplot as plt

# Définition de l'arbre
root = [1, 2, 3, 4, 5]

# Dessin de l'arbre
# fig = plt.gca()
fig = plt.figure() #Here is your error
ax = fig.add_subplot(111)
for i in root:
    ax.text(i, i, f"{i}", ha="center")
plt.axis("off")

# Exportation en JPEG
plt.savefig("arbre.jpeg", format="jpg")








