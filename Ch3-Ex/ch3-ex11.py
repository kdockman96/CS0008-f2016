# Ask the user to enter the number of books purchased
books = int(input('Enter the number of books purchased: '))

# Write an IF-ELIF-ELSE statement, but an else statement \
# is not needed in this situation
if books == 0:
    print('No points are awarded.')
elif books == 2:
    print('5 points are awarded.')
elif books == 4:
    print('15 points are awarded.')
elif books == 6:
    print('30 points are awarded.')
elif books >= 8:
    print('60 points are awarded.')