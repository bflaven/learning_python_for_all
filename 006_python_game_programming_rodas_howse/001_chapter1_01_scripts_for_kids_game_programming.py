#!/usr/bin/python
# -*- coding: utf-8 -*-
#



"""
[env]
# Conda Environment
conda create --name kids_game_programming python=3.9.13
conda info --envs
source activate kids_game_programming
conda deactivate

# if needed to remove
conda env remove -n [NAME_OF_THE_CONDA_ENVIRONMENT]
conda env remove -n kids_game_programming

# update conda 
conda update -n base -c defaults conda

# to export requirements
pip freeze > requirements.txt

# to install
pip install -r requirements.txt

conda install -c anaconda tk



# [path]
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/006_python_game_programming_rodas_howse/


# Launch the script
python 001_chapter1_01_scripts_for_kids_game_programming.py


"""
#import tkinter
import tkinter as tk
   
lives = 3
root = tk.Tk()
frame = tk.Frame(root)
# canvas = tk.Canvas(frame, width=600, height=400, bg='#aaaaff')
canvas = tk.Canvas(frame, width=800, height=600, bg='#ff0000')

frame.pack()
canvas.pack()
root.title('Hello, Pong!')
root.mainloop()

   
