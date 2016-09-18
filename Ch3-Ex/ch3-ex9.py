# Ask the user for a number and convert the input to an integer
number = input('Give me the number: ')
number = int(number)

# Test to see if number is in the range or outside the range
if number >= 0 and number <= 36:
    print('The number is in the acceptable range.')
if number < 0 or number > 36:
    print('GIVE ME A NUMBER!')

if number == 0:
    color = "green"
elif (number >= 1 and number <= 10) \
        or \
     (number >= 19 and number <= 28):
    if number % 2 == 0:
        color = "black"
    else:
        color = "red"
elif number >= 11 and number <= 18:
    if number % 2 == 0:
        color = "red"
    else:
        color = "black"
print('Your color is', color)


# (number >= 1 and number <= 10) \
# OR \
# (number >= 19 and number <= 28)
# or is executed after first condition is tested