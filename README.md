# learning_python_for_all


**A set of resources from Books, Exercises, Notebooks to discover and learn Python. It exists both in French and in English.**


## CAUTION
*It is still in WIP, mixing a lot of things, repetition, extract, franglish... a mess, running out of time and unable to delete (FOMO)*


## 1. LEARNING PYTHON WITH JUPYTER NOTEBOOK
**Check the directory `000_jupyter_notebooks` and the readme.**


```bash
# 1. open a terminal console on mac

# 2. go to the directory
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/000_jupyter_notebooks
# You will have to change it e.g. cd /[your-path]//001_python_for_family/

# 3. launch the command below in the console 
jupyter notebook

```

## 2. LEARNING PYTHON

**Check the directory `001_python_for_family` and the readme.**

```bash
# 1. open a terminal console on mac

# 2. go to the directory
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family
# You will have to change it e.g. cd /[your-path]/001_python_for_family/

# 3. launch the command below in the console 

# check python version
python --version

# Launch the script named "002_python_for_family.py" with the python installed by default
python 002_python_for_family.py

# Launch the script named "002_python_for_family.py" with the python version 3 is installed (old mac)
python3 002_python_for_family.py


# go to the readme in 001_python_for_family to have more instructions...

```

## 3. BOOKS TO LEARN PYTHON

- "Python for Teenagers: Learn to Program like a Superhero!" by James R. Payne
- "Python By Example: Learning To Program In 150 Challenges" by Nichola Lacey
- "Python Game Programming By Example" by Alejandro Rodas de Paz, Joseph Howse
- "Automate the Boring Stuff with Python" by Al Sweigart. 


## 4. GIT COMMANDS REMINDER

```bash

# go to the directory
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all

# create the directory
git remote add origin streamlit-sweetviz-pandas-profiling-eda-made-easy

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


# push to github if your branch on github is master
# git push origin master
git push

# Repair Permissions
cd /Users/brunoflaven/Documents/03_git/ia_usages
# groupname is staff on a mac
sudo chgrp -R groupname .
sudo chmod -R g+rwX .
sudo find . -type d -exec chmod g+s '{}' +

# correctio for push
git pull
git branch --set-upstream-to=origin/main main
git pull --allow-unrelated-histories
git push -u origin main

```