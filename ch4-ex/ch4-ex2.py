# Use a for loop to displays the number of calories
# burned after 10, 15, 20, 25, and 30 minutes?

for time in range(10, 31, 5):
    calories = time * 4.2
    print('The number of calories burned after', time, 'minutes ' \
          'is', calories)