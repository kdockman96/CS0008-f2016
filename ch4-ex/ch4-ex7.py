# Ask the user for the number of days
days = int(input('Enter the number of days: '))

# Print the table headings
print('Day\t\tSalary')
print('-------------')

# Initialize an accumulator variable
total = 0.01

# Print the days and the salary for each day
for days in range(1, days+1):
    salary = days * 0.01
    print(days, '\t\t', '$', salary, sep='')
    total += salary

# Display the results
print('')
print('The total pay is $', format(total, '.2f'), sep='')