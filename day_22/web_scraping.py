# Day 22: 30 Days of Python Programming

import re
import requests as req
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/datasets'

res = req.get(url)
content = res.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(res.status_code)

tables = soup.find_all('table', { 'cellpadding': '3' })

if (tables):
    table = tables[0]

    for td in table.find('tr').find_all('td'):
        print(td.text)

# EXERCISES: LEVEL 1

# Scrape the following website and store the data as json file
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

res = req.get(url)
content = res.content
soup = BeautifulSoup(content, 'html.parser')

# Extract the table in this url and change it to a json file
url = 'https://archive.ics.uci.edu/dataset/45/heart+disease'

res = req.get(url)
content = res.content
soup = BeautifulSoup(content, 'html.parser')

headers = soup.find_all('th')
headers = [header.get_text() for header in headers]

rows = soup.find_all('tr')[1:] # skip first row which contains headers
rows = [row.find_all('td') for row in rows]
rows = [[element.get_text() for element in row] for row in rows]

data = list()

for row in rows:
    json = dict()

    for (index, header) in enumerate(headers):
        json[header] = row[index]

    data.append(json)

# Scrape the presidents table and store the data as json
# The table is not very structured and the scrapping may take very long time
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

res = req.get(url)
content = res.content
soup = BeautifulSoup(content, 'html.parser')
table = soup.body.find('table', { 'class': 'wikitable' })
headers = table.find_all('th')[:7]

for i in range(0, len(headers)):
    if headers[i].find('abbr'):
        headers[i] = headers[i].find('abbr').text
    else:
        headers[i] = headers[i].text

    headers[i] = re.sub(r'[\n]', '', headers[i])
    headers[i] = headers[i].split('[')[0]
    headers[i] = headers[i].split('(')[0]

headers.remove('Portrait')

class President:
    def __init__ (self, number, name, term, party, election, vp):
        self.number = number
        self.name = name
        self.term = term
        self.party = party
        self.election = election
        self.vp = vp

numbers = [tr.find('th') for tr in table.find('tbody').find_all('tr')]
numbers = [number.find('a').text for number in numbers][1:]

names = list()
terms = list()
parties = list()
elections = list()
vps = list()

[tr.find_all('td') for tr in table.find('tbody').find_all('tr')]

for row in table.find('tbody').find_all('tr'):
    if (row.find('td')):
        data = row.find_all('td')

        name = data[1]
        name = name.find('a').text
        names.append(name)

        term = data[2].text
        term = re.sub('\n', '', term)
        term = term.split('[')[0]
        terms.append(term)

        party = data[4].text
        party = re.sub('\n', '', party)
        parties.append(party)

        election = data[5].text
        election = re.sub('\n', '', election)
        elections.append(election)

        vp = data[6].text
        vp = re.sub('\n', '', vp)
        vps.append(vp)

presidents = list()

for (index, number) in enumerate(numbers):
    president = President(number, names[index], terms[index], parties[index], elections[index], vps[index])
    presidents.append(president)

for president in presidents:
    print(president.number, president.name, president.term, president.party, president.election, president.vp)