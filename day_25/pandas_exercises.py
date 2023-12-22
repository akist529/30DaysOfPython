# Day 25: 30 Days of Python Programming

import pandas as pd

# EXERCISES: LEVEL 1

# Read the hacker_news.csv file from data directory

df = pd.read_csv('hacker_news.csv')

# Get the first five rows

dh = df.head()

# Get the last five rows

dt = df.tail()

# Get the title column as pandas series

titles = df['title']

# Count the number of rows and columns 

rows = df.shape[0]
cols = df.shape[1]

# Filter the titles which contain python

python_titles = list(filter(lambda x: 'python' in x.lower(), titles))

# Filter the titles which contain JavaScript

javascript_titles = list(filter(lambda x: 'javascript' in x.lower(), titles))

# Explore the data and make sense of it