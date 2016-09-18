# Ask the user to enter the weight of a package
weight = float(input('Enter the weight of a package: '))

# Write an IF-ELIF-ELSE statement
if weight <= 2:
    rate = 1.50
elif weight > 2 and weight <= 6:
    rate = 3.00
elif weight > 6 and weight <= 10:
    rate = 4.00
elif weight > 10:
    rate = 4.75

# Multiply shipping rate by the weight of \
# the package to find the total shipping cost
shipping = rate * weight

print('The total shipping cost is', shipping)
