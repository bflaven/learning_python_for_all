#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_crash_course_eric_matthes/

python ia_class_tree_french_2.py

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
        return f"En hiver, le {format(self.tronc)} et les {format(self.branches)} sont en dormance, et la {format(self.couronne)} peut perdre ses feuilles."



    def été(self):
        return f"En été, le {format(self.tronc)}, les {format(self.racines)} et les {format(self.branches)} prospèrent, et la {format(self.couronne)} est pleine de feuilles."

    def automne(self):
        return f"En automne, le {format(self.tronc)} et les {format(self.branches)} peuvent afficher des couleurs vibrantes, et la {format(self.couronne)} peut perdre ses feuilles."

    def printemps(self):
        return f"Au printemps, le {format(self.tronc)} et les {format(self.branches)} commencent à fleurir, et la {format(self.couronne)} obtient de nouvelles feuilles."

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



