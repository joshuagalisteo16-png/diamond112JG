"""
This was created with my partner
September 8th, 2025
"""

#required number varibles
counter, rowsDrawn, spacesOutside, spacesInside, starstoDraw, userInput = 0,0,0,0,0,0
#
#I'm using a function to organize.

def top_diamond(num1): 
    spacesOutside = userInput // 2
    #Start number of spaces between stars - starts at -1 for the top point
    spacesInside = -1
    #Loop to draw each line of the top half of the diamond
    for i in range(userInput // 2 + 1):
        #Print spaces on the outside (left side)
        print(" " * spacesOutside, end="")
        
        print("*", end="")
        #If not the first line, print inside spaces and the second star
        if spacesInside >= 0:
            print(" " * spacesInside, end="")
            print("*", end="")
        # go on to the  line
        print()
        #Decrease the outside and increase the spaces inside for next row
        spacesOutside -= 1
        spacesInside += 2
        #users input
        
userInput = int(input("Enter your first odd number (1-13) please "))
#Function to draw the top half
top_diamond(userInput)

