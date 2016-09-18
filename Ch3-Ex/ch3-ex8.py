# Ask the user how many people will attend the cookout
people = int(input('Enter the number of people attending the cookout: '))
hot_dogs = int(input('Enter the number of hot dogs each person will be given: '))

# Calculate the minimum number of packages of hot dogs required
# 10 hot dogs in one package
hot_dog_packages = (people * hot_dogs)/10

# Calculate the minimum number of packages of hot dog buns required
hot_dog_buns = (people * hot_dogs)/8

# Calculate the number of hot dogs that will be left over
leftover_hot_dogs = (people * hot_dogs) % 10

# Calculate the number of hot dog buns that will be left over
leftover_buns = (people * hot_dogs) % 8

if people == 50:
    print('The number of hot dog packages required is', hot_dog_packages)
    print('The number of packages of hot dog buns required is', hot_dog_buns)
    print('There will be', leftover_hot_dogs, 'hot dogs left over.')
    print('There will be', leftover_buns, 'hot dog buns left over.')