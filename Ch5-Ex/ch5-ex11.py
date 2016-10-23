# Write an import statement to import the random module
import random

def main():
    generate_random()
    enter_answer()

def generate_random():
    print(random.randint(1,1000))
    print('+', random.randint(1,1000))

def enter_answer():
    answer = input('Enter the correct answer: ')

main()
