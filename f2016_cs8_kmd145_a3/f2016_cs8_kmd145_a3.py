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
output_file = open('output.txt', 'w')

# Assign the master file to a variable
dataSource = '/Users/karadockman/Downloads/f2016_cs8_a3/f2016_cs8_a3.data.txt'
# Open the master input file list
fh = open(dataSource, 'r')
# Read the lines in the master file
sourceFiles = fh.readlines()
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

    # Loop over all the lines
    for line in fh:
        # Check to see if it is a header
        if not 'distance' in line:
            # Read the whole file in
            data.append(line.rstrip('\n'))
# Close file
fh.close()

master_file = 'f2016_cs8_a3.data.txt'

# Loop through the master file to read convert each file to a dictionary
for file in master_file:
    # Create a function to process the file
    # A dictionary is returned from the function
    # Concatenate all the dictionaries to a global dictionary
    d, num_lines = processMfile(file.rstrip('\n'), global_dict)
    # Reassign global dictionary to a new variable
    global_dict = d
    # Count the number of files
    num_files += 1
    # Add the number of lines from each file to get the total number of lines
    total_lines += num_lines
# Loop through the keys in the dictionary
for key in d:
    # Get the value (distance) associated with each key (name)
    value = d.get(key, 'Entry not found')
    # Each key should have a value that is a list
    value_list = d[key]
    # Loop through the values in the value list for EACH name
    for value in value_list:
        # Find the total individual distance
        total_ind_dist += value
    # Get the number of participants
    key += 1
    # See if any participants appear more than once
    if len(value_list) > 1:
        num_part_more_than_once += 1
# Close the master file
master_file.close()
# Create a max function to find the maximum distance
max = max_key(d)
# Create a min function to find the minimum distance
min = min_key(d)

# Open an output file to write the name of the participant, how many times their names
# appear in input files and the total distance run
output_file.open("output_file.txt", 'w')
output_file.write(key, num_more_than_once, total_inv_dist)

# Read the master file list to retrieve the names and distances from each file
def processMfile(file, d):
    # Initialize relevant accumulator and counter variables
    num_lines = 0
    total_ind_dist = 0
    total_file_dist = 0
    # Loop through the lines in the file
    for line in file:
        # Strip the newline off the end of the line and split the line into name and distance
        line = line.rstrip('\n').split[',']
        # Key should be a string and is in the first position
        key = str(line[0])
        # Value should be a float and is in the second position
        value = float(line[1])
        # Loop through the keys in the dictionary
        # Check to see if key already exists
        # If it does, append the new distance to the apending distance
        if key in d:
            # Append distance if key exists
            d[key] = d[key].append(value)
        else:
            # If key does not exist, add it to the dictionary
            d[key] = [value]
        # Count the number of lines
        num_lines += 1
    # Close the file
    file.close()
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

# file.open("output_file", 'w')
# file.write(string) inside a loop to print all output

