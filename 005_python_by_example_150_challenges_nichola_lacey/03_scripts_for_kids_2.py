#!/usr/bin/python
# -*- coding: utf-8 -*-
#
"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_learn_code_for_kids/python_by_example/



python 03_scripts_for_kids_2.py


python3 03_scripts_for_kids_2.py



"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_learn_code_for_kids/python_by_example/



python 03_scripts_for_kids_2.py
python3 03_scripts_for_kids_2.py

"""
# See page 27


# Challenge 001
#print ("Arthur Flaven est vraiment très très con")
   

phrase_arthur = "Variable, Arthur Flaven est vraiment très très très con"

"""
print("\n")
print(phrase_arthur)
print("\n")
print(len(phrase_arthur))
print("\n")
print(str(phrase_arthur)[37:55])
"""

# # Challenge 003
# for i in range (1,5):
#       print(i)
#       print(phrase_arthur)
#       print("\n")
      


# # Challenge 002
# name = "Louise Flaven"
# print(str(name)[7:10])

# # Challenge 003
# for i in range (1,20):
#      print(i)




"""


# Challenge 013
num = int(input("Enter a number that is under 20: "))
if num > 20:
print("The number you entered is too high. Please, try again!")
else:
print("Thank you!")





# Python by Example Book - exercises

## IF STATEMENTS CHALLENGES ###

# Challenge 012
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
print(num2, num1)
else:
print(num1, num2)
"""


"""
# challenge 073
food_dictionnary={}
food1 = input("Enter a food you like: ")
food_dictionnary[1]=food1
print("\n")

food2 = input("Enter a food you like: ")
food_dictionnary[2]=food2
print("\n")

food3 = input("Enter a food you like: ")
food_dictionnary[3]=food3
print("\n")

food4 = input("Enter a food you like: ")
food_dictionnary[4]=food4
print("\n")

food5 = input("Enter a food you like: ")
food_dictionnary[5]=food5
print("\n")

print(food_dictionnary)
print("\n")

dislike = int(input("Enter a food you dislike: ")) 
del food_dictionnary[dislike]
print("\n")
print(sorted(food_dictionnary.values()))

"""


# MORE STRING MANIPULATION

# Challenge 080
"""
Ask the user to enter their first name and then display the length of their first name.
Then ask for their surname and display the length of their username. Join their first name
and surname together with a space between and display the result.
Finally, display the length of their full name (including the space).


Demander à l'utilisateur d'entrer son prénom, puis d'afficher la longueur de son prénom.
Demander ensuite le nom de famille et afficher la longueur de leur nom de famille. Attacher le prénom et le nom de famille avec un espace entre les deux  et afficher le résultat.

Enfin, afficher la longueur de leur nom complet (le prénom plus le nom de famille)


"""


# def processing(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name


# def length_of(user_input):
#     return len(user_input)


# def display_length_name():
#     user_first_name = input("Entre ton prénom : ")
#     user_first_name_length = length_of(user_first_name)
#     print(
#         f"Ton prénom est \"{user_first_name}\" il a \"{user_first_name_length}\" caractères dedans.")

#     user_last_name = input("Entre ton nom : ")
#     user_last_name_length = length_of(user_last_name)
#     print(
#         f"Ton nom est \"{user_last_name}\" il contient \"{user_last_name_length}\" caractères dedans.")

#     full_name = processing(user_first_name, user_last_name)
#     user_full_name_length = length_of(full_name)
#     print(
#         f"Ton nom complet est \"{full_name}\" et il a \"{user_full_name_length}\" caractères dedans."
#     )


# if __name__ == "__main__":
#     display_length_name()



