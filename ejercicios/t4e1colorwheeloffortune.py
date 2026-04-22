
# Display a message based on the chosen color

def wheelFortune(color):
    if (color == 'red'):
        message = "passion and energy"

    elif (color == 'green'):
        message = "hope and growth"

    elif (color == 'blue'):
        message = "calm and serenity"

    elif (color == 'yellow'):
        message = "happiness and optimism"

    elif (color == 'purple'):
        message = "wisdom and creativity"

    return message


 # Ask the user to choose a color

color = (input("Choose a color:  "))

# We call the Wheel of Fortune to give us the message

message = wheelFortune(color)

# We print the message with the chosen color

print(message)


