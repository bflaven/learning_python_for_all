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


# lancer le script "arbre-3.py"
python arbre-3.py


https://raw.githubusercontent.com/dojojon/py_turtle/master/tree.py

"""


from turtle import *
from random import randint

speed(0)

def draw_branch(len):
    
    if(len > 5):
        color("brown")
        forward(len)
        right(25 )
        draw_branch(len - randint(4,10))
        left(50)
        draw_branch(len - randint(4,10))
        right(25)
        color("brown")
        backward(len)
    else:
        color("green", "green")
        begin_fill()
        circle(10+ randint(0,5))
        end_fill()
        
def draw_tree(start_len):
    pendown()
    setheading(90)
    color("brown")
    pensize(5)
    draw_branch(start_len)
 

penup()
goto(-100, -200)
draw_tree(randint(40, 60))
penup()
goto(100, -180)
draw_tree(randint(30, 40))



