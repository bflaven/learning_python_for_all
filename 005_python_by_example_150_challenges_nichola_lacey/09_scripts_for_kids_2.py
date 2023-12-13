#!/usr/bin/python
# -*- coding: utf-8 -*-
#


"""
https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md#the-world


python --version
# Python 2.7.10

python3 --version
# Python 3.7.7



cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_learn_code_for_kids/python_by_example/

python3 09_scripts_for_kids_2.py


"""


from turtle import *
import random

for n in range(60):
    penup()
    goto(random.randint(-400, 400), random.randint(-400, 400))
    pendown()

    red_amount = random.randint(0,  30) / 100.0
    blue_amount = random.randint(50, 100) / 100.0
    green_amount = random.randint(0,  30) / 100.0
    pencolor((red_amount, green_amount, blue_amount))

    circle_size = random.randint(10, 40)
    pensize(random.randint(1, 5))

    for i in range(6):
        circle(circle_size)
        left(60)


