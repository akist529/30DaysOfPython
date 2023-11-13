# Day 8: 30 Days of Python Programming

# Create an empty dictionary called dog
dog = dict()
print(dog)

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Bentley'
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Alex',
    'last_name': 'Kist',
    'gender': 'male',
    'age': 30,
    'marital_status': 'single',
    'skills': ['HTML, CSS, JavaScript, React, Vue, Next.js'],
    'country': 'USA',
    'city': 'Chicago',
    'address': '445 W Wellington Ave'
}

print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].append('Node.js')
student['skills'].append('Express.js')
print(student['skills'])

# Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
student.pop('marital_status')
print(student)

# Delete one of the dictionaries
del student