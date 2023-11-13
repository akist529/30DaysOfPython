# Day 6: 30 Days of Python Programming

# EXERCISES: LEVEL 1

# Create an empty tuple
new_tuple = tuple()
print(new_tuple)

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Johanna', 'Maddie')
brothers = ('Chase', 'Ben', 'Douglas')
print(sisters, brothers)

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

# How many siblings do you have?
num_of_siblings = len(siblings)
print(num_of_siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings_list = list(siblings)
siblings_list.append('Raymond')
siblings_list.append('Gisela')
family_members = tuple(siblings_list)
print(family_members)

# EXERCISES: LEVEL 2

# Unpack siblings and parents from family_members
johanna, maddie, chase, ben, douglas, raymond, gisela = family_members
print(johanna, maddie, chase, ben, douglas, raymond, gisela)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ('Banana', 'Apple', 'Orange')
vegetables = ('Tomato', 'Cucumber', 'Eggplant')
animal_products = ('Milk', 'Eggs', 'Butter')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
print(food_stuff_lt[:middle_index]+ food_stuff_lt[middle_index + 1:])

# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[3:-3])

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)
# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)