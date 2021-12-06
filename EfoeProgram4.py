# This program calculates an average test score for students

TESTS = 7
def main():
    #Create a list to hold the grades
    grades = [0]*TESTS

    #ask user for grades
    for index in range(TESTS):
        grades[index] = float(input('Enter the score: '))
        #Use a while loop to prevent the user from entering less zero.
        while grades[index] < 0:
            grades[index] = float(input('Enter a score equal or greater than zero: '))

    #calculate the average
    average = get_total(grades) / TESTS

    # Display the total of the grade in the list.
    print('Score\t\tNumeric Score')
    for index in range(len(grades)):
        print('Score', index +1,':\t\t      ', format(grades[index]), sep='')

    #Display the total and average
    print ('Total:      \t     ',format(get_total(grades), ',.1f'))
    print ('Average Score:\t     ', format (average,',.1f'))

def get_total(grade_list):
    # Create a variable to use as an accumulator.
    total = 0
    
    # Calculate the total of grades in the list
    for score in grade_list:
        total += score

    # Return the total.
    return total
# Call the main function
main()
    

        
    
        
        

    
