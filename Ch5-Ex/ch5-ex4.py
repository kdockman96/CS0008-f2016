# Define the main function
def main():
    loan_payment = float(input('Enter the monthly expense for loans: '))
    insurance = float(input('Enter the monthly expense for insurance: '))
    gas = float(input('Enter the monthly expense for gas: '))
    oil = float(input('Enter the monthly expense for oil: '))
    tires = float(input('Enter the montly expense for tires: '))
    maintenance = float(input('Enter the monthly expense for maintenance: '))
    monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance
    print('The monthly cost of all the expenses is $', format(monthly_cost, '.2f'), sep='')
    total_annual_cost = annual_cost(monthly_cost)
    print('The total annual cost of these expenses is $', format(total_annual_cost, '.2f'), sep='')


# Define annual_cost function
def annual_cost(monthly):
    annual = monthly * 12
    return annual

# Call the main function
main()