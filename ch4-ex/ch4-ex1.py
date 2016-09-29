days = 5

# initialize an accumulator variable
total = 0

# Ask the user for the number of bugs collected each day
# for 5 days
for days in range(days):
    bugs = int(input('Number of bugs collected today: '))
    total += bugs

# Display the total number of bugs collected
print('The total number of bugs collected ' + \
      'over five days is', total, 'bugs.')