#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 005a_python_for_family.py
python3 005a_python_for_family.py

Source: TP_4
Extract from chap_05 python_crash_course

"""





print ("\n --- \/ RESULT \n")


# amusement_park.py
print("\n --- amusement_park.py \n")

# age = 12
age = 50


if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# banned_users.py
print("\n --- banned_users.py \n")
banned_users = ['andrew', 'carolina', 'david']

# WRONG
user = 'andrew'

# GOOD
# user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
else:
    print("Hey, you cannot post a response!")


# cars.py
print("\n --- cars.py \n")
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# magic_number.py
print("\n --- magic_number.py \n")
# WRONG
# answer = 17

# GOOD
answer = 42

if answer != 42:
    print("That is not the correct answer. Please try again!")
else:
    print("This is the correct answer. The answer is 42!")

# toppings.py
print("\n --- toppings.py \n")

# WRONG
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

# GOOD
available_toppings = ['mushrooms', 'french fries', 'olives',
                      'green peppers', 'pepperoni', 'pineapple', 'extra cheese']


requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza anyway!")

# voting.py
print("\n --- voting.py \n")

# WRONG
# age = 17

# GOOD
age = 42



if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


print ("\n --- /\ RESULT \n")




