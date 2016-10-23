# this program calculates the amount of state and county sales tax
# on a purchase

# use the following as global constants
STATE_TAX = 0.05
COUNTY_TAX = 0.025

def main():
    # Get the amount of the purchase
    purchase = get_purchase()
    print('The amount of the purchase is $', format(purchase, '.2f'), sep='')
    # Get the amount of the state sales tax
    state_tax = get_state_tax(purchase)
    print('The amount of the state tax is $', format(state_tax, '.2f'), sep='')
    # Get the amount of the county sales tax
    county_tax = get_county_tax(purchase)
    print('The amount of the county tax is $', format(county_tax, '.2f'), sep='')
    # Get the total sales tax
    sales_tax = state_tax + county_tax
    print('The amount of the total sales tax is $', format(sales_tax, '.2f'), sep='')
    # Get the total of the sale
    total_sale = purchase + sales_tax
    print('The amount of the sale is $', format(total_sale, '.2f'), sep='')


# the get_purchase function gets the amount of the purchase
# from the user and returns that value
def get_purchase():
    amount_purchased = float(input('Enter the amount of the purchase: '))
    # return the value entered
    return amount_purchased

# the get_state_tax function gets the amount of the state tax
# and returns that amount
def get_state_tax(purchased):
    state_tax_charged = purchased * STATE_TAX
    return state_tax_charged

# the get_county_tax function gets the amount of county tax
# and returns that amount
def get_county_tax(purchased):
    county_tax_charged = purchased * COUNTY_TAX
    return county_tax_charged

main()