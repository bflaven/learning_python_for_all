# 001_maksim_football_team_rating.py

"""
# chemin
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/000_jupyter_notebooks/stage_fmm_maksim/002_stage_cat_cat_maksim_tomic_day_to_day_2

# lancer le programme
python 001_maksim_football_team_rating.py

"""

# print('Dobar Dan Maksim !')

def evaluate_team(goals_per_match):
    if goals_per_match >= 5:
        return "Excellente équipe"
    elif goals_per_match >= 2:
        return "Meilleure équipe"
    elif goals_per_match >= 1:
        return "Bonne équipe"
    else:
        return "Équipe moyenne ou faible"

# Exemple d'utilisation
goals_per_match = float(input("Entrez la moyenne de buts par match : "))
print(evaluate_team(goals_per_match))

