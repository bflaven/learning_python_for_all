#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 006e_python_for_family.py
python3 006e_python_for_family.py

Source: TP_5
Extract from chap_06 python_crash_course


"""

print ("\n --- \/ RESULT \n")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

print ("\n --- /\ RESULT \n")




