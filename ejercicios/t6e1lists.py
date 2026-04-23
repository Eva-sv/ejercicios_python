# The list of the 8 planets of the Solar System. Text

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Ask the user for a number from 1 to 8

number = int (input ("Enter a number from 1 to 8: "))

if (number > 8  |  number < 1) :
    print ("Error") 
else:
    print(planets[number - 1])



