# Create a list with the 12 months of the year

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Ask the user for a number from 1 to 12

def validate_number_and_print():
    if (number == 6 ):
        print ("The best month") 
    
    else:
        print(months[number - 1])


number = int (input ("Enter a number from 1 to 12: "))

validate_number_and_print()



