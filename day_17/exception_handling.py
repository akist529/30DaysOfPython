# Day 17: 30 Days of Python Programming

# EXERCISES: LEVEL 1

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

# Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively

*nordic_countries, es, ru = names

print('Nordic countries: %s'%(nordic_countries))
print('Estonia: {}'.format(es))
print(f'Russia: {ru}')