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

python3 10_program_like_a_superhero_chap_9.py


"""
# Create a dictionary name algebro and fill it with key-value pairs
algebro = {'codename': 'Algebro', 'power': 'Mathemagics', 'real-name': 'Al. G. Bro.'}
# Using dict.update() to add a key-pair value to our 'algebro' dictionary
# Note the use of curly braces {}, mixed with parentheses ()
algebro.update({'villainType': 'mutate'})
# Printing out the results
print("\n--- printing out the results")
print(algebro)


# CHANGE_1
# Deleting the algebro dictionary using the del keyword
# del algebro

# print(algebro)
# output an error

algebro.clear()
print("\n--- clear algebro")
print(algebro)

