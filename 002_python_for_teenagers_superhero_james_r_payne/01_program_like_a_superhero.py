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

python3 01_program_like_a_superhero.py


"""

superPowers = ['flight', 'cool cape', '20/20 vision', 'Coding Skillz']
superWeaknesses = ['bologna', 'lactose intolerance', 'social settings',
                   'tight trunks']

print("\n--- result ")
print("Behold our fledgling hero/sidekick, \"Wonder Boy!")
print("His super powers include:", *superPowers)
print("And his weaknesses are:", *superWeaknesses)


superWeaknesses.append('Taco Meat')
print(*superWeaknesses)
print(superWeaknesses.index('Taco Meat'))






