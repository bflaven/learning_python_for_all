#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 006_python_for_family.py
python3 006_python_for_family.py

Source: TP_5
Extract from chap_06 python_crash_course


"""

"""
alien.py
aliens.py
favorite_languages.py
many_users.py
pizza.py
user.py

"""

print ("\n --- \/ RESULT \n")


# alien.py
print("\n --- alien.py \n")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Figure out how far to move the alien based on its speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New position: " + str(alien_0['x_position']))

# favorite_languages.py
print("\n --- favorite_languages.py \n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
    
    
    

# aliens.py
print("\n --- aliens.py \n")

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print("...")




# many_users.py
print("\n --- many_users.py \n")

users = {
        'aeinstein': {'first': 'albert',
                       'last': 'einstein',
                       'location': 'princeton'},
        'mcurie': {'first': 'marie',
                    'last': 'curie',
                    'location': 'paris'},
         }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


# pizza.py
print("\n --- pizza.py \n")

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


# user.py
print("\n --- user.py \n")

user_0 = {'username': 'efermi',
          'first': 'enrico',
          'last': 'fermi',
          }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)




print ("\n --- /\ RESULT \n")




