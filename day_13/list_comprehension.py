# Day 13: 30 Days of Python Programming

# EXERCISES: LEVEL 1

# Filter only negative and zero in the list using list comprehension
def negative_and_zero (arr):
    lst = [i for i in arr if i <= 0]
    return lst

print(negative_and_zero([-2,-1,0,1,2]))

# Flatten the following list of lists of lists to a one dimensional list
def flatten_lists (arr):
    lst = [element for lst in arr for element in lst]
    return lst

print(flatten_lists([[1,2,3], [4,5,6], [7,8,9]]))

# using list comprehension create the following list of tuples
def list_of_tuples ():
    tuples = [(i, 1, i, i * i, i * i * i, i * i * i * i, i * i * i * i * i) for i in range(0,11)]
    return tuples

print(list_of_tuples())

# Flatten the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

def flatten_countries (arr):
    flat_lst = [element for lst in arr for element in lst]

    for i in range(0, len(flat_lst)):
        flat_lst[i] = list(flat_lst[i])

    for i in range(0, len(flat_lst)):
        for j in range(0, len(flat_lst[i])):
            flat_lst[i][j] = flat_lst[i][j].upper()
        
        flat_lst[i].insert(1, flat_lst[i][0][:3])

    return flat_lst

print(flatten_countries(countries))

# Change the following list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

def list_of_dictionaries (countries):
    dict_lst = list()

    for lst in countries:
        for tuple in lst:
            dict_lst.append({
                'country': tuple[0].upper(),
                'city': tuple[1].upper()
            })

    return dict_lst

print(list_of_dictionaries(countries))

# Change the following list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

list_of_strings = [(element[0] + ' ' + element[1]) for name in names for element in name]

print(list_of_strings)

# Write a lambda function which can solve a slope or y-intercept of linear functions
y = lambda m, x, b: m * x + b
m = lambda x, y, b: (y - b) / x
b = lambda m, x, y: y - (m * x)

print(y(2,4,6))
print(m(2,4,6))
print(b(2,4,6))