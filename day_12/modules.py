from random import randint, choice, shuffle
from string import ascii_letters

# Day 12: 30 Days of Python Programming

# EXERCISES: LEVEL 1

# Write a function which generates a six digit/character random_user_id
def random_user_id ():
    user_id = list()

    for num in range(0,6):
        rand_int = randint(0,9)
        user_id.append(str(rand_int))

    user_id = ''.join(user_id)
    user_id = int(user_id)
    return user_id

print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated
def user_id_gen_by_user ():
    num_of_chars = int(input('Enter the number of characters: '))
    num_of_ids = int(input('Enter the number of IDs: '))

    user_ids = list()

    for i in range(0, num_of_ids):
        user_id = list()

        for j in range(0, num_of_chars):
            rand_char = choice(ascii_letters)
            user_id.append(str(rand_char))

        user_id = ''.join(user_id)
        user_ids.append(user_id)

    for id in user_ids:
        print(id)

user_id_gen_by_user()

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)
def rgb_color_gen ():
    rgb = list()

    for i in range(0, 3):
        color = randint(0,255)
        rgb.append(str(color))

    return ', '.join(rgb)

print(rgb_color_gen())

# EXERCISES: LEVEL 2

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples)
def list_of_hexa_colors (num):
    codes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    colors = list()

    for i in range(0,num):
        rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
        hex = list()
        
        for j in range(0,3):
            k = rgb[j] // 16
            l = rgb[j] % 16
            hex.append(f'{codes[k]}{codes[l]}')

        colors.append('#' + ''.join(hex))

    return colors

print(list_of_hexa_colors(int(input('Enter a number of hexadecimal colors: '))))

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array
def list_of_rgb_colors (num):
    colors = list()

    for i in range(0,num):
        new_color = (randint(0,255), randint(0,255), randint(0,255))
        colors.append(new_color)

    return colors

print(list_of_rgb_colors(int(input('Enter a number of RGB colors: '))))

# Write a function generate_colors which can generate any number of hexa or rgb colors
def generate_colors (num, type):
    if type == 'hexa':
        return list_of_hexa_colors(num)
    elif type == 'rgb':
        return list_of_rgb_colors(num)
    else:
        return 'Incorrect input'
    
print(generate_colors(int(input('Enter a number of colors: ')), input('Enter a type of color ("hexa" or "rgb"): ')))

# EXERCISES: LEVEL 3

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list (arr):
    new_arr = arr.copy()
    shuffle(new_arr)
    return new_arr

print(shuffle_list([0,1,2,3,4,5]))

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique
def random_numbers ():
    arr = list()

    for i in range(7):
        num = randint(0,9)
        
        while num in arr:
            num = randint(0,9)

        arr.append(num)

    return arr

print(random_numbers())