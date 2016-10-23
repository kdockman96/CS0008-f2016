# Define the main function
def main():

    # Ask the user for the name of a file
    filename.txt = input('Enter the name of a file: ')

    # Create a variable referencing the number of lines in a file
    num_lines = input('How many lines of data are in the file? ')

    # Open the file
    infile = open('filename.txt', 'r')

    # Create an if-else statement stating what happens if there are five or more lines
    # in a file or fewer than five lines
    if num_lines >= 5:
        # Read the lines from the file
        line1 = infile.readline()
        line2 = infile.readline()
        line3 = infile.readline()
        line4 = infile.readline()
        line5 = infile.readline()
        # Close the file
        infile.close()
        # Display the contents of the file
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        print(line5)
    elif num_lines < 5:
        # Read the entire contents of the file
        file_contents = infile.read()
        # Close the file
        infile.close()
        # Display the contents of the file
        print(file_contents)
    else:
        print('ERROR')
# Call the main function
main()

