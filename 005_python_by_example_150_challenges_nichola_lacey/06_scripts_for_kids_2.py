#!/usr/bin/python
# -*- coding: utf-8 -*-
#


"""
python --version
# Python 2.7.10

python3 --version
# Python 3.7.7



cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_learn_code_for_kids/python_by_example/

python3 06_scripts_for_kids_2.py


"""


# MORE STRING MANIPULATION

# challenge 81
"""
subject = input("Enter your favourire school subject: ")
for letter in subject:
    print (letter, end="-")
print ("\n")
"""

# from random import random
# num = random()


from random import randrange
# print(randrange(10))


yep_msg = "You win man"
num = randrange(10)
print(f"num => \"{num}\" ")


correct_answer = False
while correct_answer == False:
    guess = int(input("Type a number:"))
    if guess == num:
        correct_answer = True
        print(f"\n--- {yep_msg} --- ")
