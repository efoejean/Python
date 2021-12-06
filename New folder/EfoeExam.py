#

def main():
    choice = 0

    
    while choice!= 6:
        # Call the displayMenu() display menu on the console
        displayMenu()
        print()

        # Get the user's choice
        choice = int(input('Enter a number to make a choice: ' ))
        print ()

        # Verify if user's choice is valid 
        if choice >0 and choice <6:
            first_name = input('Enter the name of the first file: ')
            while len(first_name) == 0:
                print('You must enter a file name')
                first_name = (input('Enter  file name: '))
                
            second_name = input('Enter the name of the second file: ')
            while len(second_name) == 0:
                print('You must enter a  file name')
                second_name = (input('Enter a file name: '))

        # Get input text of first file and create set containing its unique words   
            input_file1 = open(first_name, 'r')
            text1 = input_file1.read()
            text1_lower = text1.lower()
            words1 = text1.lower().split()

            unique_words1 = set(words1)     
            input_file1.close
    
        # Get input text of second file and create set containing its unique words
            input_file2 = open(second_name, 'r')
            text2 = input_file2.read()
            text2_lower = text2.lower()
            words2 = text2.lower().split()

            unique_words2 = set(words2)      
            input_file2.close
            

        # Process the choice.
        if choice == 1:
            union(unique_words1, unique_words2)
            print()

        elif choice == 2:
            intersection(unique_words1, unique_words2)
            print()

        elif choice == 3:
            difference(unique_words1, unique_words2)
            print()

        elif choice == 4:
            difference1(unique_words1, unique_words2)
            print()

        elif choice == 5:
            sym_diff(unique_words1, unique_words2)
            print()


        elif choice ==6:
            print("good bye")
            print()

        else:
            print("Incorrect entry.\nTry again.")
            print()  
            
        
    
        
 
 # The union function
def union(wrds1, wrds2):
    union = wrds1.union(wrds2)
    print()
    #Display the convertion on the console
    print('These are the unique words that are ' \
          'contained in both files:')
    print()
    for w in union:
        print(w)

    return

# The intersection function
def intersection(wrds1, wrds2):
    intersection = wrds1.intersection(wrds2)
    print()
    #Display the convertion on the console
    print('These are the words that appear both files:')
    for w in intersection:
        print(w)
    print()

    return

# The difference function
def difference(wrds1, wrds2):
    difference = wrds1.difference(wrds2)
    print()
    #Display the convertion on the console
    print('These are the words that appear in the first file' \
          ' but do not appear in the second file:')
    for w in difference:
        print(w)
    print()

    return

# The difference2 function
def difference1(wrds1, wrds2):
    difference1 = wrds2.difference(wrds1)
    print()
    #Display the convertion on the console
    print('These are the words that appear in the second file' \
          ' but do not appear in the first  file:')
    for w in difference1:
        print(w)
    print()

    return

# The sym_diff function
def sym_diff(wrds1, wrds2):
    sym_diff = wrds1.symmetric_difference(wrds2)
    print()
    #Display the convertion on the console
    print('These are the words that appear in the first' \
          ' file or the second file but do not appear in' \
          ' the both files:')
    for w in sym_diff:
        print(w)
    print()

    return

# displayMenu method
def displayMenu():
    print ('Enter 1 to display the unique words:\nEnter 2 to display the words that appear in both files:\nEnter 3 to display the words that only appear in the first file:\n'
           + 'Enter 4 to display the words that only appear in the second file:\nEnter 5 to display unique words in either the first or second files but not in both:\nEnter 6 to exit the program:')
main()    

        
