"""
This was created with my partner
September 8th, 2025
"""

#required number varibles
counter, rowsDrawn, spacesOutside, spacesInside, starstoDraw, userInput = 0,0,0,0,0,0
#
#I'm using a function to organize.
userInput=int(input("Enter an odd number (1-13): "))

def topDiamond(userInput):
    rowsDrawn= 0
    spacesOutside = userInput // 2 #starts first star at middle row. Num is rounded up.
    spacesInside= -1 #starts at 1 to ignore the "space" at the first star.
=======
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
>>>>>>> db380acbf0917bf623f9308b73434c945d965df5

    while rowsDrawn <= userInput // 2:
        output= " " #begins a new row.
        #down below draws the spaces outside the first star.
        counter = 0
        while counter < spacesOutside:
            output += " "
            counter += 1
        output += "*"
        #adds a space outside and a star at the end of the output
        #below draws spaces inside beginning from the 2nd star
        if spacesInside > 0:
            counter = 0
            while counter < spacesInside:
                output += " "
                counter += 1
            output += "*"
        print(output)
        rowsDrawn += 1 #each row is added until the user input number
        spacesOutside -= 1 #the space outside is subtracted by 1 each row
        spacesInside += 2 #each space inside is added by 2 each row. Ex: -1+2 =1. 1 space inside.

def bottomDiamond(userInput):
    rowsDrawn= 0
    spacesOutside = 1
    spacesInside= userInput - 4 #begin with num 2 fewer than userinput to be adjacent to 2nd to last num.
    
    while rowsDrawn < userInput // 2:
        output= " "
        counter = 0
        while counter < spacesOutside:
            output += " "
            counter += 1
        output += "*"
        
        if spacesInside > 0:
            counter = 0
            while counter < spacesInside:
                output += " "
                counter += 1
            output += "*"
        print(output)
        
        rowsDrawn += 1
        spacesOutside += 1
        spacesInside -= 2
        return userInput

topDiamond(userInput)
bottomDiamond(userInput)