# 000_jupyter_notebooks


**A set of notebooks that mix French and English.**


## 1. LEARNING PYTHON WITH JUPYTER NOTEBOOK

## i. How to Launch a notebook
```bash
# 1. open a terminal console on mac

# 2. go to the directory
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/000_jupyter_notebooks
# You will have to change it e.g. cd /[your-path]//001_python_for_family/

# 3. launch the command below in the console 
jupyter notebook

```



## ii. Use anaconda to manage Python environment

```bash
[env]
# Conda Environment
conda create --name python_begin python=3.9.13
conda info --envs
source activate python_begin
conda deactivate

# if needed to remove
conda env remove -n [NAME_OF_THE_CONDA_ENVIRONMENT]
conda env remove -n python_begin

# update conda 
conda update -n base -c defaults conda

# to export requirements
pip freeze > requirements.txt

# to install
pip install -r requirements.txt


```

## 2. OTHER RESSOURCES
+ Python101 - Intro to Python.ipynb
https://colab.research.google.com/github/explore-ml-iemk/Tutorials-Repo/blob/master/Python%20Tutorial/Python101_Intro_to_Python.ipynb

+ 01.02-Python-Basics.ipynb
https://colab.research.google.com/github/jckantor/CBE30338/blob/master/docs/01.02-Python-Basics.ipynb

+ A collection of Notebooks for using IPython effectively
https://github.com/odewahn/ipynb-examples

+ Python_Basics.ipynb
https://colab.research.google.com/github/saturnaxis/CompPhysics/blob/main/Chapter_2/Python_Basics.ipynb

+ Introduction to Python for Data Sciences
https://github.com/iutzeler/Introduction-to-Python-for-Data-Sciences

+ Python_1.ipynb
https://colab.research.google.com/github/wecacuee/ECE490-Neural-Networks/blob/master/notebooks/01-py-intro/Python_1.ipynb
