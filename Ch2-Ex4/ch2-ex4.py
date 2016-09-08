# Get the price of each of the five items
# Display the prices

item1 = input('Enter the price of item 1: ')
print('The price of item 1 is', item1)

item2 = input('Enter the price of item 2: ')
print('The price of item 2 is', item2)

item3 = input('Enter the price of item 3: ')
print('The price of item 3 is', item3)

item4 = input('Enter the price of item 4: ')
print('The price of item 4 is', item4)

item5 = input('Enter the price of item 5: ')
print('The price of item 5 is', item5)

# Display the subtotal of the sale by adding up the prices of the 5 items
subtotal = (item1 + item2 + item3 + item4 + item5)

# Display the sales tax rate
tax_rate = 0.07

# Calculate sales tax on the purchase
tax = tax_rate * subtotal

# Calculate the total amount of the sale
total = tax + subtotal

# Display the results
print('The subtotal of the sale is', subtotal)
print('The amount of the sales tax is', tax)
print('The total amount of the sale is', total)