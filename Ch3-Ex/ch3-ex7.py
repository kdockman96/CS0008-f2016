# Assign primary colors to corresponding variables
primary_1 = 'red'
primary_2 = 'blue'
primary_3 = 'yellow'

# Assign secondary colors to corresponding variables
purple = primary_1 + primary_2
orange = primary_1 + primary_3
green = primary_2 + primary_3

# Ask user to enter the names of two primary colors to mix
x = input('Enter the names of two primary colors to mix: ')

# Write IF_ELIF_ELSE statement
if x == primary_1 and x == primary_2:
    print('Purple')
elif x == primary_1 and x == primary_3:
    print('Orange')
elif x == primary_2 and x == primary_3:
    print('Green')
else:
    print('ERROR')



