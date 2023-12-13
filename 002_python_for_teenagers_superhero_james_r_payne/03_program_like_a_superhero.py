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

python3 03_program_like_a_superhero.py


"""
# Importing the random module to use for randomizing numbers and strings later
import random
# Importing the time module to create a delay
import time
# Creating - or initializing - our variables that will hold character stats
brains = 0
braun = 0
stamina = 0
wisdom = 0
power = 0
constitution = 0
dexterity = 0
speed = 0
answer = ''
# Creating a list of possible super powers
superPowers = ['Flying', 'Super Strength', 'Telepathy', 'Super Speed', 'Can Eat a Lot of Hot Dogs', 'Good At Skipping Rope']
# Creating lists of possible first and last names
superFirstName = ['Wonder','Whatta','Rabid','Incredible', 'Astonishing', 'Decent', 'Stupendous', 'Above-average', 'That Guy', 'Improbably']
superLastName = ['Boy', 'Man', 'Dingo', 'Beefcake', 'Girl', 'Woman', 'Guy', 'Hero', 'Max', 'Dream', 'Macho Man','Stallion']
# Introductory text
print("Are you ready to create a super hero with the Super Hero Generator 3000?")


# Ask the user a question and prompt them for an answer
# input() 'listens' to what they type on their keyboard
# We then use upper() to change the users answer to all uppercase letters
print("Enter Y/N:")
answer = input()
answer = answer.upper()



# While loop to check for the answer "Y"
# This loop will continue while the value of answer IS NOT "Y"
# Only when the user types "Y" will the loop exit and the program continue
while answer != "Y":
    print("I'm sorry, but you have to choose Y to continue!")
    print("Choose Y/N:")
    answer = input()
    answer = answer.upper()
print("Great, let's get started!")
print("Randomizing name...")
# Creating suspense using the time() function
for i in range(3):
    print("...........")
    time.sleep(3)
    print("(I bet you can't stand the suspense!)")
    print("")
# Randomizing Super Hero Name
# We do this by choosing one name from each of our two name lists
# And adding it to the variable superName
superName=random.choice(superFirstName) + " " + \
random.choice(superLastName)
print("Your Super Hero Name is:")
print(superName)

# Randomly choosing a super power from the superPowers list
# and assigning it to the variable power
power = random.choice(superPowers)
# Printing out the variable power and some text
print("Your new power is:")
print(power)
print("")









