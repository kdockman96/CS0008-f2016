# Variables need to be created to reference total rainfall, monthly rainfall,
# average rainfall, the number of years, and the total number of months
total_rainfall = 0.0
monthly_rainfall = 0.0
average_rainfall = 0.0
years = 0
total_months = 0

# Ask the user for the number of years
years = int(input('Enter the number of years: '))

# Write a for loop and incorporate an accumulator variable to keep a running total
for years in range(years):
    print('For year:', years + 1)
    for month in range(12):
        monthly_rainfall = float(input('Enter the inches of rainfall for the month: '))
        total_months += 1
        # Add to the total rainfall month
        total_rainfall += monthly_rainfall

# Calculate average rain fall for the total period
average_rainfall = total_rainfall / total_months

print('For', total_months, 'months')
print('Total rainfall: ', format(total_rainfall, '.2f'), 'inches')
print('Average monthly rainfall: ', format(average_rainfall, '.2f'), 'inches')