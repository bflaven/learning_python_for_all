#! python3
# lucky.py - Opens several Google search results.

"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/004_automate_boring_stuff_with_python_al_sweigart/


python 06_lucky.py

https://beautiful-soup-4.readthedocs.io/en/latest/


conda install -c conda-forge requests
conda install -c conda-forge/label/cf201901 requests
conda install -c conda-forge/label/cf202003 requests

pip install requests
pip install bs4

"""


import requests, sys, webbrowser, bs4
from bs4 import BeautifulSoup


print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
# soup = bs4.BeautifulSoup(res.text, "html.parser")
# Use a parser to fix second error warning
soup = BeautifulSoup(res.text, "html.parser")



# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
