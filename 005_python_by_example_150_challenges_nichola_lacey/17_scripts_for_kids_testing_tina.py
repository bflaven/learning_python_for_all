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
python 17_scripts_for_kids_testing_tina.py
python3 17_scripts_for_kids_testing_tina.py


https://hourofpython.trinket.io/a-visual-introduction-to-python#/turtles/moving

https://github.com/abdo0/python-by-example-150-challenges

"""

import random
import turtle


# challenge-060.py
"""
import turtle
draw = turtle.Turtle()
draw.shape('turtle')
for i in range(0, 4):
  draw.forward(100)
  draw.right(90)
"""

# skk = turtle.Turtle()
# skk.shape("turtle")
# for i in range(4):
#     skk.forward(50)
#     skk.right(90)
# turtle.done()

# challenge-061.py
# draw = turtle.Turtle()
# draw.shape("turtle")
# for i in range(0, 3):
#   draw.forward(100)
#   draw.right(120)
# turtle.done()



# challenge-062.py
# tortuga = turtle.Turtle()
# tortuga.shape('turtle')
# tortuga.circle(100)
# turtle.done()

# challenge-063.py
# tortuga = turtle.Turtle()
# tortuga.shape('turtle')
# # filled_color = ['red', 'blue', 'green']
# filled_color = ['pink', 'orange']


# def drawSquare():
#     for i in range(4):
#       tortuga.forward(100)
#       tortuga.right(90)


# for i in filled_color:
#   tortuga.pendown()
#   tortuga.color(i)
#   tortuga.begin_fill()
#   drawSquare()
#   tortuga.end_fill()
#   tortuga.penup()
#   tortuga.forward(150)
# turtle.done()

# challenge-064.py
# draw = turtle.Turtle()
# draw.shape("turtle")
# for i in range(5):
#   draw.forward(100)
#   draw.right(144)
# turtle.done()

# challenge-065.py

# draw = turtle.Turtle()
# draw.shape("turtle")


# def drawOne():
#   draw.right(90)
#   draw.forward(100)
#   draw.penup()
#   draw.left(90)
#   draw.forward(50)
#   draw.left(90)
#   draw.forward(100)
#   draw.right(90)


# def drawTwo():
#   draw.pendown()
#   draw.forward(70)
#   draw.right(90)
#   draw.forward(50)
#   draw.right(90)
#   draw.forward(70)
#   draw.left(90)
#   draw.forward(50)
#   draw.left(90)
#   draw.forward(70)
#   draw.penup()
#   draw.forward(50)
#   draw.left(90)
#   draw.forward(100)
#   draw.right(90)


# def drawThree():
#   draw.pendown()
#   draw.forward(70)
#   draw.right(90)
#   draw.forward(50)
#   draw.right(90)
#   draw.forward(45)
#   draw.right(180)
#   draw.forward(45)
#   draw.right(90)
#   draw.forward(50)
#   draw.right(90)
#   draw.forward(70)


# drawOne()
# drawTwo()
# drawThree()
# turtle.done()

# challenge-066.py

# draw = turtle.Turtle()
# draw.shape('turtle')
# for i in range(8):
#   draw.pencolor(random.choice(
#       ['red', 'black', 'green', 'purple', 'blue', 'orange']))
#   draw.forward(100)
#   draw.right(45)
# turtle.done()

# challenge-067.py

# draw = turtle.Turtle()
# draw.shape('turtle')
# for j in range(10):
#   for i in range(8):
#     draw.forward(50)
#     draw.right(45)
#   draw.right(36)
# turtle.done()

# challenge-068.py
# import random
# import turtle


# draw = turtle.Turtle()
# # lines = random.randint(10)
# lines = random.randint(0, 10)

# for i in range(lines):
#     length = random.randint(10, 100)
#     angle = random.randint(1, 365)
#     draw.forward(length)
#     draw.right(angle)
# turtle.done()

# https://michael0x2a.com/blog/turtle-examples
# spiral = turtle.Turtle()
# draw.shape('turtle')
# for i in range(20):
#     spiral.forward(i * 10)
#     spiral.right(144)
# turtle.done()


ninja = turtle.Turtle()
ninja.shape('turtle')
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


