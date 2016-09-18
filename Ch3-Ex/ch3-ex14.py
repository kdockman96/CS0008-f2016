# Ask the user to enter his or her weight and height
weight = int(input('Enter your weight: '))
height = int(input('Enter your height: '))

# Display BMI
bmi = weight * 703/height**2

print('Your BMI is', bmi)

# Write an IF-ELIF-ELSE statement to determine if the \
# person is underweight, overweight, or at an optimal weight
if bmi < 18.5:
    print('You are considered to be underweight.')
elif bmi >= 18.5 and bmi <= 25:
    print ('Your weight is considered to be optimal.')
else:
    print('You are considered to be overweight.')