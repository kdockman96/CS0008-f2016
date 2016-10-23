# Define the main function
def main():
    # Ask for the replacement cost of the insured building
    replacement_cost = float(input('Enter the replacement cost of the building: '))
    # Create a variable representing insurance_value
    insurance_value = replace(replacement_cost)
    # Display the results
    print('The minimum amount of insurance is $', format(insurance_value, '.2f'), sep='')

# Define replace(replacement) function
def replace(replacement):
    # Find out what 80% of the value is
    return 0.80 * replacement

# Call the main function
main()

