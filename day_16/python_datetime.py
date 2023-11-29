from datetime import datetime, date

# Day 16: 30 Days of Python Programming

# EXERCISES: LEVEL 1

# Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now.day, now.month, now.year, now.hour, now.minute, now.timestamp())

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
current_date = f'{now.month}/{now.day}/{now.year}, {now.hour}:{now.minute}:{now.second}'
print(current_date)

# Today is 5 December, 2019. Change this time string to time
d = date(2019, 12, 5)
print(d)

# Calculate the time difference between now and new year
today = date(year=now.year, month=now.month, day=now.day)
new_year = date(year=now.year + 1, month=1, day =1)
time_difference = new_year - today
print(f'Time left for new year: {time_difference}')

# Calculate the time difference between 1 January 1970 and now
time_difference = today - date(year=1970, month=1, day=1)
print('Time difference: {}'.format(time_difference))

# Think, what can you use the datetime module for? Examples: 
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog