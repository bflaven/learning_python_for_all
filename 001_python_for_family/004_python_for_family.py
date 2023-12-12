#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 004_python_for_family.py
python3 004_python_for_family.py

Source: TP_4
Extract from chap_05 python_crash_course


"""

"""
variable (integer) : 1, 2, 3, 4, 5, 6
CAS_1, dice = 1
CAS_2, dice = 2
CAS_3, dice = 3
CAS_4, dice = 4
CAS_5, dice = 5 
CAS_6, dice = 6
CAS_FAILED, dice is null 
"""

# A la sortie du lancer de mon dé virtuel la face est égale au chiffre 3
dice = 878978789

print ("\n --- \/ RESULT \n")

# CAS_1
# Si le dé s'immobilise sur la face numéro 1.
# Le lanceur du dé doit exécuter le gage numéro 1
# - 1 - Chanter une chanson accapella

if dice == 1:  # CAS_1
    print("# CAS_1")
    print("- 1 - Chanter une chanson accapella")

# CAS_2
# Si le dé s'immobilise sur la face numéro 2.
# Le lanceur du dé doit exécuter le gage numéro 1 à savoir
# - 2 - Chanter une chanson avec de l’eau dans la bouche
elif dice == 2:  # CAS_2
    print("# CAS_2")
    print("- 2 - Chanter une chanson avec de l’eau dans la bouche")


# CAS_3
# Si le dé s'immobilise sur la face numéro 3.
# Le lanceur du dé doit exécuter le gage numéro 1 à savoir
# - 3 - Raconter une blague
elif dice == 3:  # CAS_3
    print("# CAS_3")
    print("- 3 - Raconter une blague")


# CAS_4
# Si le dé (dice) s'immobilise sur la face numéro 4.
# Le lanceur du dé doit exécuter le gage numéro 1 à savoir
# - 4 - Raconter une blague dans une autre langue
elif dice == 4:  # CAS_4
    print("# CAS_4")
    print("- 4 - Raconter une blague dans une autre langue")


# CAS_5
# Si le dé s'immobilise sur la face numéro 5.
# Le lanceur du dé doit exécuter le gage numéro 1 à savoir
# - 5 - Mettre un vêtement à l’envers
elif dice == 5:  # CAS_5
    print("# CAS_5")
    print("- 5 - Mettre un vêtement à l’envers")


# CAS_6
# Si le dé s'immobilise sur la face numéro 6.
# Le lanceur du dé doit exécuter le gage numéro 1 à savoir
# - 6 - Imiter le cri d'un animal
elif dice == 6:  # CAS_6
    print("# CAS_6")
    print("- 6 - Imiter le cri d'un animal")


# CAS_FAILED
# Si le dé se perd aucune face ne sort.
# Le lanceur ne fait rien et tous les joueurs cherchent le dé
# Le gage collectif est que tous les joueurs cherchent le dé pour reprendre le jeu.
else:  # CAS_FAILED
    print("dice est nul...")


print ("\n --- /\ RESULT \n")




