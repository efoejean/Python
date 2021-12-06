# efoe Gnassia
# intializing days, total and commistion spelled commisssion.
days = 7
total = 0.0
COMM = 0.1

#You are supposed to ask the user to enter the number of days they have sales
#for, you are not supposed to assume it is seven days. Most people only work
#five days a week and some work overtime. You must ask the user.
days = int(input('Enter the number of days you have sales for:'))
#Then prevent the user from entering zero or less.
while days <= 0:
    days = int(input('Enter a number greater than zero.'))

# ask the user to print the sales of each day
#You don't allow the user to enter anything here. 
#print ("Enter the daily sale amount and enter: ")

# loop the days and retrive the amounts type by the user and do the math
for day in range(days):
    #amount should be called sales like the directions state.
    amount = float(input('Enter a amount: '))
    #Use a while loop to prevent the user from entering zero or less.
    while amount <= 0:
        amount = float(input('Enter a number greater than zero.'))
    total += amount
    #don't do this inside of the loop. You want this after all sales are totaled.
    #average = total / days
    #pay = total * COMM

#Do the math outside of the for loop after you have the total.
average = total / days
pay = total * COMM    

# Display average sales, total sale and pay on the console
print('Average Sales: $', format(average, ',.2f'))
print('Total Sales: $', format(total, ',.2f'))
print('Pay: $', format(pay, ',.2f'))

