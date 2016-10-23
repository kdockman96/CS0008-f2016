# Ask the user to enter two integer values
# in the main function
def main():
    integer1 = int(input('Enter the first integer value: '))
    integer2 = int(input('Enter the second integer value: '))
    # Validate the input to make sure the numbers entered are integer values
    if integer1 != int(integer1) and integer2 != int(integer2):
        print('Please enter an integer value.')
    # Use the returned value to assign to result variable
    result = max(integer1, integer2)
    # Display the results
    print('The greater of the two values is', result)

# Define the max function, using an if statement to see which value is bigger
def max(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        print('ERROR')

# Call the main function
main()

