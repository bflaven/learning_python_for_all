#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 009_2_class_trees_python_for_family.py
python3 009_2_class_trees_python_for_family.py

Source: TP_9
Nom : Name
Couleur : Color
Taille : Size
Tronc : Trunk
Racines : Roots
Branches : Branches
Houppier : Crown
Rameaux : Shoots
Fût : Stem




"""




print ("\n --- \/ RESULT \n")


# tree.py
print("\n --- tree.py \n")


class Tree():
    """A simple attempt to represent a tree."""

    def __init__(self, name, color, size, trunk):
        """Initialize attributes to describe a tree."""
        self.name = name # Oak
        self.color = color # Green
        self.size = size # Tall
        self.trunk = trunk # Marroon
        self.roots = 0 # 350
        self.branches = 0 # 500

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.name) + ' that is ' + self.color + ' and ' + self.size +' with a ' + self.trunk + ' trunk'
        # return long_name

        # convert in lower case
        # return long_name.lower()

        # convert in upper case
        return long_name.upper()

    def get_roots_number(self):
	    """Print a statement showing the number of roots for a tree."""
	    print("The tree has " + str(self.roots) + " roots to cling to the earth.")

    	# e.g The tree has 250 roots to cling to the earth
    
    def get_branches_number(self):
	    """Print a statement showing the number of branches for a tree."""
	    print("The tree has " + str(self.branches) + " branches to explore the sky.")

    	# e.g The tree has 67867 branches to explore the sky
     

# output
my_new_tree = Tree('Oak', 'Green', 'Tall', 'Marroon')
print('In the forest, I saw a Tree named ')
print(my_new_tree.get_descriptive_name())


my_new_tree.roots = 354
my_new_tree.get_roots_number()

my_new_tree.branches = 4690
my_new_tree.get_branches_number()





print ("\n --- /\ RESULT \n")




