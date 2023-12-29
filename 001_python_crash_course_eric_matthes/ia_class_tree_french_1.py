#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_crash_course_eric_matthes/

python ia_class_tree_french_1.py

Source: TP_1

"""

import random

class Arbre:
    def __init__(self, tronc, racines, branches, couronne):
        self.tronc = tronc
        self.racines = racines
        self.branches = branches
        self.couronne = couronne

    def hiver(self):
        return "En hiver, le {} et les {} sont en dormance, et la {} peut perdre ses feuilles.".format(self.tronc, self.branches, self.couronne)

    def été(self):
        return "En été, le {}, les {} et les {} prospèrent, et la {} est pleine de feuilles.".format(self.tronc, self.racines, self.branches, self.couronne)

    def automne(self):
        return "En automne, le {} et les {} peuvent afficher des couleurs vibrantes, et la {} peut perdre ses feuilles.".format(self.tronc, self.branches, self.couronne)

    def printemps(self):
        return "Au printemps, le {} et les {} commencent à fleurir, et la {} obtient de nouvelles feuilles.".format(self.tronc, self.branches, self.couronne)

    def vivaldi(self):
        infos = [
            "Les arbres jouent un rôle crucial dans la séquestration du carbone.",
            "Certains arbres perdent leurs feuilles en hiver pour économiser de l'énergie.",
            "Les racines ancrent l'arbre et absorbent les nutriments du sol.",
            "Les branches fournissent un support structurel et transportent les nutriments vers les feuilles.",
            "Le tronc est la structure de support principale de l'arbre.",
            "La couronne, ou le feuillage, est la partie supérieure de l'arbre qui contient les feuilles.",
            "Différentes espèces d'arbres ont des motifs de croissance et des formes distincts.",
            "Certains arbres produisent des fruits et des graines comme moyen de reproduction.",
            "Les arbres contribuent à la biodiversité en fournissant des habitats pour diverses espèces.",
            "Les forêts aident à maintenir l'équilibre écologique et à réguler le climat."
        ]
        return random.choice(infos)

# Exemple d'utilisation :
mon_arbre = Arbre(tronc="tronc épais", racines="système racinaire étendu", branches="branches larges", couronne="couronne verte luxuriante")

print(mon_arbre.hiver())
print(mon_arbre.été())
print(mon_arbre.automne())
print(mon_arbre.printemps())
print(mon_arbre.vivaldi())



