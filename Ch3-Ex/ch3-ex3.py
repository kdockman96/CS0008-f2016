# Ask the user to enter an age
x = int(input('Enter an age: '))

# Determine whether the age entered falls into the following age ranges
# based on the guidelines given
infant_age = 1
child_age = 13
teenager_age = 20
adult_age = 20

# Write an IF-ELIF-ELSE statement for the age ranges
if x <= 1:
    print('The person is an infant.')
elif 1 < x < 13:
    print('The person is a child.')
elif 13 <= x < 20:
    print('The person is a teenager.')
else:
    print('The person is an adult.')
