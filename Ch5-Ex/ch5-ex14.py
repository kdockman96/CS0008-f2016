# Define the main function
def main():
    # Ask the user to enter values for mass and velocity
    mass = float(input("Enter a value for an object's mass: "))
    velocity = float(input("Enter a value for an object's velocity: "))
    # Call the kinetic_energy function to get the object's kinetic energy
    kinetic = kinetic_energy(mass, velocity)
    print("The object has the following amount of kinetic energy:", kinetic)

# Define the kinetic_energy function
def kinetic_energy(object_mass, object_velocity):
    return 0.5 * object_mass * object_velocity**2

# Call the main function
main()