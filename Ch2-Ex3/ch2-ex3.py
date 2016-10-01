# This program calculates the number of acres in a tract of land

# Get the number of square meters in a tract of land
square_feet = int(input("How many square meters are in this tract of land? "))

# Calculate the size of the land in acres
land_size = square_feet/4046.8564224

# Display the result
print ("That's equal to " + format(land_size, '.2f') + " acres.")
