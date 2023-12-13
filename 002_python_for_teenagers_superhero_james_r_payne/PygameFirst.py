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

python3 PygameFirst.py
"""


import pygame
from pygame.locals import *
import sys
# Initialize all of the Pygame modules so we can use them later on
pygame.init()
# Create the game screen and set it to 800 x 600 pixels
screen = pygame.display.set_mode((800, 600))
# Create a loop that will keep the game running
# Until the user decides to quit
while True:
    # Get feedback from the player in the form of events
    for event in pygame.event.get():
    # If the player clicks the red 'x', it is considered a quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


