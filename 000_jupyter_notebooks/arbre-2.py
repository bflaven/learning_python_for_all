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


# lancer le script "arbre-2.py"
python arbre-2.py


"""


# Python program to draw a tree using turtle 
# Importing required modules 
import turtle 
import math 


# Function to draw rectangle 
def drawRectangle(t, width, height, color): 
	t.fillcolor(color) 
	t.begin_fill() 
	t.forward(width) 
	t.left(90) 
	t.forward(height) 
	t.left(90) 
	t.forward(width) 
	t.left(90) 
	t.forward(height) 
	t.left(90) 
	t.end_fill() 

	
# Function to draw triangle	 
def drawTriangle(t, length, color): 
	t.fillcolor(color) 
	t.begin_fill() 
	t.forward(length) 
	t.left(135) 
	t.forward(length / math.sqrt(2)) 
	t.left(90) 
	t.forward(length / math.sqrt(2)) 
	t.left(135) 
	t.end_fill() 

	
# Set the background color 
screen = turtle.Screen ( ) 
screen.bgcolor("skyblue") 


# Creating turtle object 
tip = turtle.Turtle() 
tip.color ("black") 
tip.shape ("turtle") 
tip.speed (2) 


# Tree base 
tip.penup() 
tip.goto(100, -130) 
tip.pendown() 
drawRectangle(tip, 20, 40, "brown") 


# Tree top 
tip.penup() 
tip.goto(65, -90) 
tip.pendown() 
drawTriangle(tip, 90, "lightgreen") 
tip.penup() 
tip.goto(70, -45) 
tip.pendown() 
drawTriangle(tip, 80, "lightgreen") 
tip.penup() 
tip.goto(75, -5) 
tip.pendown() 
drawTriangle(tip, 70, "lightgreen")









