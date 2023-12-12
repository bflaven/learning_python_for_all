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

python3 02_program_like_a_superhero.py


"""

# Variables to check
wonderBoyAllowance = 20
newCape = 20
newShoes = 50
# Checks if you can afford a new cape
if wonderBoyAllowance >= newCape:
    print("You can afford a new cape.")
    print("But how about new shoes?")
# When the if check to see if you can afford the new cape passes it does this
if wonderBoyAllowance >= newShoes:
    print("Looks like you can afford new shoes as well.")
    print("That's good, because the old ones are really stinky!")
    print("But can you afford both together?")

#If you cannot afford the shoes, but can afford the cape, it does this
# else:
#     print("You can only afford the new cape, sorry.")
# If both of the conditionals fail, the else below triggers
# If even one of the conditionals are true, this else does not trigger
else:
    print("That's a shame, because one of them is really stanky!")









