#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 003_python_for_family.py
python3 003_python_for_family.py

Source: TP_3
Extract from chap_04 python_crash_course

"""
print ("\n --- \/ RESULT \n")

# 1. magicians.py
print ("\n --- magicians.py \n")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you everyone, that was a great magic show!")


# 2. first_numbers.py
print ("\n --- first_numbers.py \n")
for value in range(1, 5):
    print(value)

# 3. even_numbers.py
print ("\n --- even_numbers.py \n")
numbers = list(range(1, 6))
print(numbers)


# 4. squares.py
print ("\n --- squares.py \n")
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

# 4a. simple_statistics.py
print ("\n --- simple_statistics.py \n")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
digits_min = min(digits)
print (digits_min)
# 0
digits_max = max(digits)
print (digits_max)
# 9
digits_sum = sum(digits)
print (digits_sum)
# 45

# 5. players.py
print ("\n --- players.py \n")
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
# 6. foods.py
print ("\n --- foods.py \n")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Tuples
# 7. dimensions.py
print ("\n --- dimensions.py \n")
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


print ("\n --- /\ RESULT \n")




