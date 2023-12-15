# learning_python_for_all


**A set of resources from Books, Exercises, Notebooks to discover and learn Python. It exists both in French and in English.**


## CAUTION
*It is still in WIP, mixing a lot of things, repetition, extract, franglish... a mess, running out of time and unable to delete (FOMO)*


## DIRECTORIES DESCRIPTION

**What you will find in these directories....**

- **000_jupyter_notebooks:** Some notebooks to allow children (from 7 years old) or teenagers, or even seniors, to learn about programming. These elements were collected in particular to keep trainees occupied during their discovery internships in a professional environment. The vocation is for them to be autonomous and to produce visible results. It is therefore a very result-oriented initiation, favoring immediacy and practice, very little theoretical. Check 001_notebook_beginner_fr_learn_python.ipynb that is written with the help Mistral and ChatGPT.

- **001_python_crash_course_eric_matthes:** Summary and extract from the book `Python Crash Course, A Hands-On, Project-Based Introduction to Programming` by by Eric Matthes


- **002_python_for_teenagers_superhero_james_r_payne:** Summary and extract from the book `Python for Teenagers: Learn to Program like a Superhero!` by James R. Payne

- **003_code_for_family_lesson:** My own modest stuff with some examples of Python Scripts.

- **004_automate_boring_stuff_with_python_al_sweigart:** Summary and extract from the book `Automate the Boring Stuff with Python` by Al Sweigart. Great book full of practical examples.

- **005_python_by_example_150_challenges_nichola_lacey:** Summary and extract from the book `Python By Example: Learning To Program In 150 Challenges` by Nichola Lacey


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
```bash
https://link.springer.com/book/10.1007/978-1-4842-9988-3
```

- "Python By Example: Learning To Program In 150 Challenges" by Nichola Lacey
```bash
https://www.abebooks.com/9781108716833/Python-Example-Learning-Program-150-1108716830/plp
```


- "Python Game Programming By Example" by Alejandro Rodas de Paz, Joseph Howse

```bash
https://www.oreilly.com/library/view/python-game-programming/9781785281532/
```


- "Automate the Boring Stuff with Python" by Al Sweigart. 
```bash
https://automatetheboringstuff.com/
```



- "Python Crash Course, A Hands-On, Project-Based Introduction to Programming" by Eric Matthes

```bash
https://ehmatthes.github.io/pcc_3e/
https://nostarch.com/python-crash-course-3rd-edition
```



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
# git push
git push -u origin main
# git push origin master


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

## 6. PROMPTING STUFF


**Product of my experience, every time you see in title or description the verbs: `Unleash`, `Harnessing`, `Supercharge`... I am sure that is has been generated by ChatGPT or any other IA!**

```bash
# Some title extracted from YouTube, certainly generated by an IA

# search for "Unleash Code"
# search for "Harnessing Code"
# search for "Supercharge Code"

Unleash the power of Atlas.ti with AI code generation: A step-by-step guide
Unleash Code LLAMA to Generate and Explain Code in Any Language!
Unleash the POWER of Windows WSL! Master Linux Like a PRO
Defining the future: Harnessing generative AI for low-code automation
Supercharge Your Code: Harnessing the Potential of Methods and Functions

# to be continued

```

**PROMPT_1:**

```bash
Generate a sexy text to present a set of jupyter notebooks for teenagers and kids on how to start learning Python`
```
**OUTPUT_PROMPT_1:**

🔥 Unleash the Python Passion: Dive into the World of Code with These Sizzling Jupyter Notebooks! 🔥

Hey future Pythonistas! 🚀 Ready to embark on an electrifying journey into the magical realm of coding? 🌟 Our collection of Jupyter Notebooks is here to make learning Python as thrilling as a rollercoaster ride!

🎉 Python Playtime: Unwrap the Gift of Code! 🎉

🚀 **Notebook 1: Python's Secret Language Unveiled!**
   - Crack the code and unlock Python's secrets! 🕵️‍♂️
   - Learn the basics with fun games and mind-bending puzzles! 🧩

🌈 **Notebook 2: The Art of Pythonic Spells**
   - Cast enchanting spells with Python's sleek syntax! 🧙‍♂️✨
   - Dive into creative coding and craft your own digital masterpieces! 🎨🚀

🤖 **Notebook 3: Meet Python's Robot Sidekicks**
   - Build your own virtual robot army with Python! 🤖💻
   - Command your creations to perform awesome tasks and conquer challenges! 🚀🔧

🔮 **Notebook 4: Python Potions for Game Wizards**
   - Brew your own Python potions and conjure up cool games! 🎮🔮
   - Become a gaming wizard with hands-on projects and interactive challenges! 🚀🕹️

🌐 **Notebook 5: Python Voyagers in Cyber Space**
   - Soar through cyberspace and explore the wonders of Python web development! 🌐💻
   - Design your own websites and launch them into the digital universe! 🚀🚀

Get ready to turn your coding dreams into reality, ignite your creativity, and blaze a trail into the exciting world of Python! 🔥🚀

💻 Unlock the power of Python, one notebook at a time! Are you ready for the coding adventure of a lifetime? Let's make Python sizzle! 🔥💻 #CodeCrush #PythonPassion #JupyterJamboree 🚀💻