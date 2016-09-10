# First get the cost of the meal purchased at the restaurant
food = float(input('What was the cost of the meal? '))

# Get the amount of the sales tax charged
tax = .07 * food

# Add the values of the food and tax together to find the subtotal
sub_total = food + tax

# Calculate the amount of the tip
tip = sub_total * .18

# Calculate the total amount of the meal
total = sub_total + tip

# Display the results, with formatting features for the numbers
print("The charge for the food is ${}". format(food, '.2f'))
print("The tax is: ${}". format(tax, '.2f'))
print("The tip is: ${}". format(tip, '.2f'))
print("The total cost of the meal is: ${}". format(total, '.2f'))



