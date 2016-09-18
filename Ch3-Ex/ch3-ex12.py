# Ask the user to enter the number of packages purchased
packages = int(input('Enter the number of packages purchased: '))

price = 99.00

# Write an IF-ELIF-ELSE statement
if packages >= 10 and packages <= 19:
    discount = .10 * price
elif packages >= 20 and packages <= 49:
    discount = .20 * price
elif packages >= 50 and packages <= 99:
    discount = .30 * price
elif packages >= 100:
    discount = .40 * price
else:
    print('There is no quantity discount.')

# Subtract the discount from the sales price
purchase = price - discount

#Display the results
print('The amount of the discount is ${}'. format(discount, '.2f'))
print('The total amount of the purchase is $', purchase)
