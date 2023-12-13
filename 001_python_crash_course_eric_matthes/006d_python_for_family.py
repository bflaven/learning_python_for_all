#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 006d_python_for_family.py
python3 006d_python_for_family.py

"""

print ("\n --- \/ RESULT \n")

# 006d_python_for_family.py.py
print("\n --- 006d_python_for_family.py \n")

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

print ("\n --- /\ RESULT \n")




