# 112 square feet = one gallon of paint, eight hours of labor
# $35/hr of labor
#
# Ask the user to enter the square feet of wall space to be painted
# and the price of paint per gallon
#
# Define the main function
def main():
    square_feet = float(input('Enter the square feet of wall space to be painted: '))
    price_gal = float(input('Enter the price of paint per gallon: '))
    number_gal = num_gal(square_feet)
    labor_hours = labor_hr(square_feet)
    paint_cost = cost_paint(number_gal, price_gal)
    labor_cost = labor_charge(labor_hours)
    total_cost = paint_cost + labor_cost
#
# Define the num_gal function
def num_gal(square_feet):
    gallons = square_feet / 112
    print('The number of gallons of paint required is', format(gallons, '.1f')
#
# Define the labor_hours function
def labor_hr(square_feet):
    hours = (112/8) * square_feet
    print('The hours of labor required are', hours)
#
# Define the paint_cost function
def cost_paint(number_gal, price_gal):
    paint = number_gal * price_gal
    print('The cost of the paint is', format(paint, '.1f'))
    return paint
#
# Define the labor_cost function
def labor_charge(labor_hours):
    cost_labor = labor_hours * 35
    print('The labor charges are', cost_labor)
    return cost_labor
#
# Call the main function
main()