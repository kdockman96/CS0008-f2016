# Ask the user which system of units he or she wants to use
units = input('Which system do you want to use? ')

# Ask for the distance driven and gasoline used, using the units entered by the user
# Convert the quantities provided by the user into the other units system
if units == 'USC':
    miles = float(input('How many miles were driven? '))
    gallons = float(input('How many gallons of gasoline were used? '))
    kilometers = miles * 1.60934
    liters = gallons * 3.78541
elif units == 'Metric':
    kilometers = float(input('How many kilometers were driven? '))
    liters = float(input('How many liters of gasoline were used? '))
    miles = kilometers * 0.621371
    gallons = liters * 0.264172
else:
    print('Please enter either USC or Metric.')


# Compute the fuel consumption in MPG and 1/100Km
mpg = miles / gallons
cm = 100 * (liters / kilometers)

# Display the results, with consumption rating at the end, using
# if-else statement
print('')
print('{:>35}'.format('USC'), '{:>17}'.format('Metric'))
print('Distance ______________:', format(miles, '10.3f'), 'miles', format(kilometers, '11.3f'), 'Km')
print('Gas ___________________:', format(gallons, '10.3f'), 'gallons', format(liters, '9.3f'), 'Liters')
print('Consumption ___________:', format(mpg, '10.3f'), 'mpg', format(cm, '13.3f'), '1/100Km')
print('')

# Rate the consumption rate based on the following ranges
if cm > 20:
    print('Gas Consumption Rating : Extremely Poor')
elif 15 < cm <= 20:
    print('Gas Consumption Rating : Poor')
elif 10 < cm <= 15:
    print('Gas Consumption Rating : Average')
elif 8 < cm <= 10:
    print('Gas Consumption Rating : Good')
elif cm <= 8:
    print('Gas Consumption Rating : Excellent')
else:
    print('ERROR')



