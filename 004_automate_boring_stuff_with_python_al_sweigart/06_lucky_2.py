#! python3
# lucky.py - Opens several Google search results.

"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/004_automate_boring_stuff_with_python_al_sweigart/


python 06_lucky_2.py

https://beautiful-soup-4.readthedocs.io/en/latest/


conda install -c conda-forge requests
conda install -c conda-forge/label/cf201901 requests
conda install -c conda-forge/label/cf202003 requests

pip install requests
pip install bs4

"""


import requests
from bs4 import BeautifulSoup


# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
URL = 'https://www.monster.fr/emploi/recherche/?q=Coach-de-vie&where=La-Rochelle__2C-Nouvelle__2DAquitaine'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="ResultsContainer")

# print(soup)
print(results.prettify())

# job_elems = results.find_all('section', class_='card-content')
# for job_elem in job_elems:
#     print(job_elem, end='\n'*2)

