# Ask the user to enter an object's mass
mass = float(input("Enter an object's mass:" ))

# Use the following formula to calculate the weight in Newtons
weight = mass * 9.8

# Write IF statement to determine if the weight is too heavy
if weight > 500:
    print('The object is too heavy.')
# Write IF statement to determine if the weight is too light
if weight < 100:
    print('The object is too light.')
