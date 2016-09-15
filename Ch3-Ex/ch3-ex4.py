# Ask the user to enter a number within the range of 1 through 10
x = int(input('Enter a number within the range of 1 through 10: '))

# Use psuedocode to write a description of the requirements
# If the number entered is equal to 1, then display the roman numeral I.
# Elif, if the number entered is equal to 2, then display the roman numeral II.
# Elif, if the number entered is equal to 3, then display the roman numeral III.
# Elif, if the number entered is equal to 4, then display the roman numeral IV.
# Elif, if the number entered is equal to 5, then display the roman numeral V.
# Elif, if the number entered is equal to 6, then display the roman numeral VI.
# Elif, if the number entered is equal to 7, then display the roman numeral VII.
# Elif, if the number entered is equal to 8, then display the roman numeral VIII.
# Elif, if the number entered is equal to 9, then display the roman numeral IX.
# Elif, if the number entered is equal to 10, then display the roman numeral X.
# Else, the number is outside of the acceptable range.

# Write an IF-ELIF-ELSE statement
if x == 1:
    print('I')
elif x == 2:
    print('II')
elif x == 3:
    print('III')
elif x == 4:
    print('IV')
elif x == 5:
    print('V')
elif x == 6:
    print('VI')
elif x == 7:
    print('VII')
elif x == 8:
    print("VII")
elif x == 9:
    print('IX')
elif x == 10:
    print('X')
else:
    print('The number is outside of the acceptable range.')


