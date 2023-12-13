#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python by Example Book - exercises
"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/002_learning_python_for_family/002_learn_code_for_kids/english_booK_python_by_example/



python 01_scripts_for_kids_2.py

"""

"""
001
Display hello world in the console
This script prints the classic "Hello, World!" message to the console, serving as a simple introduction to programming.
"""
# Printing the "Hello world" message to the console
print("Hello world")



"""
002
Display the name defined in the variable {name} in "hello {name}" in the console
This script demonstrates the use of a variable and f-string formatting to display a personalized greeting in the console.
"""

# Defining a variable 'name' with the value "Bruno"
name = "Bruno"

# Printing a greeting using f-string formatting, incorporating the value of the 'name' variable
print(f"Bonjour {name}")



"""
003
Display a certain part of the word "Magically".
This script demonstrates string slicing in Python by extracting a substring from the word "Magically." It starts from index 1 and goes up to index 4 (exclusive), resulting in the expected output "agi."

"""

# Extracting a substring from "Magically" and printing the result
print("Magically"[1:4])
# OUTPUT
# agi


"""
004
Make a loop and display a list of number
This code is a simple Python script that uses a "for" loop to iterate over a range of numbers from 1 to 19 (20 is not included). In each iteration, it prints the current value of the variable i.

"""
for i in range (1,20):
    print(i)

## IF STATEMENTS CHALLENGES ###

# Challenge 012
# num1 = int(input("Enter first number (num1): "))
# num2 = int(input("Enter second number (num2): "))
# if num1 > num2:
#     print('num1 is superior to num2')
#     print(f'num1 = {num1}')
#     print(f'num2 = {num2}')
    
# else:
#     print('num1 is inferior or equal to num2')
#     print(f'num1 = {num1}')
#     print(f'num2 = {num2}')

## FOR LOOP CHALLENGES ###

# Challenge 035 & 36

# name = input("Enter your name: ")
# print(name)


# num = int(input("Enter a number: "))
#     # print(name)


# for i in range(0, num):
#     print (i)


# Challenge 051
"""
Using the song “10 green bottles”, display the lines “There are [num] green bottles hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle should accidentally fall”. Then ask the question “how many green bottles will be hanging on the wall?” If the user answers correctly, display the message “There will be [num] green bottles hanging on the wall”. If they answer incorrectly, display the  message “No, try again” until they get it right. When the number of green
bottles gets  down to 0, display the message “There are no more green bottles hanging on the wall”.
"""

# count = 10
# while count > 0:
#     print("There are", count, "green bottles hanging on the wall")
#     print(count, "green bottles hanging on the wall, and if 1 green bottle should accidentally fall.")
#     count = count - 1
#     answer = int(input("How many green bottles will be hanging on the wall? "))
#     if answer == count:
#         print("Correct! There will be ", count,
#               "green bottles hanging on the wall.")
#     else:
#         while answer != count:
#             answer = int(input("No, try again: "))
# print("There are no more green bottles hanging on the wall.")


### RANDOM CHALLENGE ###

"""
053
Display a random fruit from a list of five fruits
"""

import random
def get_random_choice(input_array):
    return random.choice(input_array)


print(get_random_choice(["apple", "pear", "peach", "banana", "mango"]))
