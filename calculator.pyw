# calculator.pyw
# Author: Michael Wise
# CMPT 120: Project
from graphics import *
from calc_functions import *


# Draws the window, display, and labels      
def createDisplay(bList):
    keys = createKeypad(bList)
    
    win = GraphWin("Calculator", 500, 600)
    win.setBackground("gray25")
    win.setCoords(0,0,4,7) # the book used these coords but I want to go back and make them nicer
    display = Rectangle(Point(.25, 6),Point(3.75, 6.75))
    display.setFill("white")
    display.draw(win)
    text = Text(Point(2,6.375), "")
    text.setSize(28)
    text.draw(win)
    
    drawKeys(keys, win)
    return win, display, text

# Creates the buttons (alternative to listing them all out one by one)
def createButton(values):
    p1 = Point(values[0] + .1, values[1] + .1)
    p2 = Point(values[0] + .9, values[1] + 0.9)
    button = Rectangle(p1, p2)
    button.setFill(values[3])
    numtext = Text(Point(values[0] + .5, values[1] + .5), values[2])
    numtext.setSize(36)
    return button, numtext

# Creates the full keypad
def createKeypad(lst):
    keys = []
    for key in lst:
        button, numtext = createButton(key)
        keys.append([button, numtext])
    return keys

# Draws all the keys onto the window using a loop
def drawKeys(keys, win):
    for key in keys:
        key[0].draw(win)
        key[1].draw(win)
        
# Gets user input, returns the button label and adds to main equation
def getInput(click, bList):
    x = click.getX()
    y = click.getY()
    for i in range(len(bList)):
        if bList[i][1] == int(y): 
            for j in range(i,len(bList)):
                if bList[j][0] == int(x):
                    if bList[j][2] in ['*','/','+','-']:
                        return " " + bList[j][2] + " "
                    else:
                        return bList[j][2]

def main():
# List containing all the symbols on the calculator with their respective coordinates/colors
# Used integers so it would be easier for getInput to know what button is pressed
    bList = [[0, 1, "+/-", "OrangeRed1"],[1, 1, "0", "gray50"], [2, 1, ".", "gray50"],     [3, 1, "-", "OrangeRed1"],
             [0, 2, "1", "gray50"],      [1, 2, "2", "gray50"], [2, 2, "3", "gray50"],     [3, 2, "+", "OrangeRed1"],
             [0, 3, "4", "gray50"],      [1, 3, "5", "gray50"], [2, 3, "6", "gray50"],     [3, 3, "*", "OrangeRed1"],
             [0, 4, "7", "gray50"],      [1, 4, "8", "gray50"], [2, 4, "9", "gray50"],     [3, 4, "/", "OrangeRed1"],
                                                                [2, 0,  "C", "OrangeRed1"],[3, 0,  "=", "OrangeRed1"]]
    win, display, text = createDisplay(bList)

    equation = ""

# Loop that keeps checking for input
    while True:
        click = win.getMouse()
        buttonText = getInput(click, bList)
        print(buttonText)

        if equation == "Error":
            equation = ""
          
        try:
            # Solves equation (using solve() as defined in calc_functions.py)
            if buttonText == "=": 
                result = solve(equation.split())
                equation = str(result)
            # Changes last digit to opposite sign
            elif buttonText == "+/-":
                lastDigit = float(equation.split()[-1])
                lastDigit = lastDigit * -1
                equation = " ".join(equation.split()[:-1]) + " " + str(lastDigit)
            # Clear calculator (eventually want to add a button that deletes only one entry)
            elif buttonText == "C":
                result = ""
                equation = str(result)
            # Takes the equation string and concatenates it with the text of the button pressed.
            else:
                equation = equation + buttonText
        # Error message        
        except:
            equation = "Error"
              
        text.setText(equation)
        
main()
