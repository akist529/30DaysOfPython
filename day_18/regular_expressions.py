import re
import keyword

# Day 18: 30 Days of Python Programming

# EXERCISES: LEVEL 1

# What is the most frequent word in the following paragraph?

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = paragraph.replace('.', '').split(' ')
word_count = dict()

for word in words:
    if word_count.get(word) != None:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_frequent_word = list(word_count.keys())[0]

for word in list(word_count.keys()):
    if word_count.get(word) > word_count.get(most_frequent_word):
        most_frequent_word = word

print(most_frequent_word,',',word_count.get(most_frequent_word))

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction
# Extract these numbers from this whole text and find the distance between the two furthest particles

text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
pattern = r'-?\d+'
points = re.findall(pattern, text)

print(int(points[len(points) - 1]) - int(points[0]))

# EXERCISES: LEVEL 2

# Write a pattern which identifies if a string is a valid python variable
pattern = r'^[A-Za-z]'
keywords = keyword.kwlist

def is_valid_variable (var):
    if var in keywords:
        return False

    is_valid = re.match(pattern, var, re.I)
    
    if is_valid:
        return True
    else:
        return False

print(is_valid_variable('false'))

# EXERCISES: LEVEL 3

# Clean the following text. After cleaning, count three most frequent words in the string

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean_text = re.sub('%|@|\$|&|#|;|,|\.|\?|!', '', sentence)

def most_frequent_words (text):
    arr = text.split()
    word_count = list()

    for word in set(arr):
        count = len(re.findall(r'\b' + word + r'\b', text, re.I))
        word_count.append((count, word))

    word_count.sort(reverse=True)

    print(set(arr))

    return word_count

print(most_frequent_words(clean_text)[:3])