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
python3 16_scripts_for_kids_testing_all.py


"""

# --- python3 16_scripts_for_kids_testing_all.py
# --- example_code_1(16_scripts_for_kids_testing_all.py)
# again = "yes"
# while again == "yes":
#     print ("Hello")
#     again = str(input("Do you want to loop again? "))

# --- python3 16_scripts_for_kids_testing_all.py
# --- example_code_2 (16_scripts_for_kids_testing_all.py)
# total = 0
# while total < 100:
# 	num = int(input("Enter a number: "))
# 	total = total + num
# 	print("The total is", total)
 
# --- python3 16_scripts_for_kids_testing_all.py
# --- example_code_3 (16_scripts_for_kids_testing_all.py)
# import random
# num = random.random()
# num = num * 100
# print("\n--- \/ result ---\n")
# print(num)
# print("\n--- /\ result---\n")

# import random
# num1 = random.randint(0, 1000)
# num2 = random.randint(0, 1000)
# newrand = num1/num2
# print("\n--- \/ result ---\n")
# print(newrand)
# print("\n--- /\ result---\n")


# import turtle
# turtle.shape("turtle")
# for i in range(0,5):
#         turtle.forward(100)
#         turtle.right(72)
#         turtle.exitonclick()

# Python program to draw square
# using Turtle Programming
# import turtle
# skk = turtle.Turtle()
# skk.shape("turtle")
# for i in range(4):
#     skk.forward(50)
#     skk.right(90)
# turtle.done()

# import turtle
# skk = turtle.Turtle()
# skk.shape("turtle")
# for i in range(0,5):
#     skk.forward(200)
#     skk.right(72)
# turtle.done()


# Python program to draw star
# using Turtle Programming
# import turtle

# star = turtle.Turtle()
# star.shape("turtle")

# for i in range(50):
#     star.forward(200)
#     star.right(144)
# turtle.done()

# import turtle
# tina = turtle.Turtle()
# tina.shape('turtle')

# tina.penup()
# tina.forward(20)
# tina.write("Why, hello there!")
# tina.backward(20)

import turtle
tina = turtle.Turtle()
tina.shape("turtle")

tina.forward(50)
tina.left(90)
tina.forward(50)
tina.left(90)
tina.forward(50)

### MODEL ###
# Challenge 050
# num = int(input("Enter a number between 10 and 20: "))

# while num < 10 or num > 20:
#     if num < 10:
#         print("Too low!")
#     else:
#         print("Too high")
#     num = int(input("Try again: "))

# print("Thank you!")



# Challenge 045
# total = 0
# while total <= 50:
#     num = int(input('Enter a number: '))
#     total = total + num
#     print("The total is ...", num)
