# Ask user to enter a temperature in Fahrenheit
f_degrees = float(input('What was the temperature today in degrees Fahrenheit? '))

# Convert temperature from Fahrenheit to Celsius degrees
c_degrees = 5 * (f_degrees-32)/9

# Display the temperature in degrees Celsius
print('The temperature in degrees Celsius is', c_degrees)
