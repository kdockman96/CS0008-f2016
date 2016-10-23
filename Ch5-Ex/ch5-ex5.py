# Define the main function
def main():
    # Get the property value
    property_value = float(input('Enter the property value: '))
    print('The property value is $', format(property_value, '.2f'), sep='')
    # Get the assessment value
    assessment_value = get_assessment_value(property_value)
    print('The assessment value is $', format(assessment_value, '.2f'), sep='')
    # Get the property tax
    property_tax = get_property_tax(assessment_value)
    print('The amount of the property tax is $', format(property_tax, '.2f'), sep='')

# Define the get_assessment_value function
def get_assessment_value(property):
    assessment = 0.60 * property
    return assessment

# Define the get_property_tax function
def get_property_tax(assessment_amount):
    property_tax_amount = (assessment_amount/100) * 0.72
    return property_tax_amount

# Call the main function
main()

