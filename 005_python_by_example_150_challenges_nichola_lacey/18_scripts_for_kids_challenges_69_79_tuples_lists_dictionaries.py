#!/usr/bin/python
# -*- coding: utf-8 -*-
#


"""
https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md#the-world


python --version
# Python 2.7.10

python3 --version
# Python 3.7.7

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_000_python_for_family/002_learn_code_for_kids/english_booK_python_by_example/

# required
python 18_scripts_for_kids_challenges_69_79_tuples_lists_dictionaries.py
python3 18_scripts_for_kids_challenges_69_79_tuples_lists_dictionaries.py


https://github.com/abdo0/python-by-example-150-challenges

"""


# example_1
grades = [{"Ma": 45, "En": 37, "Fr": 54}, {"Ma": 62, "En": 58, "Fr": 59}, {
    "Ma": 49, "En": 47, "Fr": 60}, {"Ma": 78, "En": 83, "Fr": 62}]
print (grades[0]["En"])
# output 37


# example_2
grades = {"Susan": {"Ma": 45, "En": 37, "Fr": 54}, "Peter": {"Ma": 62, "En": 58, "Fr": 59},
          "Mark": {"Ma": 49, "En": 47, "Fr": 60}, "Andy": {"Ma": 78, "En": 83, "Fr": 62}}
print (grades["Peter"]["En"])
# output 58




