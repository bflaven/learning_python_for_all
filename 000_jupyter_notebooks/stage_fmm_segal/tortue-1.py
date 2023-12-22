#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# le chemin
cd /Users/macbookair/Documents/stage_fmm

# lancer le script
python lenomquejeveux-1.py

Source: 21/12/23 TP_SEGAL_1

"""
# import turtle library
import turtle             
my_wn = turtle.Screen()
turtle.speed(2)
for i in range(30):
   turtle.circle(5*i)
   turtle.circle(-5*i)
   turtle.left(i)
turtle.exitonclick()




