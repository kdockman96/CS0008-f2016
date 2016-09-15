# Ask the user to enter a month, day, and two-digit year,
# in numeric form
month = int(input('Enter a month in numeric form: '))
day = int(input('Enter a day: '))
year = int(input('Enter a two-digit year: '))

# Determine whether the month times the day equals the year,
# using an IF-ELSE statement
if year == month * day:
    print('The date is magic!')
else:
    print('The date is not magic.')