# Ask the user to enter the number of coins required \
# to make exactly one dollar.

pennies = int(input('Enter the number of pennies: '))
nickels = int(input('Enter the number of nickels: '))
dimes = int(input('Enter the number of dimes: '))
quarters = int(input('Enter the number of quarters: '))

# Multiply the number of coins entered by the value of
# the coins relative to a dollar
pennies_value = pennies * .01
nickels_value = nickels * .05
dimes_value = dimes * .10
quarters_value = quarters * .25

# Create another variable that adds the values of \
# pennies, nickels, dimes, and quarters to see if the \
# sum equals one dollar exactly
dollar = pennies_value + nickels_value + dimes_value + quarters_value

# Write an IF-ELIF-ELSE statement
if dollar == 1.00:
    print('Congraluations on winning the game!')
elif dollar > 1.00:
    print('The amount entered is more than one dollar.')
else:
    print('The amount entered is less than one dollar.')