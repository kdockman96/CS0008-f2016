# Specify the starting and ending temperature
start_temp = 0
end_temp = 21

# Print the table headings
print('Celsius\tFahrenheit')
print('--------------------')

# Print the temperatures
for celsius in range(start_temp, end_temp):
    fahrenheit = (9/5)* celsius + 32
    print(celsius, '\t\t', format(fahrenheit, '.1f'))

