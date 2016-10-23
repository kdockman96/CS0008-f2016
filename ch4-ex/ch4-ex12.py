# Ask the user for the starting number of organisms
organisms = int(input('Enter the starting number of organisms: '))

# As the user the average daily population increase as a percentage
daily_pop_increase = float(input('Enter the average daily population increase as a decimal: '))

if daily_pop_increase < 0 or daily_pop_increase > 1:
    print('Error')
    daily_pop_increase = float(input('Enter the correct population increase as a decimal: '))

# Ask the user what the number of days the organisms will be left to multiply will be
days_multiply = int(input('Enter the number of days to multiply: '))

# Create a variable that references a Boolean value
first = True

# display table headings
print('')
print('Day Approximate\tPopulation')

# Write a for loop with an if statement and running total
# Display the results
for days_multiply in range(organisms, days_multiply + 1):
    if first:
        print(1, '\t\t\t\t', organisms)
        first = False
    add = organisms * daily_pop_increase
    organisms += add
    print(days_multiply, format(organisms, '20.3f'))



