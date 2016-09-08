# Create two variables: speed and time
speed = 90
time = 6
# Display the values referenced by the variables
print(speed)
print(time)
# Multiply speed by time to find distance traveled in 6 hours
distance = speed * time
# Display the number of miles the car travels in 6 hours
print("The car will travel", distance, "miles in 6 hours.")
# Reassign the time variable so it references a different value
time = 10
# Multiply speed by time to find distance traveled in 10 hours
distance = speed * time
# Display the number of miles the car travels in 10 hours
print('The car will travel', distance,'miles in 10 hours.')
# Reassign the time variable so it references a different value
time = 15
# Multiply speed by time to find distance traveled in 15 hours
distance = speed * time
# Display the number of miles the car travels in 15 hours
print('The car will travel', distance, 'miles in 15 hours.')
# Reassign the time variable so it references a different value
time = 2.42
# Multiply speed by time to find distance traveled in 2 hours 25 minutes
distance = speed * time
format = (distance, ',.2f')
# Display the number of miles the car travels in 2 hours and 25 minutes
print('The car will travel', format(distance, '.2f'),
      'miles in 2 hours and 25 minutes')




