# Define the main function
def main():

    # Initialize accumulator variable for partial total lines
    PTL = 0
    # Initialize accumulator variable for partial distance
    PD = 0
    # Initialize accumulator variable for total number of lines
    TL = 0
    # Initialize accumulator variable for total distance run
    TD = 0

    # Ask the user to enter the name of a text file
    file = input('Please provide the file name : ')
    print('')
    printKV('File read', file)

    # Create a while loop to process the file if the user desires and to exit
    # the loop if the user says "quit"
    while file and file != 'quit' and file != 'Quit' and file != 'Q' and file != 'q':
        # Open the file using a file object, in the read mode
        if file == 'f2016_cs8_a2.data.1.csv':
            FO = open(r'/Users/karadockman/Downloads/f2016_cs8_a2.data.1.csv', 'r')
        elif file == 'f2016_cs8_a2.data.2.csv':
            FO = open(r'/Users/karadockman/Downloads/f2016_cs8_a2.data.2.csv', 'r')
        # Since processFile function returns two values (partial distance and partial
        # total lines, these two values need to be on the left of the = operator in the
        # assignment statement when the function is called
        PD, PTL = processFile(FO)
        # Print the partial output, using the printKV function call
        # <description> : <value>
        printKV('Partial total # of lines', PTL)
        printKV('Partial distance run', PD)
        print('')
        # Close the file when the processing is complete
        FO.close()
        # Add the partial distance of the particular file to the total distance
        TD += PD
        # Add the partial total lines value to the total number of lines
        TL += PTL
        # Ask the user if they want to enter another file name
        file = input('Please provide the file name : ')
        print('')
        printKV('File read', file)
    # Print the total output from all the files read
    # <description> : <value>
    print('')
    printKV('Total # of lines', TL)
    printKV('Total distance run', TD)


# Define the processFile, using file object as an argument (since it is the way to
# access the actual contents of the file)
def processFile(FO):
    # Initialize accumulator variable for partial total lines
    PTL = 0
    # Initialize accumulator variable for partial distance
    PD = 0
    # Initialize accumulator variable for total number of lines
    TL = 0
    # Initialize accumulator variable for total distance run
    TD = 0
    # Use a for loop to perform specific operations to extract distance from the string
    # in the file
    for line in FO:
        # Strip the implicit newline character from the line
        # Ex) BEFORE this method, the line reads, "Max,32.23\n"
        # AFTER this method, the line reads, "Max,32.23"
        line = line.rstrip('\n')
        # Split the line into a list containing name and distance
        # Output should look like: ["name" "distance]
        temp = line.split(',')
        # Temp[1] refers to the index (position) of the distance in the line
        # Converting distance to a float allows mathematical operations to be
        # performed on the value
        # "distance" (string) >> distance (float)
        dist = float(temp[1])
        # Since PD = 0 intially, distance is added to the total each time the
        # loop is iterated
        PD += dist
        # Since PTL = 0 initially, each time the loop iterates a line is added
        # to the total
        PTL += 1
    # Return the two values that are required to process the total output
    return PD, PTL

# Define the printKV function
def printKV(key, value, klen = 28):
    # Key, which is n-length character string, is the max
    # between length of key and value of klen
    KL = max(len(key), klen)
    # Provide alternative formatting whether value is float, integer, or string
    if isinstance(value, str):
        FS = '.30s'
    elif isinstance(value, float):
        FS = '10.3f'
    elif isinstance(value, int):
        FS = '10'
    print(format(key, str(KL)),':', format(value, FS))

# Call the main function
main()




