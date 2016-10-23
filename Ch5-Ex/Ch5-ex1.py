# Ask the user for a distance in kilometers
# first define the main function
def main():
    # display the intro screen
    intro()
    distance = float(input('Enter the distance in kilometers: '))
    # Convert kilometers to miles
    km_to_miles(distance)
#
# define the intro function
def intro():
    print('This program converts distance in kilometers to miles.')
    print('')

# KM_to_miles function accepts a distance in km and converts it
# to miles
def km_to_miles(km):
    miles = km * 0.6214
    print('That converts to', format(miles, '.2f'), 'miles')

# call the main function
main()