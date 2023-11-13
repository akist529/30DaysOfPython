# Day 5: 30 Days of Python Programming

# EXERCISES: LEVEL 1

# Declare an empty list
list = list()
print(list)

# Declare a list with more than 5 items
list = [1, 2, 3, 4, 5, 6]
print(list)

# Find the length of your list
print(len(list))

# Get the first item, the middle item and the last item of the list
middle_index = len(list) // 2
print(list[0], list[middle_index], list[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
height = 5 + round(11/12, 2)
mixed_data_types = ['Alex Kist', 30, height, 'Single', '445 W Wellington Ave']
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
middle_index = len(it_companies) // 2
print(it_companies[0], it_companies[middle_index], it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Twitter')
print(it_companies)

# Insert an IT company in the middle of the companies list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Yahoo')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
joined_it_companies = '#;  '.join(it_companies)
print(joined_it_companies)

# Check if a certain company exists in the it_companies list
company_exists = 'Microsoft' in it_companies
print(company_exists)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[3:])

# Slice out the last 3 companies from the list
print(it_companies[0:-3])

# Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
print(it_companies[:middle_index] + it_companies[middle_index + 1:])

# Remove the first IT company from the list
print(it_companies[1:])

# Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
print(it_companies[:middle_index] + it_companies[middle_index + 1:])

# Remove the last IT company from the list
print(it_companies[:-1])

# Remove all IT companies from the list
print(it_companies.clear())

# Destroy the IT companies list
del it_companies

# Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
tech_stack = front_end.copy()
tech_stack.extend(back_end)
print(tech_stack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux
full_stack = tech_stack.copy()
redux_index = full_stack.index('Redux') + 1
full_stack.insert(redux_index, 'Python')
full_stack.insert(redux_index + 1, 'SQL')
print(full_stack)

# EXERCISES: LEVEL 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(min_age, max_age)

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
middle_index = len(ages) // 2
median_age = ages[middle_index]
print(median_age)

# Find the average age (sum of all items divided by their number)
average_age = sum(ages) // len(ages)
print(average_age)

# Find the range of the ages (max minus min)
range = max_age - min_age
print(range)

# Compare the value of (min - average) and (max - average), use abs() method
min_average = abs(min_age - average_age)
max_average = abs(max_age - average_age)
print(abs(max_average - min_average))

# Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

middle_index = len(countries) // 2
print(countries[middle_index])

# Divide the countries list into two equal lists if it is even if not one more country for the first half
is_even = (len(countries) % 2 == 0)

if is_even:
    first_list = countries.copy()
    del first_list[middle_index:]
    second_list = countries.copy()
    del second_list[:middle_index]
    print(first_list, second_list)
else:
    countries.insert(middle_index, 'Wakanda')
    print(countries)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *rest = countries
print(china, russia, usa, rest)