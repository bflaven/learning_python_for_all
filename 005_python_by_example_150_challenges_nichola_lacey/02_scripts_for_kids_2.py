#!/usr/bin/python
# -*- coding: utf-8 -*-
#
"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_learn_code_for_kids/python_by_example/


jupyter notebook
python 02_scripts_for_kids_2.py

https://docs.python.org/3/library/turtle.html


"""


# import turtle

# wn = turtle.Screen()
# wn.bgcolor("lightgreen")        # set the window background color

# tess = turtle.Turtle()
# tess.color("blue")              # make tess blue
# tess.pensize(3)                 # set the width of her pen

# tess.forward(50)
# tess.left(120)
# tess.forward(50)

# wn.exitonclick()


import turtle
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


# import turtle
# for i in range(0, 13):
# 	turtle.forward(150)
# 	turtle.right(80)
# turtle.exitonclick

# import turtle
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
# 	for i in range(0, 6):
# 		turtle.forward(150)
# 		turtle.right(80)
# end_fill()
# done()
