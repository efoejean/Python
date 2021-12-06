# Exam 2

def main():
    choice = 0

    
    while choice!= 5:
        # Call the displayMenu() display menu on the console
        displayMenu()
        print()

        # Get the user's choice
        choice = int(input('Enter a number to make a choice: ' ))
        print ()

        # Verify if user's choice is valid 
        if choice >0 and choice <5:
            user_string = (input('Enter the string: '))
            while len(user_string) == 0:
                print('You must enter a string')
                user_string = (input('Enter the string: '))

        #Use the upper() method to convert the string to uppercase.
        if choice == 1:
            firstChoice = user_string.upper()
            print()
            #Display the convertion on the console
            print (" You entered {} and the convertion is {}" .format(user_string, firstChoice))
            print()

         #use the lower() method to convert the string to lowercase
        elif choice == 2:
            secondChoice = user_string.lower()
            print()
            print(" You entered {} and the convertion is {}" .format(user_string, secondChoice))
            print()

        # use the split() method to split the string on spaces 
        elif choice == 3:
            thirdChoice = user_string.split(" ")

            #and store it in a list called user_list and Use the len() method to get the length of the list
            user_list = []
            for ls in range(len(thirdChoice)):
                user_list.append(ls)

            print()

            #Display the result on the console
            print (" You entered {} and it has {} words " .format(user_string, user_list[ls] + 1))
            print()
            
        #
        elif choice == 4:
            # Use a variable called vowels to store the vowels in.
            vowels = 'AEIOU'

            # using the upper() to make sure count counts upper and lowercase vowels
            fourthChoice = (user_string).upper()
            count= 0

            # iterate through the user’s string
            for ch in fourthChoice:
                # Usee find() method to check for the characters contained in the vowels variable in the user’s string
                if vowels.find(ch) != -1:
                    count += 1
                    
            print()
            #Display the result on the console
            print(" You entered {} and it has {} vowels " .format(user_string, count))
            print()

        elif choice == 5:
            print("Good Bye")
            print()


        else:
            print("Incorrect entry.\nTry again.")
            print()
 

# displayMenu method
def displayMenu():
    print ('Enter 1 to convert a string to uppercase:\nEnter 2 to convert a string to lowercase:\nEnter 3 to count the number of words in a string:\n'
       + 'Enter 4 to count the number of vowels in a string:\nEnter 5 to Exit: ')

main()    

        
