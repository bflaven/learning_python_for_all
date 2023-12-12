#!/usr/bin/python
# -*- coding: utf-8 -*-
#


"""
https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md#the-world


python --version
# Python 2.7.10

python3 --version
# Python 3.7.7


cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_learn_code_for_kids/python_for_teenagers/

python3 PygameSecond.py
"""


import pygame
from pygame.locals import *
import sys


# Creating a tuple to hold the RGB (Red, Green Blue) values
# So that we can paint our screen blue later
colorBLUE = (0, 0, 255)
# Initialize all of the Pygame modules so we can use them later on
pygame.init()
# Create the game screen and set it to 800 x 600 pixels
screen = pygame.display.set_mode((800, 600), 0, 32)
# Set a caption to our window
pygame.display.set_caption("Super Sidekick: Sophie the Bulldog!")
# Draw a blue background onto our screen/window
screen.fill(colorBLUE)
# Draw the now blue window to the screen
pygame.display.update()
# Create a variable to hold the value of whether
# The game should end or not
running = True
# Create a loop that will keep the game running
# Until the user decides to quit
# When they do, it will change the value of running
# To False, ending the game
while True:
    # Get feedback from the player in the form of events
    for event in pygame.event.get():
    # If the player clicks the red 'x', it is considered a quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()




