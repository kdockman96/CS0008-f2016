# name       : Kara Dockman
# email      : kmd145@pitt.edu
# date       : 12/15/2016
# class      : CS0008-f2016
# instructor : Max Novelli

# Final Project

# Description:

# A customer needs to process a number of text files (called data files) that contain names and distance run by study
# participants.
# The format of those files is as follows:
#
# Max ,34.23
# Barbara ,23.00
# Luka ,12.87
#
# In those files, each row is a comma separated list of 2 values: the first one is the name of the participant and the
# second is the distance that the participant has run.
# The names of the input files are stored one per line in an additional file, called the master input list.
# This file has the following structure:
#
# <data file 1>
# <data file 2>
# <data file 3>
# …
#
# Write a program that read the master input list file, retrieves the names of the data files and from each one of them
# reads every line, extract name and distance. Once the program has all the data in memory, it has to compute the
# following quantities and informations:
# - number of files read in input
# - total number of lines read
# - total distance run (aka the sum of all the distances loaded from provided files)
# - total distance run for each individual participant
# - individual maximum distance run and by which participant
# - individual minimum distance run and by which participant
# - report if there are any participants that appears more than once, how many times and their names
# - total number of participants
#
# The program should provide an terminal output similar to the following:
#
#	Number of Input files read   : xx
#	Total number of lines read   : xx
#
#	total distance run           : xxxx.xxxxx
#
#	max distance run             : xxxx.xxxxx
#	  by participant             : participant name
#
#	min distance run             : xxxx.xxxxx
#	  by participant             : participant name
#
#	Total number of participants : xx
#	Number of participants
#    with multiple records       : xx
#
# The program should also create an output file reporting name of the participant, how many times their name appears in
# the input files and the total distance run. Each row should be as follows:
#
# Max,3,124.23
# Barbara,2,65.00
# Luka,1,12.87

# Use a class named participants that has 2 properties:
# name: name of the participant. String.
# distance: accumulator for total distance run by the participant. Float.
# runs: accumulator for the total number of runs run by the participant.
# Use the following methods:
# addDistance(d)
# add single distance to the distance accumulator and increments runs by 1. Argument d is a single float.
# addDistances(ld)
# add an array of distances to distance accumulator. Argument ld is a list of floats.
# getDistance()
# get the current value of the distance accumulator.
# getName()
# get the name of the participant of the current instance
# __init__ (n,d=0)
# initializer method. set name and initial distance if provided. If initial distance is not specified, it should be set
# to zero
# __str__()
# stringify method. Returns a string with name, total distance run and how many distances the object added, according
# to the following format:
# Name : xxxxxxxxxxxxxxxxxxx. Distance run : yyyy.yyyy. Runs : zzzz
# where xxxxxxxxxxxxxxxxxxx is a right align string of 20 characters for the name,
# yyyy.yyyy is the total distance run with 9 digits, decimal point and 4 decimals,
# and zzzz is the number of runs with 4 digits, no decimals.


# class definition
class participant:
    """ participant class """

    # data attributes
    # name of participant
    name = 'unknown'
    # total distance run by the participant
    distance = 0
    # total number of runs by the participant
    runs = 0

    # methods
    # initializer methods
    def __init__(self, name, distance=0):
        # set name
        self.name = name
        # set distance if not zero
        if distance > 0:
            # set distance
            self.distance = distance
            # set number of runs
            self.runs = 1
    # addDistance method
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1
    # addDistances method
    def addDistances (self, distances):
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1
    # return the name of participant
    def getName(self):
        return self.name
    # return total distance
    def getDistance(self):
        return self.distance
    # return number of runs
    def getRuns(self):
        return self.runs
    # use str method
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')
    # convert to csv
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])

# function getDataFromFile(file)
# read all the lines from the file, remove first line (header) and split all the others into name and distance
# insert a dictionary with name and distance in output list
#
# Input:
#  - file: (string) data file name
#
# Output
#  - data: (list) list of dictionaries, with each dictionary defined as follows
#          { 'name': <participant_name>, 'distance' : <distance_run> }

def getDataFromFile(file):
    # Initialize output list
    output = []
    # read lines in file
    for line in open(file, 'r'):
        # Exclude the first line, which is the header (contains the word 'distance')
        if "distance" in line:
            # skip line
            continue
         # remove \n at the end of each line and split the line
        temp1 = line.rstrip('\n').split(',')
        # use try/except to avoid unhandled errors
        try:
            # append record to output list in the form of a dictionary with 2 keys: name and distance
            # remove unwanted spaces from name and convert distance to float
            output.append({'name': temp1[0].strip(' '), 'distance':float(temp1[1])})
        except:
            # catch all the lines that are incorrectly formatted and skip them
            print('Invalid row : '+line.rstrip('\n'))
    # return data
    return output

# Get master file from user
masterFile = input('Enter the master file: ')

# Read master file and extract files
try:
    dataFiles = [file.rstrip('\n') for file in open(masterFile,'r')]
except:
    print("Impossible to read master file or invalid file name")
    exit(1)

# read data from files
# rawData is a list of 3 lists which contains dictionaries with data from each file
rawData = []
for file in dataFiles:
    for item2 in getDataFromFile(file):
        rawData.append(item2)


# number of files read
# this is equivalent to the number of elements in dataFiles
numberFiles = len(dataFiles)

# total number of lines read
# this is equivalent to the sum of the second item in each item of rawData
totalLines = len(rawData)

# total number distance run by every participant
# this is equivalent of the sum of the "distance" element of the items in rawData
totalDistanceRun = sum([item['distance'] for item in rawData])

# compute distance run for each participant and how many records for each one
# initialize all the accumulators
# dictionary with one element for each participant whose value is
# the list of all the distances found in data for the participant
participants= {}

for item in rawData:
    # check if the names have already been found previously or if it is new
    # if new, initialize elements
    if not item['name'] in participants.keys():
        participants[item['name']] = participant(item['name'])
    # add distance in the list for participant
    participants[item['name']].addDistance(item['distance'])


# initialize accumulators

# minimum distance run with name
minDistance = { 'name' : None, 'distance': None }

# maximum distance run with name
maxDistance = { 'name' : None, 'distance': None }

# appearances dictionary
appearances = {}
#
# compute the total distance run for each participant iterating on all the participants
for name, object in participants.items():
    # get the total distance run by this participant
    distance = object.getDistance()
    # check if we need to update min
    # if this is the first iteration or if the current participant distance is lower than the current min
    if minDistance['name'] is None or minDistance['distance'] > distance:
        minDistance['name'] = name
        minDistance['distance'] = distance

    # check if we need to update max
    # if this is the first iteration or if the current participant distance is higher than the current max
    if maxDistance['name'] is None or maxDistance['distance'] < distance:
        maxDistance['name'] = name
        maxDistance['distance'] = distance

    # get number of runs, aka appearances from participant object
    participantAppearances = object.getRuns()
    #
    # check if we need to initialize this entry
    if not participantAppearances in appearances.keys():
        appearances[participantAppearances] = []
    appearances[participantAppearances].append(name)

# compute total number of participants
# this is equivalent to the length of participants
totalNumberOfParticipant = len(participants)

# compute total number of participants with more than one record
# extract all the participants that have 2 or more runs
# and count the number of elements in the list with len()
totalNumberOfParticipantWithMultipleRecords = len([1 for item in participants.values() if item.getRuns() > 1])

# set format strings
INTEGER = '3d'
FLOAT = '11.5f'
STRING = '20s'
#
# provide requested output
print("")
print(" Number of Input files read   : " + format(numberFiles,INTEGER))
print(" Total number of lines read   : " + format(totalLines,INTEGER))
print("")
print(" Total distance run           : " + format(totalDistanceRun,FLOAT))
print("")
print(" Max distance run             : " + format(maxDistance['distance'],FLOAT))
print("   by participant             : " + format(maxDistance['name'],STRING))
print("")
print(" Min distance run             : " + format(minDistance['distance'],FLOAT))
print("   by participant             : " + format(minDistance['name'],STRING))
print("")
print(" Total number of participants : " + format(totalNumberOfParticipant,INTEGER))
print(" Number of participants")
print("  with multiple records       : " + format(totalNumberOfParticipantWithMultipleRecords,FLOAT))
print("")

# create output file
outputFile = "f2016_cs8_kmd145_fp.data.output.csv"
# open file for writing
fh = open(outputFile,'w')
# write header in file
fh.write('name,records,distance\n')
# loop on all the participants
for name, object in participants.items():
    # write line in file
    fh.write(object.tocsv() + '\n')

# close files
fh.close()
