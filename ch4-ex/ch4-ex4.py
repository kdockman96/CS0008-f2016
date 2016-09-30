# Ask the user for the speed of a vehicle in mph
speed = int(input('What is the speed of the vehicle in mph? '))
time = int(input('How many hours has it traveled? '))

# Print the table headings
print('Hour\tDistance Traveled')
print('------------------------')

# Print the speeds
for htime in range(1, time + 1):
    distance = speed * htime
    print(htime, "\t\t", format(distance, '.1f'))

