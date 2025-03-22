# prompt_trainee_program_3.md


## PROMPT_1
Écris-moi un programme qui dit que une équipe de foot si elle marque un ancien en moyenne elle marque un but par match c'est une bonne équipe si elle est elle marque 2 buts par match en moyenne c'est une meilleure équipe si elle marque plus de 5 buts par match c'est une excellente équipe 

## PROMPT_2
Écris-moi un programme d'un élève qui se fait harceler si il se fait harceler un jour il doit le dire aux surveillants si il se fait harceler entre 2 et 3 semaines, il doit le dire à son professeur principal et s'il se fait harceler entre 6 et 8 semaines mois il doit le dire au proviseur 



## CHATGPT_1
Voici un programme en Python qui prend en entrée la moyenne de buts marqués par match et affiche une évaluation de l'équipe en fonction de cette moyenne :

Ce programme demande à l'utilisateur d'entrer la moyenne de buts par match et affiche l'évaluation correspondante. Tu veux ajouter d'autres critères ou garder ce fonctionnement simple ? 

```python
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
```

## CHATGPT_2
