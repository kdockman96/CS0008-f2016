# Print the table headings
print('Year\tMillimeters')
print('--------------------')

# Print the ocean level each year for the next 25 years
for years in range(1, 26):
    ocean_level = 1.6 * years
    print(years, '\t\t', format(ocean_level, '.2f'))