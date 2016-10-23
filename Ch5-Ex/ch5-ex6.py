# Define the main function
def main():
    # Call get_fat_grams function
    fat_grams = get_fat_grams()
    print('The amount of calories from fat is', fat_grams)
    # Call the get_carb_grams function
    carb_grams = get_carb_grams()
    print('The amount of calories from carbs is', carb_grams)

# Define the get_fat_grams function
def get_fat_grams():
    # Ask the user for the amount of fat grams consumed in a day
    fat = int(input('Enter the amount of fat grams consumed in a day: '))
    calories_fat = fat * 9
    return calories_fat

# Define the get_carb_grams function
def get_carb_grams():
    # Ask the user for the carb grams consumed in a day
    carbs = int(input('Enter the amount of carb grams consumed in a day: ')
    calories_carbs = carbs * 4
    return calories_carbs

# Call the main function
main()
