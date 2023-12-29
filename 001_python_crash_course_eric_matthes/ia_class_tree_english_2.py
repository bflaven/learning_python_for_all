#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_crash_course_eric_matthes/

python ia_class_tree_english_2.py

Source: TP_1

"""
import random

class Tree:
    def __init__(self, trunk, roots, branches, crown):
        self.trunk = trunk
        self.roots = roots
        self.branches = branches
        self.crown = crown

    def winter(self):
        return f"In winter, the {format(self.trunk)} and {format(self.roots)} are dormant, and the {format(self.crown)} may lose its leaves."

    def summer(self):
        return f"In summer, the {format(self.trunk)} and {format(self.roots)} are flourishing, and the {format(self.crown)} is full of leaves."

    def autumn(self):
        return f"In autumn, the {format(self.trunk)} and {format(self.roots)} may display vibrant colors, and the {format(self.crown)} may shed its leaves."

    def spring(self):
        return f"In spring, the {format(self.trunk)} and {format(self.roots)} start to bloom, and the {format(self.crown)} gets new leaves."

    def vivaldi(self):
        info_list = [
            "Trees play a crucial role in carbon sequestration.",
            "Certain trees shed their leaves in winter to conserve energy.",
            "Roots anchor the tree and absorb nutrients from the soil.",
            "Branches provide structural support and carry nutrients to the leaves.",
            "The trunk is the main support structure of the tree.",
            "The crown, or canopy, is the upper part of the tree that contains the leaves.",
            "Different tree species have distinct growth patterns and shapes.",
            "Some trees produce fruits and seeds as a means of reproduction.",
            "Trees contribute to biodiversity by providing habitats for various species.",
            "Forests help maintain ecological balance and regulate climate."
        ]
        return random.choice(info_list)

# Example usage:
my_tree = Tree(trunk="thick trunk", roots="extensive root system", branches="wide branches", crown="lush green crown")

print(my_tree.winter())
print(my_tree.summer())
print(my_tree.autumn())
print(my_tree.spring())
print(my_tree.vivaldi())


