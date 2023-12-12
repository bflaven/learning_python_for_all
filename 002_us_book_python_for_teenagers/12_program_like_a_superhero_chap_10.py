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

python3 12_program_like_a_superhero_chap_10.py


"""


# Example of exception handling a ValueError
try:
    pin = int(input("Enter your pin number: "))
    print("You entered: ", pin)
except ValueError:
    print("You must only enter a numeric value.")




