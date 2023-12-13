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

python3 14_program_like_a_superhero_chap_10.py


"""

# Example of exception handling a ValueError
# Using a Try Except Else block
# Enclosed in a while loop
repeat = 1
while repeat > 0:
        try:
            pin = int(input("Enter your pin number: "))
        except ValueError:
            print("You must only enter a numeric value.")
            repeat = 1
        else:
            print("You entered: ", pin)
        repeat = 0
