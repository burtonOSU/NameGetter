# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:03:38 2019

@author: Matthew
"""

import requests
from bs4 import BeautifulSoup 

URL = "https://www.fantasynamegenerators.com/orc_names.php"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

names = []

print(soup.find(id="results"))
