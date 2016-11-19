# import the random module in order to use the functions to generate random numbers
import random

# Create an list that will hold 7 elements
lottery_list = [0] * 7

# Add some random numbers to the list
index = 0
while index < len(lottery_list):
    # Generate a random number
    lottery_list[index] = random.randint(1,9)
    index += 1

# Display each element of the list
print('Here are the lottery numbers: ')

# Create a loop to display the elements
for value in lottery_list:
    print(value)


