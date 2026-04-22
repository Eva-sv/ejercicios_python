# Ask the user 5 times to enter a color

colours = []

def checkColor(colours):
    if ('blue' in colours):
        print ("You have won")

    else :
        print ("Try another colour")


for i in range(5):
    colour_value = input(f"Enter colour{i}: ")
    colours.append(colour_value)

checkColor(colours)







