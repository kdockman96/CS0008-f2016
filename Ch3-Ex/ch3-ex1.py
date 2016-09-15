# 1 = Monday
# 2 = Tuesday
# 3 = Wednesday
# 4 = Thursday
# 5 = Friday
# 6 = Saturday
# 7 = Sunday

# I am writing the requirements in psuedocode so
# I can better assess what I have to do.

# If the number entered is equal to 1, then display Monday
# Elif, if the number entered is equal to 2, then display Tuesday
# Elif, if the number entered is equal to 3, then display Wednesday
# Elif, if the number entered is equal to 4, then display Thursday
# Elif, if the number entered is equal to 5, then display Friday
# Elif, if the number entered is equal to 6, then display Saturday
# Elif, if the number entered is equal to 7, then display Sunday
# Else, the number is outside of the acceptable range.

# Use the input function to ask user for a number
x = int(input('Enter a number in the range of 1 through 7: '))

# Write IF-ELIF-ELSE statement
if x == 1:
    print('Monday')
elif x == 2:
    print('Tuesday')
elif x == 3:
    print('Wednesday')
elif x == 4:
    print('Thursday')
elif x == 5:
    print('Friday')
elif x == 6:
    print('Saturday')
elif x == 7:
    print('Sunday')
else:
    print('The value is outside the acceptable range.')