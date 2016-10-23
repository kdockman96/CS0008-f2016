# the first row contains 7 asteriks, with the following rows with one less asterik
base_size = 7

# create a while loop to print the pattern
# running total subtracts 1 from the base size each time
while base_size > 0:
    print('*' * base_size)
    base_size -= 1

