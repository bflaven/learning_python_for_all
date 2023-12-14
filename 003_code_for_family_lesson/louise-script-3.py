#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/003_code_for_family_lesson/

python louise-script-3.py
python3 louise-script-3.py

Source: TP_1

"""

# it suppose to have random installed
import random

def generate_name(starts_with):
    names = ["Bernard", "Jonas", "Nomonde", "Robert", "Guido", "Lorenzo", "Pia", "Prisca", "Minnie", "Margaret", "Myrtle", "Noa", "Nadia"]
    if starts_with:
        names = [n for n in names if n.lower().startswith(starts_with)]
    random_name = random.choice(names)
    # return {"name": random_name}
    print(random_name)




print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('What is your search? Tip: type a name with "m" like Mendel') # ask for their name
mySearch = input()
generate_name(mySearch)
