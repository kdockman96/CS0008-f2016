# This program gets the projected amount of total sales and
# calculates the profit made from that amount, which is
# 23% of total sales.

# Get the projected amount of total sales
total_sales = float(input("Enter the projected amount of total sales: "))

# Calculate the profit made from that amount
profit = total_sales * 0.23

# Display the profit made
print('The profit made from projected total sales is', format(profit,',.2f'))

