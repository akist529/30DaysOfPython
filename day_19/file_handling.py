# Day 19: 30 Days of Python Programming

# EXERCISES: LEVEL 1

# Write a function which count number of lines and number of words in a text.
# All the files are in the data the folder:
    # a) Read obama_speech.txt file and count number of lines and words
    # b) Read michelle_obama_speech.txt file and count number of lines and words
    # c) Read donald_speech.txt file and count number of lines and words
    # d) Read melina_trump_speech.txt file and count number of lines and words

def num_of_lines (file):
    return len(file.readlines())

def num_of_words (file):
    return len(file.read().split(' '))

with open('./obama_speech.txt', 'r') as file:
    print(f'Number of lines in Barack Obama speech: {num_of_lines(file)}')
    file.seek(0)
    print(f'Number of words in Barack Obama speech: {num_of_words(file)}')

with open('./michelle_obama_speech.txt', 'r') as file:
    print(f'Number of lines in Michelle Obama speech: {num_of_lines(file)}')
    file.seek(0)
    print(f'Number of words in Michelle Obama speech: {num_of_words(file)}')

with open('./donald_speech.txt', 'r') as file:
    print(f'Number of lines in Donald Trump speech: {num_of_lines(file)}')
    file.seek(0)
    print(f'Number of words in Donald Trump speech: {num_of_words(file)}')

with open('./melania_trump_speech.txt', 'r') as file:
    print(f'Number of lines in Melania Trump speech: {num_of_lines(file)}')
    file.seek(0)
    print(f'Number of words in Melania Trump speech: {num_of_words(file)}')

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

import json
import re

def most_spoken_languages (data):
    language_count = list()

    lst = [country['languages'] for country in data]
    flat_lst = [i for g in lst for i in g]
    flat_set = set(flat_lst)

    for language in flat_set:
        count = flat_lst.count(language)
        language_count.append((count, language))

    language_count.sort(key=lambda x: x[0], reverse=True)
    return language_count[:10]

with open('./countries_data.json') as file:
    data = json.load(file)
    print(most_spoken_languages(data))

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

def most_populated_countries (data):
    sorted_data = sorted(data, key=lambda x: x['population'], reverse=True)[:10]
    countries = list()

    for country in sorted_data:
        countries.append({
            'name': country['name'],
            'population': country['population']
        })

    return countries

with open('./countries_data.json') as file:
    data = json.load(file)
    print(most_populated_countries(data))

# EXERCISES: LEVEL 2

# Extract all incoming email addresses as a list from the email_exchange_big.txt file
def extract_addresses (file):
    text = file.readlines()
    filtered = filter(lambda x: re.match('^From', x), text)
    addresses = list()

    for line in filtered:
        arr = line.split()
        addresses.append(arr[1])

    return list(set(addresses))


with open('./email_exchanges_big.txt', 'r') as file:
    print(extract_addresses(file))

# Find the most common words in the English language
# Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words
# Your function will return an array of tuples in descending order. Check the output

most_common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def find_most_common_words (string, number):
    arr = string.split()
    words = [(len(re.findall(word, string)), word) for word in set(arr)]
    words.sort(key=lambda x: x[0], reverse=True)
    return words[:number]

print(find_most_common_words('How much wood could a wood chuck chuck if a wood chuck could chuck wood', 5))

# Use the function, find_most_frequent_words to find:
# a) The ten most frequent words used in Obama's speech
# b) The ten most frequent words used in Michelle's speech
# c) The ten most frequent words used in Trump's speech
# d) The ten most frequent words used in Melina's speech

def find_most_frequent_words (text):
    clean_text = re.sub(r'[!-\/:-@[-`{-~]', '', text)
    clean_text = clean_text.lower()
    arr = clean_text.split()
    words = [(len(re.findall(word, text)), word) for word in set(arr)]
    words.sort(key=lambda x: x[0], reverse=True)
    return words[:10]

with open('./obama_speech.txt', 'r') as file:
    text = file.read()
    print('Most frequent words in Barack Obama speech: ', find_most_frequent_words(text))

with open('./michelle_obama_speech.txt', 'r') as file:
    text = file.read()
    print('Most frequent words in Michelle Obama speech: ', find_most_frequent_words(text))

with open('./donald_speech.txt', 'r') as file:
    text = file.read()
    print('Most frequent words in Donald Trump speech: ', find_most_frequent_words(text))

with open('./melania_trump_speech.txt', 'r') as file:
    text = file.read()
    print('Most frequent words in Melania Trump speech: ', find_most_frequent_words(text))

# Write a python application that checks similarity between two texts
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts
# For instance check the similarity between the transcripts of Michelle's and Melina's speech
# You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity)
# List of stop words are in the data directory

def get_clean_text (text):
    return re.sub(r'[!-\/:-@[-`{-~]', '', text)

def filter_word (word):
    stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    
    if word in stop_words:
        return False
    else:
        return True

def remove_support_words (text):
    arr = text.split()
    filtered_text = filter(filter_word, arr)

    return ' '.join(filtered_text)

def check_text_similarity (text_one, text_two):
    clean_text_one = get_clean_text(text_one)
    clean_text_two = get_clean_text(text_two)

    stripped_text_one = remove_support_words(clean_text_one)
    stripped_text_two = remove_support_words(clean_text_two)
    
    print('Number of words in first file: ', len(stripped_text_one.split()))
    print('Number of words in second file: ', len(stripped_text_two.split()))

with open('./donald_speech.txt', 'r') as file_one:
    with open('./obama_speech.txt', 'r') as file_two:
        text_one = file_one.read()
        text_two = file_two.read()
        check_text_similarity(text_one, text_two)

# Find the 10 most repeated words in the romeo_and_juliet.txt

def most_repeated_words (file):
    text = file.read()
    clean_text = re.sub(r'[0-9!-\/:-@[-`{-~]', '', text)
    clean_text = remove_support_words(clean_text)
    all_words = clean_text.split()
    words = set(map(lambda x: x.lower(), all_words))
    words = filter(lambda x: len(x) > 1, words)
    word_count = [(len(re.findall(word, clean_text)), word) for word in words]
    word_count.sort(key=lambda x: x[0], reverse=True)

    return word_count[:10]
    

with open('./romeo_and_juliet.txt', 'r') as file:
    print(most_repeated_words(file))

# Read the hacker news csv file and find out:
    # a) Count the number of lines containing python or Python
    # b) Count the number lines containing JavaScript, javascript or Javascript
    # c) Count the number lines containing Java and not JavaScript

def strings_in_line (line, strs):
    for string in strs:
        if string in line:
            return True
    
    return False

def strings_not_in_line (line, strs):
    for string in strs:
        if string in line:
            return False
        
    return True

def num_of_lines_with_string (file, good_strs, bad_strs):
    lines = file.readlines()
    lines_with_string = filter(lambda line: strings_in_line(line, good_strs) and strings_not_in_line(line, bad_strs), lines)
    num = len(list(lines_with_string))
    return num

with open('./hacker_news.csv', 'r') as file:
    print('Number of lines containing python or Python: ', num_of_lines_with_string(file, ['python', 'Python'], []))
    file.seek(0)
    print('Number of lines containing JavaScript, javascript, or Javascript: ', num_of_lines_with_string(file, ['JavaScript', 'javascript', 'Javascript'], []))
    file.seek(0)
    print('Number of lines containing Java and not JavaScript: ', num_of_lines_with_string(file, ['Java'], ['JavaScript']))