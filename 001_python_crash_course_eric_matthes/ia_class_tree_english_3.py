#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_crash_course_eric_matthes/

python ia_class_tree_english_3.py

Source: TP_1

System:

Below is an instruction that describes a task. Write a response that appropriately completes the request.

User:

Write a Python class for a object named "Tree" with the following characteristics: Trunk, Roots, Branches, Crown. Within this Class "Tree", write four different methods (functions) for each of the four seasons: Winter, Summer, Autumn, Spring plus an extra method named Vivaldi that tells a random info among ten specific information on Tree.

Assistant:

"""

import random

class Tree:
    def __init__(self, trunk, roots, branches, crown):
        self.trunk = trunk
        self.roots = roots
        self.branches = branches
        self.crown = crown
    
    def winter(self):
        print("The tree is bare during Winter.")
    
    def summer(self):
        print("During Summer, the tree is full of leaves.")
    
    def autumn(self):
        print("In Autumn, the leaves turn red and fall off.")
    
    def spring(self):
        print("Spring brings new growth to the tree.")
    
    def vivaldi(self):
        info = ["The tree is a maple",
                "It has a trunk that's 10 feet long",
                "The crown of the tree is very wide",
                "During winter, the leaves fall off and form a ring around the trunk",
                "In spring, new growth appears on the branches",
                "The tree produces acorns in autumn",
                "During summer, the tree is full of bees buzzing around the flowers",
                "The roots of the tree go deep into the ground",
                "The trunk of the tree is very strong",
                "During winter, the tree's branches form a protective canopy to shield the leaves from the cold wind"]
        print(random.choice(info))

# Example taken from ChatGPT

# Example usage:
my_tree = Tree(trunk="thick trunk", roots="extensive root system", branches="wide branches", crown="lush green crown")

print(my_tree.winter())
print(my_tree.summer())
print(my_tree.autumn())
print(my_tree.spring())
print(my_tree.vivaldi())

