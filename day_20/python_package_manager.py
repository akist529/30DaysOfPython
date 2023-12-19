# Day 20: 30 Days of Python Programming

import numpy, re, json, functools

print(numpy.version.version)

lst = [1, 2, 3, 4, 5]

np_arr = numpy.array(lst)
print(np_arr)

print(len(np_arr))

np_arr * 2

np_arr + 2

print(np_arr)

import pandas

import webbrowser

url_lists = [

]

for url in url_lists:
    webbrowser.open_new_tab(url)

import requests

url = 'https://www.google.com' 

response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
print(response.text)

from mypackage import arithmetics

print(arithmetics.add_numbers(1, 2, 3, 4, 5))

from mypackage import greet

print(greet.greet_person('Alex', 'Kist'))

# EXERCISES: LEVEL 1

# Read this url and find the 10 most frequent words. moby_dick = 'https://www.gutenberg.org/cache/epub/2701/pg2701.txt'

# moby_dick = 'https://www.gutenberg.org/cache/epub/2701/pg2701.txt'
# response = requests.get(moby_dick)
# text = response.text
# clean_text = re.sub(r'[!-\/:-@[-`{-~]', '', text)
# clean_text = clean_text.lower()
# arr = clean_text.split()
# words = [(len(re.findall(word, clean_text)), word) for word in set(arr)]
# words.sort(key=lambda x: x[0], reverse=True)
# print(words[:10])

# Find the min, max, mean, median, standard deviation of cats' weight in metric units

cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
data = response.json()

weights = [cat['weight']['metric'] for cat in data]
mean_weights = list()

for weight in weights:
    min_weight = int(weight.split(' ')[0])
    max_weight = int(weight.split(' ')[len(weight.split(' ')) - 1])
    mean_weights.append((min_weight + max_weight) / 2)

mean_weights.sort()

def get_min_weight ():
    min_weights = [weight.split(' ')[0] for weight in weights]
    min_weights.sort()
    return min_weights[0]

def get_max_weight ():
    max_weights = [weight.split(' ')[len(weight.split(' ')) - 1] for weight in weights]
    max_weights.sort(reverse=True)
    return max_weights[0]

def get_mean_weight ():
    total_weight = functools.reduce(lambda x, y: x + y, mean_weights)

    return total_weight / len(weights)

def get_median_weight ():
    middle_index = len(weights) // 2

    return mean_weights[middle_index]

def get_stddev_weight ():
    return numpy.std(mean_weights)

print('Minimum weight of a cat: ', get_min_weight())
print('Maximum weight of a cat: ', get_max_weight())
print('Mean weight of a cat: ', get_mean_weight())
print('Median weight of a cat: ', get_median_weight())
print('Standard deviation of a cat\'s weight: ', get_stddev_weight())

# Find the min, max, mean, median, standard deviation of cats' lifespan in years

lifespans = [cat['life_span'] for cat in data]

mean_lifespans = list()

for lifespan in lifespans:
    min_lifespan = int(lifespan.split(' ')[0])
    max_lifespan = int(lifespan.split(' ')[len(lifespan.split(' ')) - 1])
    mean_lifespans.append(max_lifespan - min_lifespan / 2)

mean_lifespans.sort()

def get_min_lifespan ():
    min_lifespans = [int(lifespan.split(' ')[0]) for lifespan in lifespans]
    min_lifespans.sort()
    return min_lifespans[0]

def get_max_lifespan ():
    max_lifespans = [int(lifespan.split(' ')[len(lifespan.split(' ')) - 1]) for lifespan in lifespans]
    max_lifespans.sort(reverse=True)
    return max_lifespans[0]

def get_mean_lifespan ():
    total_lifespans = functools.reduce(lambda x, y: x + y, mean_lifespans)
    
    return total_lifespans / len(mean_lifespans)

def get_median_lifespan ():
    middle_index = len(lifespans) // 2

    return mean_lifespans[middle_index]

def get_stddev_lifespan ():
    return numpy.std(mean_lifespans)

print('Minimum lifespan of a cat: ', get_min_lifespan())
print('Maximum lifespan of a cat: ', get_max_lifespan())
print('Mean lifespan of a cat: ', get_mean_lifespan())
print('Median lifespan of a cat: ', get_median_lifespan())
print('Standard deviation of a cat\'s lifespan: ', get_stddev_lifespan())

# Create a frequency table of country and breed of cats

countries = numpy.array([cat['country_code'] for cat in data])
unique, counts = numpy.unique(countries, return_counts=True)
print(numpy.asarray((unique, counts)).T)

breeds = numpy.array([cat['name'] for cat in data])
unique, counts = numpy.unique(breeds, return_counts=True)
print(numpy.asarray((unique, counts)).T)