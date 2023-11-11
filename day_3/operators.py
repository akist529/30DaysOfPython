import math

# Day 3: 30 Days of Python Programming

# Declare your age as integer variable
age = 30

# Declare your height as a float variable
height = 5 + (11 / 12)

# Declare a variable that store a complex number
complex = (1 + 2j)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)
base = int(input('Enter the base of the triangle: '))
height = int(input('Enter the height of the triangle: '))
area_of_triangle = (1 / 2) * (base * height)
print('The area of the triangle is ', area_of_triangle)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)
a = int(input('Enter side a of the triangle: '))
b = int(input('Enter side b of the triangle: '))
c = int(input('Enter side c of the triangle: '))
perimeter_of_triangle = a + b + c
print('The perimeter of the triangle is ', perimeter_of_triangle)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length_of_rectangle = int(input('Enter the length of the rectangle: '))
width_of_rectangle = int(input('Enter the width of the rectangle: '))
area_of_rectangle = length_of_rectangle * width_of_rectangle
perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)
print('The area of the rectangle is ', area_of_rectangle)
print('The perimeter of the rectangle is ', perimeter_of_rectangle)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14
radius_of_circle = int(input('Enter the radius of the circle: '))
area_of_circle = math.pi * (radius_of_circle ** 2)
circumference_of_circle = 2 * math.pi * radius_of_circle
print('The area of the circle is ', area_of_circle)
print('The circumference of the circle is ', circumference_of_circle)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
x1 = 0
x2 = 5
y1 = -2
y2 = 8
m1 = (y2 - y1) / (x2 - x1)
x_int = 1
y_int = -2
print('The slope of the line is ', m1)
print('The x-intercept of the line is ', x_int)
print('The y-intercept of the line is ', y_int)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
m2 = (10 - 2) / (6 - 2)
distance = math.sqrt((6 - 2) ** 2 + (10 - 2) ** 2)
print('The slope of the line is ', m2)
print('The euclidean distance of the line is ', distance)

# Compare the slopes in tasks 8 and 9.
print('The difference in slopes is ', m2 - m1)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
y = (3 ** 2) + (6 * 3) + 9
print('The value of y is ', y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement
python_length = len('python')
dragon_length = len('dragon')
print(python_length > dragon_length)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("'on' found in both 'python' and 'dragon': ", 'on' in 'python' and 'on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("'Jargon' in the sentence 'I hope this course is not full of jargon': ", 'jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python
print("'on' in both 'dragon' and 'python': ", 'on' in 'dragon' and 'on' in 'python')

# Find the length of the text python and convert the value to float and convert it to string
python_length = len('python')
python_length = float(python_length)
python_length = str(python_length)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = input('Enter a number: ')
number_is_even = (float(number) % 2) == 0

if number_is_even:
    print('Number is even')
else:
    print('Number is odd')

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print('Floor division of 7 by 3 is equal to the int converted value of 2.7: ', 7 // 3 == int(2.7))

# Check if type of '10' is equal to type of 10
print("Type of '10' is equal to type of 10: ", type('10') == type(10))

# Check if int('9.8') is equal to 10
print("int('9.8') is equal to 10: ", int(9.8) == 10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person
hours = float(input('Enter hours: '))
rate_per_hour = float(input('Enter rate per hour: '))
print('Your weekly earning is ', hours * rate_per_hour)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('Enter number of years you have lived: '))
seconds = years * 365 * 24 * 60 * 60
print('You have lived for ' + str(seconds) + ' seconds')

# Write a Python script that displays the following table
print('1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')