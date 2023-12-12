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

python3 myVeryFirstTestingModule.py
"""

# We first have to import our module
# We import our module by using the name of the file, minus the .py extension

import myVeryFirstModule

# Now we call the function to use it

myVeryFirstModule.firstFunction()

# print the helpfile for firstFunction()

#help(ourFirstModule)

# Calling our second function

myVeryFirstModule.secondFunction()

# Calling and printing a variable within our module

print("The value of a is: ", myVeryFirstModule.X)




