# one foot = 12 inches
FEET_TO_INCH = 12

# Define the main function
def main():
    num_feet = float(input('Enter the number of feet: '))
    feet_in_inches = feet_to_inches(num_feet)
    print('The equivalent number of inches is',format(feet_in_inches, '.2f')

# Define the feet_to_inches function
def feet_to_inches(feet):
    return feet * FEET_TO_INCH

print(feet_to_inches(1))
print(feet_to_inches(3))
print(feet_to_inches(10))

# Call the main function
main()