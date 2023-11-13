# Day 7: 30 Days of Python Programming

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# EXERCISES: LEVEL 1

# Find the length of the set it_companies
it_companies_length = len(it_companies)
print(it_companies_length)

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Xerox', 'Sony'])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)

# What is the difference between remove and discard?
# Remove returns an error if the item is not found, discard does not.

# EXERCISES: LEVEL 2

# Join A and B
print(A.union(B))

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
print(A.union(B))
print(B.union(A))

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del A, B

# EXERCISES: LEVEL 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print('List is larger than set: ', len(age) > len(age_set))

# Explain the difference between the following data types: string, list, tuple and set
# A string is a collection of characters. A list is an ordered and mutable collection of data of any types. 
# A tuple is an ordered and immutable collection of data of any types. 
# A set is an unordered and unindexed collection of unique data of any types. 

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words
sentence = 'I am a teacher and I love to inspire and teach people'
unique_words = sentence.split()
unique_words = set(unique_words)
print(unique_words)