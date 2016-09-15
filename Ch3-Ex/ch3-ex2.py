# Ask the user for the lengths and widths of two rectangles
length_1 = int(input('Enter the length of rectangle 1: '))
width_1 = int(input('Enter the width of rectangle 1: '))
length_2 = int(input('Enter the length of rectangle 2: '))
width_2 = int(input('Enter the width of rectangle 2: '))

# Display the formula for the area of a rectangle
area_1 = length_1 * width_1
area_2 = length_2 * width_2

# Create an IF-ELSE statement that tells the user which
# rectangle has the greater area or if the areas are the same.

if area_1 > area_2:
    print('Rectangle 1 has a greater area than rectangle 2.')
else:
    print('The areas of both rectangles are the same.')


