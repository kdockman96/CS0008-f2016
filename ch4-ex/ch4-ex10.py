# Print the table headings
print('Year\tTuition')
print('---------------')

tuition = 8000

# Display the tuition for the next 5 years, with a 3% growth each year
for years in range(1,6):
    tuition_growth = tuition * 0.03
    tuition = tuition + tuition_growth
    print(years, '\t\t', '$', format(tuition, ',.2f'), sep='')