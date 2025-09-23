"""
This was created with my partner
September 8th, 2025
"""

#required number varibles
counter, rowsDrawn, spacesOutside, spacesInside, starstoDraw, userInput = 0,0,0,0,0,0
#
#I'm using a function to organize.
userInput = int(input("Enter your first odd number (1-13) please "))

def top_diamond(starstoDraw): 
    spacesOutside = userInput // 2
    #Start number of spaces between stars - starts at -1 for the top point
    spacesInside = -1 
    #Loop to draw each line of the top half of the diamond
    rowsDrawn = userInput // 2 + 1
    for i in range(rowsDrawn):
        #Print spaces on the outside (left side)
        print(" " * spacesOutside, end="")
        print("*", end="")
        #If not the first line, print inside spaces and the second star 
        #Decrease the outside and increase the spaces inside for next row
         if spacesInside >= 0:
            print(" " * spacesInside, end="")
            print("*", end="")
        #Move to the next line
        print()
        #Decrease outside spaces and increase inside spaces for next row
        spacesOutside -= 1
        spacesInside += 2

def get_valid_input(counter):
    while True:
        try:
            userInput = int(input("Enter an odd number from 1 to 13: "))
            if userInput < 1 or userInput > 13:
                print("Number must be between 1 and 13.")
            elif userInput % 2 == 0:
                print("Number must be odd.")
            else:
                return userInput
        except ValueError:
            print("Please enter a valid integer.")

    userInput = get_valid_input
#Function to draw the top half
top_diamond(userInput)

#def bottom_diamond
    #spacesOutside = userInput // -2
    #spacesInside = -1
    #for i in range(userInput // 2 + 1):
        #print(" " * spacesOutside, end="")
