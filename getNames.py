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

tables = soup.find('div', attrs = {'id':'result'})
'''
for row in tables.findAll('div', attrs = {'id':'result'}):
      name = {}
      names.append(name)
'''
print(tables)