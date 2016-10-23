# Define the main function
def main():
    # Initiate an accumulator variable
    total = 0
    # Open the numbers.txt file
    infile = open('numbers.txt', 'r')
    # Read the numbers from the file
    for line in infile:
        amount = int(line)
        total += amount
    # Close the file
    infile.close()
    # Print the total
    print(total)
# Call the main function
main()