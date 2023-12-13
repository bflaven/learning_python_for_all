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

python3 11_scripts_for_kids_2.py


"""


# CODE 1

# What comes after the # is not seen by python. These are comments. :)

from turtle import *  # imports the module turtle,
#* stands for all, which makes things easier

speed(0)  # sets the speed of drawing to 0, which is the fastest
pencolor('green')  # sets the color of the pen/lines to white
bgcolor('blue')  # sets the color of the background/canvas to black

x = 0  # creates a variable x with value 0
up()  # lifts up the pen, so no lines are drawn

#note fd() means move forward, bk() means move back
# rt() or lt() means tilt right by a certain angle

rt(45)
fd(90)
rt(135)

down()  # sets down the pen, so that turtle can draw
while x < 120:  # while the value of x is lesser than 120,
    #continuously do this:
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)

    rt(11.1111)
    x = x+1  # adds 1 to the value of x,
    # so that it is closer to 120 after every loop

exitonclick()  # When you click, turtle exits.

#That's all! Try customizing the script! 8)
