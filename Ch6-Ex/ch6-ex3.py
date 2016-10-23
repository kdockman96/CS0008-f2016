# Create a variable that keeps track of line numbers

line_num = 1

# Define the main function
def main():
    # Ask the user for the name of a file
    filename.txt = input('Enter the name of a file: ')
    # Open the file_name file for reading
    infile = open('filename.txt', 'r')
    # Read all the lines from the file
    for line in infile:
        # Print the line numbers followed by the contents of the line
        print(line_num, ':', line)
    # Close the file
    infile.close()
# Call the main function
main()
