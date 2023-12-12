#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 006a_python_for_family.py
python3 006a_python_for_family.py

Source: TP_5
Extract from chap_06 python_crash_course


"""

print ("\n --- \/ RESULT \n")

# example_1
# little_kid = {'name': 'arthur', 'age': 11}
# little_kid = {'name': 'Louise', 'age': 13}

# print(little_kid['name'])
# print(little_kid['age'])

# example_2
# required python3
# the_kid_name = little_kid['name']
# print(f"Tu te nommes donc {the_kid_name}, super !")


# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# example_3
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# example_4
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# example_5
# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")


# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")

# example_6
# alien.py
# print("\n --- alien.py \n")

# alien_0 = {'x_position': 5, 'y_position': 25, 'speed': 'medium'}
# print("Original position: " + str(alien_0['x_position']))

# # Move the alien to the right.
# # Figure out how far to move the alien based on its speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast alien.
#     x_increment = 3

# # The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print("New position: " + str(alien_0['x_position']))


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)



print ("\n --- /\ RESULT \n")




