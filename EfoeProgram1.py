#Efoe Gnassia
#Program 1
# Get the user number
user_num = float(input('Enter a number: '))

# Calculate User's number squared
square = user_num **2

# Calculate user's number cubed
cube = user_num **3

# Display the label using Escape Character \t on the console
print('User Number\tSquare\t\tCube')

# Display the results using the special argument end='' on the console
print(format(user_num, ',.2f'), end='          ')
print(format(square, ',.2f'), end='         ')
print(format(cube, ',.2f'))
