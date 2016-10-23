# Define the main funcition
def main():
    # Open the names.txt file
    infile = open('names.txt', 'r')
    # Create an accumulator variable
    count = 0
    # Read each line of the file -- test to make sure the line isn't empty first
    line = infile.readline()
    # Create a while loop to read lines of the file until it returns an empty line
    while line != ' ':
        # Display the contents
        print(line, end='')
        # Add each line
        count += 1
        # If the line is NOT empty, then read the next line
        line = infile.readline()
    # Close the file
    infile.close()
    # Display the results
    print('There were a total of', count, 'name(s).')