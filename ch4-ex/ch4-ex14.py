# row-by-row description
# first row: 2 # characters in a row
# second row: # character, 1 space, second # character
# third row: # character, 2 spaces, second # character
# fourth row: # character, 3 spaces, second # character
# fifth row: # character, 4 spaces, second # character
# sixth row: # character, 5 spaces, second # character

# outer loop will iterate 6 times
# inner loop will display # and required spaces

# assign the number of rows to a variable
steps = 6

# write a for loop -- the outer iteration prints # and the inner iteration prints space and #
for r in range(steps):
    print('#', end='')
    for c in range(r):
       print(' ', end='')
    print('#')


