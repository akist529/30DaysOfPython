# Day 9: 30 Days of Python Programming

# EXERCISES: LEVEL 1

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18 - age} more years to learn to drive.')

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age
my_age = 30
your_age = int(input('Enter your age: '))
if my_age > your_age:
    if my_age - your_age == 1:
        print('I am 1 year older than you.')
    else:
        print(f'I am {my_age - your_age} years older than you.')
elif your_age > my_age:
    if your_age - my_age == 1:
        print('You are 1 year older than me.')
    else:
        print(f'You are {your_age - my_age} years older than me.')
else:
    print('We are the same age.')

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

# EXERCISES: LEVEL 2

# Write a code which gives grade to students according to theirs scores
score = int(input('Enter your score (0 - 100): '))
while score > 100:
    score = int(input('Enter a valid score (0 - 100): '))
if score >= 80:
    print('Your grade is an A. Congratulations!')
elif score >= 70:
    print('Your grade is a B. Well done.')
elif score >= 60:
    print('Your grade is a C. Not bad...')
elif score >= 50:
    print('Your grade is a D. Try harder next time...')
else:
    print('Your grade is an F. You must try harder!')

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input('Enter the current month: ')
if month == 'September' or month == 'October' or month == 'November':
    print('The season is autumn.')
elif month == 'December' or month == 'January' or month == 'February':
    print('The season is winter.')
elif month == 'March' or month == 'April' or month == 'May':
    print('The season is spring.')
elif month == 'June' or month == 'July' or month == 'August':
    print('The season is summer.')
else:
    print('Invalid month.')

# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit = input('Enter a fruit: ')
if fruit in fruits:
    print('That fruit already exists in the list.')
else:
    fruits.append(fruit)
    print(fruits)

# EXERCISES: LEVEL 3

# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Alex',
    'last_name': 'Kist',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list
if 'skills' in person:
    middle_index = len(person['skills']) // 2
    print(person['skills'][middle_index])

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result
if 'skills' in person and 'Python' in person['skills']:
    print('Person is skilled in Python')
else:
    print('Person is not skilled in Python')

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    if len(person['skills']) == 2 and 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('He is a frontend developer.')
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a backend developer.')
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a fullstack developer.')
    else:
        print('Unknown title')
else:
    print('He has no skills.')

# If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if person.get('is_married') == True and person.get('country') == 'Finland':
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.')