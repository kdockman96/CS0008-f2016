# This program reads and displays the integers in the numbers.txt file

# Define the main function
def main():
    # Open a file named numbers.txt
    infile = open('numbers.txt', 'r')
    # Read the file's contents
    file_contents = infile.read()
    # Close the file
    infile.close()
    # Print the data that was read into memory
    print(file_contents)
# Call the main function
main()