# Ask the user to enter a nonnegative integer
number = int(input('Enter a nonnegative integer: '))

# Validate the input
if number < 0:
    print('Error')
    number = int(input('Enter a nonnegative integer: '))

keep_going = 'y'

while keep_going == 'y':
