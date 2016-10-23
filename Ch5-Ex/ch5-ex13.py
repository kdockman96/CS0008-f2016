# Define the main function
def main():
    for time in range(1,11):
        distance = falling_distance(time)
        print(distance)

# Define the falling_distance function
def falling_distance(falling_time):
        for falling_time in range(1,11):
            return 0.5 * 9.8 * falling_time**2

main()