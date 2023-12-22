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


# lancer le script "arbre-5.py"
python arbre-5.py


https://pythonturtle.academy/rainbow-colored-tree/
"""



import turtle
import colorsys

def draw_stick(x,y,length,pensize,color,angle):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(angle)
    turtle.pensize(pensize)
    turtle.down()
    turtle.color(color)
    turtle.fd(length)

def draw_tree(x,y,length,pensize,hue,angle,fat_angle,n):
    if n == 0:
        return
    (r,g,b) = colorsys.hsv_to_rgb(hue,1,1)
    draw_stick(x,y,length,pensize,(r,g,b),angle)
    tx = turtle.xcor()
    ty = turtle.ycor()
        
    draw_tree(tx,ty,length*0.7,pensize*0.7,hue-1/13,angle+fat_angle,fat_angle,n-1)
    draw_tree(tx,ty,length*0.7,pensize*0.7,hue-1/13,angle-fat_angle,fat_angle,n-1)
    
turtle.setup(800,800)
turtle.title("Rainbow Colored Tree - PythonTurtle.Academy")
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)
turtle.bgcolor('black')

draw_tree(0,-300,200,10,12/13,90,25,12)
turtle.update()
turtle.getcanvas().postscript(file="tree_5.png")


