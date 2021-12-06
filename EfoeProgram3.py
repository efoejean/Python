#Efoe Gnassia
#program 3

#The main function
def main():
# ask user for input
    score1 = float(input('Please enter the first score  Between 0 and 100: '))
    score2 = float(input('Please enter the second score Between 0 and 100: '))
    score3 = float(input('Please enter the third score  Between 0 and 100: '))
    score4 = float(input('Please enter the fourth score Between 0 and 100: '))
    score5 = float(input('Please enter the fifth score  Between 0 and 100: '))

# We call the  calc_avg function to calculate the average of the scores
    average = calc_avg(score1, score2, score3, score4, score5)

    #Display the scores and the grade on the console. we call the get_grade function to get each score.
    print('Score\t\tNumeric Score\tLetter Grade')
    print('Score 1:           ', format(score1, ',.2f'), '          '+ get_grade(score1))
    print('Score 2:           ', format(score2, ',.2f'), '          '+ get_grade(score2))
    print('Score 3:           ', format(score3, ',.2f'), '          '+ get_grade(score3))
    print('Score 4:           ', format(score4, ',.2f'), '          '+ get_grade(score4))
    print('Score 5:           ', format(score5, ',.2f'), '          '+ get_grade(score5))
    print('Average Score:\t\t\t ', format(average,',.2f'))


# Calc_avg function
def calc_avg(scr1, scr2, scr3, scr4, scr5):
    total = scr1 + scr2 + scr3 + scr4 + scr5
    avrage = total / 5
    return avrage

#get_grade function
def get_grade(test_score):
    if test_score >= 90 and test_score <= 100:
        grade = 'A'
    elif test_score >= 80 and test_score <= 89.99:
        grade = 'B'
    elif test_score >= 70 and test_score <= 79.99:
        grade = 'C'
    elif test_score >= 60 and test_score <= 69.99:
        grade = 'D'
    else:
        grade = 'F'

    return grade
    
# Call the main function
main()
