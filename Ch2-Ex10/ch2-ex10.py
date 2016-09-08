cookie_recipe = 48

# Ask the user how many cookies he or she wants to make
cookies_desired = int(input('How many cookies do you want to make? '))

# Calculate the grams of sugar needed
sugar = ((cookies_desired/cookie_recipe) * 300)

# Calulate the grams of butter needed
butter = ((cookies_desired/cookie_recipe) * 240)

# Calculate the grams of flour needed
flour = ((cookies_desired/cookie_recipe) * 330)

# Display the results
print('Here are the quantities needed for each ingredient to make the specified number of cookies:')
print('Sugar:', sugar)
print('Butter:', butter)
print('Flour:', flour)
