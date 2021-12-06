# efoe Gnassia
# intializing days, total and commistion
days = 7
total = 0.0
COMM = 0.1

# ask the user to print the sales of each day

print ("Enter the daily sale amount and enter: ")

# loop the days and retrive the amounts type by the user and do the math
for day in range(days):
    amount = float(input('Enter a amount: '))
    total +=amount
    average = total / days
    pay = total * COMM

# Display average sales, total sale and pay on the console
print('Average Sales: $', format(average, ',.2f'))
print('Total Sales: $', format(total, ',.2f'))
print('Pay: $', format(pay, ',.2f'))

