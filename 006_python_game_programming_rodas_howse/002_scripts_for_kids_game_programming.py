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

# [path]
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/006_python_game_programming_rodas_howse/


# Launch the script
python 002_scripts_for_kids_game_programming.py

"""


#import tkinter
import tkinter as tk
   

class Game(tk.Frame):
    def __init__(self, master):


        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self, bg='#aaaaff',
                                width=self.width,
                                height=self.height)


        self.canvas.pack()
        self.pack()


# load it baby
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Hello, Pong!')
    game = Game(root)
    game.mainloop()
