#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/003_code_for_family_lesson/

python louise-script-4.py
python3 louise-script-4.py

Source: TP_1

"""


print('\n--- EXEMPLE_1 Lists')
# Lists
# simple_statistics.py
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits))
# 0


print(max(digits))
# 9

print(sum(digits))
# 45


print('\n--- EXEMPLE_2 Tuples')
# Tuples
mytuple = ("apple", "banana", "cherry")
print(mytuple)


# Logique et Programmation par le jeu
print('\n--- EXEMPLE_3 Logique et Programmation par le jeu')


# set the dice
dice=3

# CAS_1
# Si le dé s'immobilise sur la face numéro 1.
# Le lanceur du dé doit exécuter le gage numéro 1
# - 1 - Chanter une chanson accapella

if dice == 1: # CAS_1
	print("CAS_1")
	print("- 1 - Chanter une chanson accapella")

# CAS_2
# Si le dé s'immobilise sur la face numéro 2.
# Le lanceur du dé doit exécuter le gage numéro 1 à savoir
# - 2 - Chanter une chanson avec de l'eau dans la bouche
elif dice == 2: # CAS_2
	print("CAS_2")
	print("- 2 - Chanter une chanson avec de l'eau dans la bouche")


# CAS_3
# Si le dé s'immobilise sur la face numéro 3. 
# Le lanceur du dé doit exécuter le gage numéro 1 à savoir
# - 3 - Raconter une blague
elif dice == 3: # CAS_3
	print("CAS_3")
	print("- 3 - Raconter une blague")


# CAS_4
# Si le dé (dice) s'immobilise sur la face numéro 4. 
# Le lanceur du dé doit exécuter le gage numéro 1 à savoir
# - 4 - Raconter une blague dans une autre langue
elif dice == 4: # CAS_4
	print("CAS_4")
	print("- 4 - Raconter une blague dans une autre langue")


# CAS_5
# Si le dé s'immobilise sur la face numéro 5. 
# Le lanceur du dé doit exécuter le gage numéro 1 à savoir
# - 5 - Mettre un vêtement à l'envers
elif dice == 5: # CAS_5
	print("CAS_5")
	print("- 5 - Mettre un vêtement à l'envers")


# CAS_6 
# Si le dé s'immobilise sur la face numéro 6. 
# Le lanceur du dé doit exécuter le gage numéro 1 à savoir
# - 6 - Imiter le cri d'un animal
elif dice == 6: # CAS_6
	print("CAS_6")
	print("- 6 - Imiter le cri d'un animal")


# CAS_FAILED
# Si le dé se perd aucune face ne sort. 
# Le lanceur ne fait rien et tous les joueurs cherchent le dé 
# Le gage collectif est que tous les joueurs cherchent le dé pour reprendre le jeu.
else: # CAS_FAILED
	print("dice is null")



# Dictionaries
print('\n--- EXEMPLE_4 Dictionaries')

little_kid = {'name': 'arthur', 'age': 11}
little_kid = {'name': 'louise', 'age': 13}

print(little_kid['name'])