# Ask the user to enter the budget for the month
budget = float(input('Enter the amount budgeted for the month: '))


# Initialize an accumulator to keep a running total
total_expenses = 0

# Create a variable that will eventually terminate the loop
keep_going = 'y'

while keep_going == 'y':
    expense = float(input('How much was the expense? $'))
    total_expenses += expense
    keep_going = input('Are there any more expenses? (Enter y for yes.) ')

# Display the amount that the user is over or under budget
if expense < budget:
    difference = format(budget - expense, ',.2f')
    print('You were $', difference, 'under budget.')
elif expense > budget:
    difference = format(budget-expense, ',.2f')
    print('You were $', difference, 'over budget.')
else:
    print('You are on budget.')