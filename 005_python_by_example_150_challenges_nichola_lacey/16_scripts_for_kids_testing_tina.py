#!/usr/bin/python
# -*- coding: utf-8 -*-
#


"""
https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md#the-world


python --version
# Python 2.7.10

python3 --version
# Python 3.7.7



cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_000_python_for_family/002_learn_code_for_kids/english_booK_python_by_example/

# required
python3 16_scripts_for_kids_testing_tina.py


https://hourofpython.trinket.io/a-visual-introduction-to-python#/turtles/moving


"""


# import turtle
# tina = turtle.Turtle()
# tina.shape("turtle")

# tina.forward(50)
# tina.left(90)
# tina.forward(50)
# tina.left(90)
# tina.forward(50)

import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.penup()
tina.goto(30, -150)
tina.pendown()
tina.circle(130)
tina.penup()
tina.goto(0, 0)
tina.pendown()
tina.circle(20)
tina.circle(10)
tina.penup()
tina.forward(60)
tina.right(45)
tina.pendown()
tina.circle(30)
tina.circle(10)
tina.penup()
tina.right(90)
tina.forward(90)
tina.pendown()
tina.circle(40)
tina.penup()
tina.goto(25, -25)
