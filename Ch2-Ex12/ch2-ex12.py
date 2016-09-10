# Create a variable showing the amount of shares purchased
shares_bought = 2000 * 40

# Find the commission paid to the stockbroker
# after he bought the shares
c_bought = .03 * shares_bought

# Create a variable showing the amount of shares sold
shares_sold = 2000 * 42.75

# Find the commission paid to the stockbroker after
# he sold the shares
c_sold = .03 * shares_sold

# Find the difference between the amount he paid for
# the stock and the amount he sold the stock for
total_amount = shares_sold - shares_bought

# Find the total amount of the commission
total_com = c_bought + c_sold

# Find the difference between total amount of shares
# and total commission to see if he made a profit
profit = total_amount - total_com

# Display the results
print('The amount of money Joe paid for stock is $',shares_bought)
print('The amount of commission Joe paid his broker' \
      'when he bought the stock is $', c_bought)
print('The amount that Joe sold the stock for is $', shares_sold)
print('The amount of commission Joe paid his broker' \
      'when he sold the stock is $', c_sold)
print('The profit that Joe made is $', profit)


