"""
This was created with my partner
September 8th, 2025
"""

#required number varibles
counter, rowsDrawn, spacesOutside, spacesInside, starstoDraw, userInput = 0,0,0,0,0,0
#
#I'm using a function to organize.
userInput = int(input("Enter an odd number (1-13): "))

def topDiamond(userInput):
    rowsDrawn= 0
    spacesOutside = userInput // 2 #starts first star at middle row. Num is rounded up.
    spacesInside= -1 #starts at 1 to ignore the "space" at the first star.
    while rowsDrawn <= userInput // 2:
        starstoDraw = " " #begins a new row.
        #down below draws the spaces outside the first star.
        counter = 0
        while counter < spacesOutside:
            starstoDraw += " "
            counter += 1
        starstoDraw += "*"
        #adds a space outside and a star at the end of the output
        #below draws spaces inside beginning from the 2nd star
        if spacesInside > 0:
            counter = 0
            while counter < spacesInside:
                starstoDraw += " "
                counter += 1
            starstoDraw += "*"
        print(starstoDraw)
        rowsDrawn += 1 #each row is added until the user input number
        spacesOutside -= 1 #the space outside is subtracted by 1 each row
        spacesInside += 2 #each space inside is added by 2 each row. Ex: -1+2 =1. 1 space inside.

def bottomDiamond(userInput):
    rowsDrawn= 0
    spacesOutside = 1
    spacesInside= userInput - 4 #begin with num 2 fewer than userinput to be adjacent to 2nd to last num.
    
    while rowsDrawn < userInput // 2:
        starstoDraw= " "
        counter = 0
        while counter < spacesOutside:
            starstoDraw += " "
            counter += 1
        starstoDraw += "*"
        
        if spacesInside > 0:
            counter = 0
            while counter < spacesInside:
                starstoDraw += " "
                counter += 1
            starstoDraw += "*"
        print(starstoDraw)
        rowsDrawn += 1
        spacesOutside += 1
        spacesInside -= 2

def get_valid_input():
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
    return userInput
userInput = get_valid_input()
print(userInput)
topDiamond(userInput)
bottomDiamond(userInput)
