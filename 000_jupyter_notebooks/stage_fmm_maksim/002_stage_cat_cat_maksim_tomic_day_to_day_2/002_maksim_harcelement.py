# 001_maksim_football_team_rating.py

"""
# chemin
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/000_jupyter_notebooks/stage_fmm_maksim/002_stage_cat_cat_maksim_tomic_day_to_day_2

# lancer le programme
python 002_maksim_harcelement.py

"""

# print('Dobar Dan Maksim !')

def signaler_harcelement(duree_en_semaines):
    if duree_en_semaines == 1:
        return "Parle-en aux surveillants."
    elif 2 <= duree_en_semaines <= 3:
        return "Parle-en à ton professeur principal."
    elif 6 <= duree_en_semaines <= 8:
        return "Parle-en au proviseur."
    else:
        return "Cherche de l'aide immédiatement auprès d'un adulte de confiance."

# Exemple d'utilisation
duree_en_semaines = int(input("Depuis combien de semaines subis-tu du harcèlement ? "))
print(signaler_harcelement(duree_en_semaines))

