#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 010_python_for_family_pizza.py

Source: TP_9

CAUTION
The file is imported in 008_python_for_family.py

"""


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

# launch the function        
# make_pizza(16, 'pepperoni')
make_pizza(24, 'mushrooms, green peppers, extra cheese')
