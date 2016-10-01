# Assign primary colors to corresponding variables
primary_1 = 'red'
primary_2 = 'blue'
primary_3 = 'yellow'


# Ask user to enter the names of two primary colors to mix
x = input('Enter the name of a primary color: ')
y = input('Enter the name of a second primary color: ')

# print ERROR if the colors entered by the user are NOT the
# primary colors
if x != 'red' and x != 'blue' and x != 'yellow':
   print('ERROR')

if y != 'red' and y!= 'blue' and y!= 'yellow':
    print('ERROR')

# Write IF_ELIF_ELSE statement
if (x == 'red' and y == 'blue') or (x == 'blue'and y == 'red'):
    print('Purple')
elif (x == 'red' and y == 'yellow') or (x == 'yellow' and y == 'red'):
    print('Orange')
elif (x == 'blue' and y == 'yellow') or ( x == 'yellow' and y == 'blue'):
    print('Green')
else:
    print('ERROR')
