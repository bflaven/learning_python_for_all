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

python3 07_program_like_a_superhero_chap_9.py


"""
# Create a dictionary name algebro and fill it with key-value pairs
algebro = {'codename': 'Algebro', 'power': 'Mathemagics', 'real-name': 'Al. G. Bro.'}
# Print just the keys in the algebro dictionary
# print(algebro.keys())

# Print just the values in the algebro dictionary
# print(algebro.values())

# Print the key-value pairs
# print(algebro.items())

# Using a for loop to iterate through and print out our dictionary
for key, value in algebro.items():
    print("The key is: ", key, " and the value is: ", value)
