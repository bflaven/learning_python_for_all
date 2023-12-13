#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 008_python_for_family.py
python3 008_python_for_family.py

Source: TP_8


"""

"""

formatted_name.py
greet_users.py
greeter.py
making_pizzas.py
person.py
pets.py
pizza.py
printing_models.py
user_profile.py


"""


# uses in making_pizzas.py
import import_python_for_family_pizza as p

print ("\n --- \/ RESULT \n")

# formatted_name.py
print("\n --- formatted_name.py \n")


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


# musician = get_formatted_name('jimi', 'hendrix')
musician = get_formatted_name('arthur', 'flaven')
print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
musician = get_formatted_name('jean', 'baptiste', 'musset')
print(musician)

# greet_users.py
print("\n --- greet_users.py \n")


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


# usernames = ['hannah', 'ty', 'margot']
usernames = ['Arthur', 'Louise', 'Anne', 'Bruno']
greet_users(usernames)



# greeter.py
print("\n --- greeter.py \n")


def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")


# greet_user('jesse')
greet_user('Louise')


# making_pizzas.py
print("\n --- making_pizzas.py \n")
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

p.make_pizza(16, 'caramel')
p.make_pizza(12, 'poivre', 'huile', 'oeufs')


# person.py
print("\n --- person.py \n")


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


# musician = build_person('jimi', 'hendrix', age=27)
musician = build_person('jean-baptiste', 'musset', age=54)
print(musician)



# pets.py
print("\n --- pets.py \n")
def describe_pet(pet_name, animal_type='chien'):
    """Display information about a pet."""
    print("\nJ'ai un " + animal_type + ".")
    print("Mon animal est " + animal_type + ", son nom est " + pet_name.title() + ".")
    
# A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')

describe_pet('swannie')
describe_pet(pet_name='swannie')


# A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('swannie', 'chat')
describe_pet(pet_name='swannie', animal_type='chat')
describe_pet(animal_type='chat', pet_name='swannie')


# printing_models.py
print("\n --- printing_models.py \n")


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3d print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# user_profile.py
print("\n --- user_profile.py \n")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


print ("\n --- /\ RESULT \n")




