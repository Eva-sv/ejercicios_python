def guessNumber(number):
    if (number == 4):
        message = "You have won"
    
    elif (number in [1,2,3,5,6,7,8,9,10]):
        message = "You have lost"

    else:
        message = "Incorrect number"
    return message



# Ask the user for a number between 1 and 10

number = float (input("Enter a number between 1 and 10: "))

# We call the guess number to give us the message

message = guessNumber(number)

# We print the message with the choosen number

print(message)


