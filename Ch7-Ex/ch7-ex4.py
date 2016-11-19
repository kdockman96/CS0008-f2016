# Define the main function
def main():
    # Create a function that gets numbers from the user
    numbers = get_values()
    # Display the lowest and highest numbers from the list
    print('The lowest number is', min(numbers))
    print('The highest number is', max(numbers))
    # Initialize an accumulator variable
    total = 0
    # Use a loop to find the total of the numbers
    for value in numbers:
        total += value
    # Display the total
    print('The total is', total)
    # Calculate the average
    average = total / len(numbers)
    #  Display the average
    print('The average is', average)

# Define the get_values function
def get_values():
    print('Please enter a series of 20 numbers.')
    # Create an empty list
    values = []
    # Append each number to the list as the loop iterates
    for num in range(20):
        value = int(input('Enter a number: '))
        values.append(value)
    return values

# Call the main function
main()



