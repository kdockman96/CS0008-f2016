# NUM_DAYS constant holds the number of days that we will gather sales data for
NUM_DAYS = 7

def main():
    # Create a list to hold the sales for each day
    sales = [0] * NUM_DAYS

    # Create a variable to hold an index
    index = 0

    print('Enter the sales for each day: ')

    # Get the sales for each day
    while index < NUM_DAYS:
        print('Day #', index + 1, ': ', sep='', end='')
        sales[index] = float(input())
        index += 1

    # Create a variable to use as an accumulator
    total = 0

    # Calculate the total of the list elements
    for value in sales:
        total += value

    # Display the total of the list elements
    print('The total sales for week is $', format(total, '.2f'), sep='')

# Call the main function
main()