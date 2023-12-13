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

python3 10_scripts_for_kids_2.py


"""


import turtle
turtle.shape("turtle")
ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()
