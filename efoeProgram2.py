#Efoe Gnassia
#Program 2

#Declare Variables
TAX_RATE = 0.0925
quantity = 0
choice = 0
price = 0.0
subtotal = 0.0
sale_tax = 0.0
total = 0.0

# Display the items on the console
print ('Enter 1 for Baseballs:\nEnter 2 for Bats:\nEnter 3 for Caps:\nEnter 4 for jerseys:\nEnter 5 for Gloves:\nEnter 6 to Exit: ')

# Get the user' choice
choice = int(input('Enter your choice by entering your number:' ))

# We validate the choice of the user by using if statement
if choice < 1 or choice > 6:
    print('You made a wrong choice')
    exit()
elif choice == 6:
    exit()

# Get the user' quantity         
else:
    quantity = int(input('Enter the quantity you want:'))
    
# Determine and assign  price and quantity to the user's  choice
    if choice == 1 and quantity >= 1:
        price = 5.99
        
# Calculate subtotal, sale tax and total
        subtotal = price * quantity
        sale_tax = subtotal * TAX_RATE
        total = subtotal + sale_tax
        
# Determine and assign  price and quantity to the user's  choice
    elif choice == 2 and quantity >= 1:
        price = 15.49

# Calculate subtotal, sale tax and total
        subtotal = price * quantity
        sale_tax = subtotal * TAX_RATE
        total = subtotal + sale_tax
        
# Determine and assign  price and quantity to the user's  choice
    elif choice == 3 and quantity >= 1:
        price = 14.99

# Calculate subtotal, sale tax and total
        subtotal = price * quantity
        sale_tax = subtotal * TAX_RATE
        total = subtotal + sale_tax     
        
# Determine and assign  price and quantity to the user's  choice
    elif choice == 4 and quantity >= 1:
        price = 10.99

# Calculate subtotal, sale tax and total
        subtotal = price * quantity
        sale_tax = subtotal * TAX_RATE
        total = subtotal + sale_tax       

# Determine and assign  price and quantity to the user's  choice
    elif choice == 5 and quantity >= 1:
        price = 43.89

# Calculate subtotal, sale tax and total
        subtotal = price * quantity
        sale_tax = subtotal * TAX_RATE
        total = subtotal + sale_tax
# Display the Subtotal, Sale Tax and Total on the console        
# We display an error message if quantity is not 1 or more
    else:
        print('Error:quantity shloud be 1 or more')


# Display the Subtotal, Sale Tax and Total on the console
print('subtotal: \t$' + format(subtotal, ',.2f'))
print('Sales Tax:\t$' + format(sale_tax,  ',.2f'))
print('total:\t \t$' + format(total, ',.2f'))



 
      
