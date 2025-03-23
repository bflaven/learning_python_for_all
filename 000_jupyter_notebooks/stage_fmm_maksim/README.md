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
# listing the files in the directory
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
Anaconda - Une plateforme de distribution gratuite qui regroupe de nombreux outils pour travailler avec Python et R, particulièrement pour les projets scientifiques, l'analyse de données et l'intelligence artificielle. C'est comme une grande boîte à outils déjà prête avec tout ce dont tu as besoin pour commencer à programmer sans avoir à installer chaque outil séparément. Anaconda inclut Python lui-même, plus de 1500 packages (bibliothèques) scientifiques populaires, et des applications comme Jupyter Notebook qui te permettent d'écrire et d'exécuter du code de façon interactive. Un des grands avantages d'Anaconda est sa gestion des "environnements", qui te permet de créer des espaces isolés pour différents projets avec leurs propres versions de packages, évitant ainsi les conflits entre tes différents programmes. C'est très utilisé par les étudiants, les chercheurs et les professionnels dans les domaines de la science des données, l'apprentissage automatique et la visualisation de données.


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


- **4. Gérer localemnt des LLM avec Ollama**

*Utilisation de Anaconda pour gérer les environnements en python*

**Anaconda, c'est "koi" ?**
Ollama - Un logiciel gratuit et open-source qui te permet d'installer et d'utiliser différents modèles d'intelligence artificielle directement sur ton propre ordinateur, au lieu de passer par internet. C'est comme avoir ton propre assistant IA personnel qui fonctionne même sans connexion internet. Ollama te donne accès à plusieurs modèles IA comme Llama, Mistral ou Gemma que tu peux télécharger facilement avec une simple commande. L'avantage principal d'Ollama est la confidentialité : tes conversations et tes données restent sur ton ordinateur et ne sont pas envoyées vers des serveurs externes. C'est aussi pratique pour les développeurs qui veulent expérimenter avec l'IA sans payer d'abonnement à des services en ligne. Par contre, comme ces modèles fonctionnent sur ton propre matériel, ils sont généralement moins puissants que les versions en ligne comme ChatGPT ou Claude, surtout si ton ordinateur n'est pas très récent ou n'a pas de carte graphique performante.


``` bash
# utiliser mistral en local
ollama list
ollama run mistral:latest
```


```bash
# To run and chat with Llama 2
ollama run llama2
ollama run codellama:7b



# To run and chat with orca-mini
ollama run orca-mini
ollama pull orca-mini
ollama run codellama:7b

# remove a model
ollama rm llama2
ollama rm orca-mini
ollama rm codellama:7b
ollama rm codellama:7b-python


# list the model
ollama list


# when you are in the model you can use
>>> /?
>>> /list
>>> /set verbose

# to get out from the model
/exit
```



- Site officiel ollama : https://ollama.com/
- Github ollama : https://github.com/ollama/ollama


## VIDÉOS
Coming soon
<!-- 
### Vidéo #1 Stage d'observation du 20 au 22 décembre 2023 au sein de France Médias Monde (Français)

[Vidéo #1 Stage d'observation du 20 au 22 décembre 2023 au sein de France Médias Monde (Français)](https://www.youtube.com/watch?v=h1E_QOrYdHs)[![Vidéo #1 Stage d'observation du 20 au 22 décembre 2023 au sein de France Médias Monde (Français)](explications_segal_1.png)](https://www.youtube.com/watch?v=h1E_QOrYdHs)


 -->

## GIT COMMANDS REMINDER

```bash

# go to the directory
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/000_jupyter_notebooks

# know your branch
git branch


# check for status
git status


# for any change just type this command
git add .

# add a commit with a message
git commit -am "add usecase"
git commit -am "add files"
git commit -am "update files"
git commit -am "update readme"
git commit -am "add files and update readme"
git commit -am "add to .svg the Musk\'s Favorite Letter X"
git commit -am "add .gitignore"
git commit -am "add docker files"
git commit -am "updates files maksim"


# push to github if your branch on github is master
# git push origin master
git push
# git push -u origin main
# git push origin master

```