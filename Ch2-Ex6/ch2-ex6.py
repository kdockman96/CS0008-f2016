# Get the amount of the purchase from the user
purchase = float(input('Enter the amount of the purchase: '))

# Calculate the amount of the state and county sales tax
state_tax = purchase * 0.05
county_tax = purchase * 0.025

# Calculate the total sales tax
sales_tax = state_tax + county_tax

# Calculate tht total of the sale
sale = purchase + sales_tax

# Display the results
print("The amount of the purchase is", purchase)
print('The state sales tax is', state_tax)
print('The county sales tax is', county_tax)
print('The total sales tax is', sales_tax)
print('The total of the sale is', sale)