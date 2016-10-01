# Initialize an accumulator variable
total = 0.0

# Ask the user to enter a series of positive numbers
positive_num = float(input('Enter a positive number: '))

# Create a while loop to keep a running total of positive numbers
# If the number entered is negative, the loop terminates
while positive_num > 0:
    total += positive_num
    print('The total is', format(total, '.2f'))
    positive_num = float(input('Enter another positive number: '))