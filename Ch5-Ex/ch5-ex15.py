# Get five scores
score1 = float(input('Enter a test score: '))
score2 = float(input('Enter a test score: '))
score3 = float(input('Enter a test score: '))
score4 = float(input('Enter a test score: '))
score5 = float(input('Enter a test score: '))

# Define the main function
def main():
    average_score = calc_average(score1, score2, score3, score4, score5)
    print('The average score is', average_score)
    determine_grade(score1)

# Define calc_average function
def calc_average(first_score, second_score, third_score, fourth_score, fifth_score):
    return (score1 + score2 + score3 + score4 + score5) / 5


# Define determine_grade function
def determine_grade(first_score):
    if first_score >= 90 and first_score <= 100:
        print('The first score is an A')
    elif first_score >= 80 and first_score <= 89:
        print('The first score is a B')
    elif first_score >= 70 and first_score <= 79:
        print('The first score is a C')
    elif first_score >= 60 and first_score <= 69:
        print('The first score is a D')
    else:
        print('The first score is F')

# Call the main function
main()