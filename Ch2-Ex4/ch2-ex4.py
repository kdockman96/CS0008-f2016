# Get the price of each of the five items
# Display the prices

item1 = float(input('Enter the price of item 1: '))
print('The price of item 1 is $', format(item1, '.2f'), sep='')

item2 = float(input('Enter the price of item 2: '))
print('The price of item 2 is $', format(item2, '.2f'), sep='')

item3 = float(input('Enter the price of item 3: '))
print('The price of item 3 is $', format(item3, '.2f'), sep='')

item4 = float(input('Enter the price of item 4: '))
print('The price of item 4 is $', format(item4, '.2f'), sep='')

item5 = float(input('Enter the price of item 5: '))
print('The price of item 5 is $', format(item5, '.2f'), sep='')

# Display the subtotal of the sale by adding up the prices of the 5 items
subtotal = (item1 + item2 + item3 + item4 + item5)

# Display the sales tax rate
tax_rate = 0.07

# Calculate sales tax on the purchase
tax = tax_rate * subtotal

# Calculate the total amount of the sale
total = tax + subtotal

# Display the results
print('The subtotal of the sale is $', format(subtotal, '.2f'), sep='')
print('The amount of the sales tax is $', format(tax, '.2f'), sep='')
print('The total amount of the sale is $', format(total, '.2f'), sep='')