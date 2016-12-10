#
# MN: header with user, instructor and course info is missing
#
# Notes:
# MN: the output to screen is enterily missing.
# MN: you should have experimented more and tested your script more
#

# number of files read
# total number of lines read
# total distance run
# total distance run for each participant
# individual maximum distance run and by which participant
# individual minimum distance run and by which participant
# report if there are any participants that appear more than once, how many times, and their names
# total number of participants

# Each individual file should be made up of a dictionary with name as key and distance as value
# Extract the distance (value) using the key (name) for the min and max functions

# OUTPUT
# Number of Input files read   : xx
# Total number of lines read   : xx

# total distance run           : xxxx.xxxxx

# max distance run             : xxxx.xxxxx
#  by participant              : participant name

# min distance run             : xxxx.xxxxx
#  by participant              : participant name

# Total number of participants : xx
# Number of participants
# with multiple records        : xx

# output file

#
# MN: you need to define the functions all at the beginning of your program
#     before you use them
# MN: I moved them here from the bottom of the program
#
# Read the master file list to retrieve the names and distances from each file
# MN: you are assuming that file is a file handler, but it is not.
#     you need to open the file before you use it in the loop
def processMfile(file, d):
    # Initialize relevant accumulator and counter variables
    num_lines = 0
    # MN: why do you have this initializations here when you do not use them within the function?
    #total_ind_dist = 0
    #total_file_dist = 0
    # MN: open the file for reading
    fh = open(file,'r')
    # Loop through the lines in the file
    # MN: you need to use the file handle in the loop and not file
    #for line in file:
    for line in fh:
        # Strip the newline off the end of the line and split the line into name and distance
        # MN: we need to remove the file headers otherwise conversion to float fails
        if 'distance' in line:
            continue
        # MN: incorrect syntax
        #line = line.rstrip('\n').split[',']
        line = line.rstrip('\n').split(',')
        # Key should be a string and is in the first position
        key = str(line[0])
        # Value should be a float and is in the second position
        value = float(line[1])
        # Loop through the keys in the dictionary
        # Check to see if key already exists
        # If it does, append the new distance to the apending distance
        # MN: you need to check if key is in the list of keys of the dictionary d
        # if key in d:
        if key in d.keys():
            # Append distance if key exists
            # MN: append method does in place replacement, you do not need to reassign
            #d[key] = d[key].append(value)
            d[key].append(value)
        else:
            # If key does not exist, add it to the dictionary
            d[key] = [value]
        # Count the number of lines
        num_lines += 1
    # Close the file
    # MN: you need to close the file handle
    #file.close()
    fh.close()
    # Return relevant values
    return d, num_lines

# Define max function
def max_key(d):
    # Get the max distance
    # Use the values method to get a sequence of values to compare
    dist = list(d.values())
    # Get the participant who ran that distance
    # Use the keys method to get a sequence of keys
    name = list(d.keys())
    return name[dist.index(max(dist))]

# Define min function
def min_key(d):
    # Get the min distance
    # Use the values method to get a sequence of values to compare
    dist = list(d.values())
    # Get the participant who ran that distance
    # Use the keys method to get a sequence of keys
    name = list(d.keys())
    return name[dist.index(min(dist))]

# Initialize the accumulator and counter variables
num_files = 0
num_lines = 0
total_lines = 0
total_dist = 0
total_ind_dist = 0
total_file_dist = 0
max_dist = 0
min_dist = 0
num_ind = 0
num_part_more_than_once = 0

# Create a global dictionary
global_dict = {}

# Create an output file
# MN: you do not want to open the output file faraway from where you use it
#output_file = open('output.txt', 'w')

# Assign the master file to a variable
# MN: you should ask the user for the master list file
#dataSource = '/Users/karadockman/Downloads/f2016_cs8_a3/f2016_cs8_a3.data.txt'
dataSource = input('Please enter the master list file : ')
# Open the master input file list
fh = open(dataSource, 'r')
# Read the lines in the master file
sourceFiles = fh.readlines()
# MN: you should close your file handle here. Close file handle right after you are done using it
fh.close()
# Strip the newline character from the end of the individual files
sourceFiles = [item.strip('\n') for item in sourceFiles]


# Initialize the data container
data = []
# Loop through the files to add the distances of each
for source in sourceFiles:
    # Open current data file for reading
    fh = open(source, 'r')
    # Read all the lines and concatenate to data list
    data = data + fh.readlines()[1:]
    # Use the sum function to add all the distances in each file
    total_distance = sum([float(item.strip('\n').split(',')[1]) for item in data])

    # MN: why are you trying to read your file again
    #     you already read all the lines with readlines above
    #     When you get here, they file pointer is at the end of the file
    #     and you will not read anymore lines
    #
    # Loop over all the lines
    #for line in fh:
    #    # Check to see if it is a header
    #    if not 'distance' in line:
    #        # Read the whole file in
    #        data.append(line.rstrip('\n'))

    # MN: you need close the file handle as soon as you are done using it
    #     if you place it outside the loop, you are going to close only the last one
    fh.close()

# Close file
# MN: if you close the file handle here, you are leaving 3 file handles open.
#fh.close()

# MN: why do you need to assign the master file name here?
# MN: you can remove this line. master_file is not used
#master_file = 'f2016_cs8_a3.data.txt'

# Loop through the master file to read convert each file to a dictionary
# MN: with this statement, you are looping on string and not on the content of the file
#     you have to loop on the list sourceFiles that you have previously populated
#
# MN: you need to initialize num_files
num_files = 0
#for file in master_file:
for file in sourceFiles:
    # Create a function to process the file
    # A dictionary is returned from the function
    # Concatenate all the dictionaries to a global dictionary
    d, num_lines = processMfile(file.rstrip('\n'), global_dict)
    # Reassign global dictionary to a new variable
    # MN: why not replace d with global_dict in the previous statement and remove the following one
    global_dict = d
    # Count the number of files
    num_files += 1
    # Add the number of lines from each file to get the total number of lines
    total_lines += num_lines

# MN: initializint the number of participants
num_participants = 0
# Loop through the keys in the dictionary
for key in d:
    # MN: why do you define value and value_list
    #     value is redundant and you re-defined it in the for loop
    # Get the value (distance) associated with each key (name)
    #value = d.get(key, 'Entry not found')
    # Each key should have a value that is a list
    value_list = d[key]
    # Loop through the values in the value list for EACH name
    # MN: total_ind_dist is not initialized and as it is now
    #     you will find the overall total distance across all participants
    for value in value_list:
        # Find the total individual distance
        total_ind_dist += value
    # Get the number of participants
    # MN: key is the name of the participant and it is assigned by the loop
    #     if you want to count the participants you need to use another variable
    #key += 1
    num_participants += 1
    # See if any participants appear more than once
    # MN: you are computing this for each participant
    #     as it is now, as soon as you exit the loop
    #     you will have the info of the last participant
    if len(value_list) > 1:
        num_part_more_than_once += 1

# Close the master file
# MN: master_file is not a file handler, you cannot close it
#master_file.close()
# Create a max function to find the maximum distance
max = max_key(d)
# Create a min function to find the minimum distance
min = min_key(d)

# Open an output file to write the name of the participant, how many times their names
# appear in input files and the total distance run
# MN: wrong syntax
#output_file.open("output_file.txt", 'w')
output_file = open('f2016_cs9_kmd145.output.txt', 'w')

# MN: you are writing only one record and not for all the records.
# MN: wrong variable names and wrong syntax
#output_file.write(key, num_more_than_once, total_inv_dist)
output_file.write(key + ',' + str(num_part_more_than_once) + ',' + str(total_ind_dist))
# MN: you need to close the output file handler
output_file.close()


# MN: why do you have this lines commented here?
# file.open("output_file", 'w')
# file.write(string) inside a loop to print all output

