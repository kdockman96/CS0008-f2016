# Get the number of miles driven on last tank of gas
miles = input('How many miles did you drive on the last tank of gas? ')

# Get the number of the gallons of gas used
gallons = input('How many gallons did you use to fill the gas tank? ')

# Calculate MPG where MPG = miles driven/gallons of gas used
miles_per_gallon = float(miles)/float(gallons)

# Display the result
print("You will have gotten", miles_per_gallon, "mpg on your last tank of gas.")

# 1 mile = 1.60934 kilometers
# Convert miles to kilometers
kilometers = miles * 1.60934

#1 gallon = 3.78541 liters
# Convert gallons to liters
liters = gallons * 3.78541

#Calculate L per 100 km
L_per_km = 100 * (liters/kilometers)
