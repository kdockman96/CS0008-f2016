# Get the number of males in the class
males = int(input("How many males are registered in the class? "))

# Get the number of females in the class
females = int(input("How many females are registered in the class? "))

# Find the total amount of students in the class
total = males + females

# Calculate the percentage of males in the class
males_percentage = males//total

# Calculate the percentage of females in the class
females_percentage = females//total

# Display the percentages, with formatting
print('There are{}'.format(males_percentage, '%'), "males in the class.")
print('There are{}'.format(females_percentage, '%'), "females in the class.")
