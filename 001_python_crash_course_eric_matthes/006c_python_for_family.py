#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 006c_python_for_family.py
python3 006c_python_for_family.py

Source: TP_5
Extract from chap_06 python_crash_course


"""

print ("\n --- \/ RESULT \n")


# example_1
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# example_2
# aliens.py
print("\n --- aliens.py \n")

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(0, 30):
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 10 aliens:
# for alien in aliens[0:10]:
#     print(alien)
# print("...")


for alien in aliens[0:3]:
    if alien['color'] == 'green':
        #values
        alien['color'] = 'rose'
        alien['speed'] = 'snail'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        #values
        alien['color'] = 'prune'
        alien['speed'] = 'superligh'
        alien['points'] = 15

# Show the first 10 aliens:
for alien in aliens[0:10]:
    print(alien)
print("...")

print ("\n --- /\ RESULT \n")




