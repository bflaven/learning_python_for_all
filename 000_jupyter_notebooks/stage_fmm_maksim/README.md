# stage_fmm_maksim


**Une partie des éléments du Stage d'observation du 17 au 21 mars 2025 au sein de France Médias Monde en Français**

_NOTE: Un certain nombre d'éléments ont été anonymisés pour des raisons de confidentialité._


## FICHIERS & RÉPERTOIRES
```bash
001_stage_cat_cat_maksim_tomic_day_to_day_1
002_stage_cat_cat_maksim_tomic_day_to_day_2
003_stage_cat_cat_maksim_tomic_day_to_day_3
004_stage_cat_cat_maksim_tomic_day_to_day_4
005_stage_cat_cat_maksim_tomic_day_to_day_5
README.md
images_generated
programmation_files
```



- 001_stage_cat_cat_maksim_tomic_day_to_day_1 : Programme du jour #1
- 002_stage_cat_cat_maksim_tomic_day_to_day_2 : Programme du jour #2
- 003_stage_cat_cat_maksim_tomic_day_to_day_3 : Programme du jour #3
- 004_stage_cat_cat_maksim_tomic_day_to_day_4 : Programme du jour #4
- 005_stage_cat_cat_maksim_tomic_day_to_day_5 : Programme du jour #5
- README.md : Fichier de présentation
- images_generated : Images générés avec ChatGPT
- programmation_files : Notebook jupyter d'introduction au Python pour les débutants (adolenscents) 


## COMMANDES À RETENIR

- **1. Quelques commandes dans dans la console mac (commandes linux)**

```bash
# few commands in the console
# go to path
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/000_jupyter_notebooks/stage_fmm_maksim/
# where am I ?
pwd
# listing the file
ls -l
```

- **2. Dans la console ou terminal MAC, lancer ou exécuter un script python **
```bash
# Lancer le script python 003_maksim_nba_streamlit.py

# chemin
cd /Users/brunoflaven/Documents/02_copy/stage_cat_cat_maksim_tomic/_stage_cat_cat_maksim_tomic_day_to_day_2/

# lancer le programme
python 003_maksim_nba_streamlit.py
```

- **3. Dans la console ou terminal MAC, lancer ou exécuter un script python  avec Streamlit dedans**
```bash
# Lancer le script python avec Streamlit dedans 004_maksim_balkans_streamlit.py

# chemin
cd /Users/brunoflaven/Documents/02_copy/stage_cat_cat_maksim_tomic/_stage_cat_cat_maksim_tomic_day_to_day_5

# lancer le programme
streamlit run 004_maksim_balkans_streamlit.py
```



- Exemples de webapp construites avec Streamlit : https://streamlit.io/gallery
- Site officiel de Streamlit : https://streamlit.io/

**Streamlit, c'est "koi" ?**

> Streamlit - Un outil de programmation qui permet de transformer facilement des scripts Python en applications web interactives sans avoir besoin de connaître le développement web traditionnel. C'est comme un pont magique entre le code et une interface utilisateur. Avec Streamlit, tu peux créer en quelques lignes de code des applications avec des boutons, des curseurs, des graphiques interactifs et même des cartes. Par exemple, si tu as écrit un programme Python qui analyse des données sportives, Streamlit te permet de le transformer en un site web où les utilisateurs peuvent sélectionner leur équipe préférée via un menu déroulant et voir instantanément les statistiques s'afficher dans un joli graphique. C'est très utilisé par les data scientists et les développeurs qui veulent rapidement partager leurs projets d'analyse de données ou d'intelligence artificielle avec d'autres personnes qui ne savent pas coder. La grande force de Streamlit est sa simplicité : tu peux créer une application web complète en écrivant seulement du Python, sans avoir besoin d'apprendre HTML, CSS ou JavaScript.


- **3. Gérer facilement des environnements en python pour "jouer" avec Streamlit par exemple**

*Utilisation de Anaconda pour gérer les environnements en python*

**Anaconda, c'est "koi" ?**
Anaconda - Une plateforme de distribution gratuite qui regroupe de nombreux outils pour travailler avec Python et R, particulièrement pour les projets scientifiques, l'analyse de données et l'intelligence artificielle. C'est comme une grande boîte à outils déjà prête avec tout ce dont tu as besoin pour commencer à programmer sans avoir à installer chaque outil séparément. Anaconda inclut Python lui-même, plus de 1500 packages (bibliothèques) scientifiques populaires,


- Site officiel de Anaconda : https://www.anaconda.com/

```python
"""
[env]
# Conda Environment
conda create --name nba_app python=3.9.13
conda info --envs
source activate nba_app
conda deactivate


# BURN AFTER READING
source activate nba_app

# if needed to remove
conda env remove -n [NAME_OF_THE_CONDA_ENVIRONMENT]
conda env remove -n nba_app

# install packages
python -m pip install streamlit 
python -m pip install streamlit

# chemin
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/000_jupyter_notebooks/stage_fmm_maksim/002_stage_cat_cat_maksim_tomic_day_to_day_2

# lancer le programme
streamlit run 004_maksim_nba_streamlit.py

"""
```


## VIDÉOS
Coming soon
<!-- 
### Vidéo #1 Stage d'observation du 20 au 22 décembre 2023 au sein de France Médias Monde (Français)

[Vidéo #1 Stage d'observation du 20 au 22 décembre 2023 au sein de France Médias Monde (Français)](https://www.youtube.com/watch?v=h1E_QOrYdHs)[![Vidéo #1 Stage d'observation du 20 au 22 décembre 2023 au sein de France Médias Monde (Français)](explications_segal_1.png)](https://www.youtube.com/watch?v=h1E_QOrYdHs)


 -->
