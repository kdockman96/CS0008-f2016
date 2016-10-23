# Define the main function
def main():
    class_a = class_a_seats()
    class_b = class_b_seats()
    class_c = class_c_seats()

# Define the class_A_seats function
def class_a_seats():
    class_a_tickets = int(input('How many tickets were sold for class A? '))
    income_a = 20 * class_a_tickets
    print('The amount of income generated from class A tickets is $', income_a, sep=')'

# Define the class_B_seats function
def class_b_seats():
    class_b_tickets = int(input('How many tickets were sold for class B? '))
    income_b = 15 * class_b_tickets
    print('The amount of income generated from class B tickets is $', income_b, sep='')

# Define the class_C_seats function
def class_c_seats():
    class_c_tickets = int(input('How many tickets were sold for class C? '))
    income_c = 10 * class_c_tickets
    print('The amount of income generated from class C tickets is $', income_c, sep='')

# Call the main function
main()