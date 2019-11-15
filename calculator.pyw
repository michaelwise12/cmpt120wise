# calculator.pyw
# Author: Michael Wise
# CMPT 120: Calculator Project #3

# Next step is an object-oriented approach!!

from graphics import *
from calc_functions import *

# Draws the window, display, and labels      
def createDisplay(bList):
    keys = createKeypad(bList)
    
    win = GraphWin("Calculator", 500, 600)
    win.setBackground("gray25")
    win.setCoords(0,0,4,7) # the book used these coords but I want to go back and make them nicer
    display = Rectangle(Point(.25, 6.125),Point(3.75, 6.875))
    display.setFill("white")
    display.draw(win)
    text = Text(Point(2,6.5), "0")
    text.setSize(28)
    text.draw(win)
    memText = Text(Point(.5, 6.25),"")
    memText.setSize(8)
    memText.draw(win)
    
    drawKeys(keys, win)
    return win, display, text, memText

# Creates the buttons (alternative to listing them all out one by one)
def createButton(values):
    p1 = Point(values[0] + .1, values[1] + .1)
    p2 = Point(values[0] + .9, values[1] + .9)
    button = Rectangle(p1, p2)
    button.setFill(values[3])
    numtext = Text(Point(values[0] + .5, values[1] + .5), values[2])
    numtext.setSize(34)
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
    if int(y) == 0 and int(x) == 0 or int(y) == 0 and int(x) == 1:
        return "None"
    elif int(y) == 6:
        return "None"
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
             [0, 5, "M+", "red"  ],      [1, 5, "M-", "red"  ], [2, 5, "MR", "red"  ],     [3, 5, "MC", "red"  ],
                                                                [2, 0,  "C", "OrangeRed1"],[3, 0,  "=", "red"]]
    win, display, text, memText = createDisplay(bList)

    equation = ""
    memory = 0

# Loop that keeps checking for input
    while True:
        click = win.getMouse()
        buttonText = getInput(click, bList)
        print(buttonText)
        
        if equation in ["Error", "0", "+", "-", "*", "/"]:
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
                result = "0"
                equation = str(result)
            # If clicking on a space with no button, does nothing (instead of saying error).
            elif buttonText == "None":
                equation = equation
                
            # Memory functions
            elif buttonText == "M+":
                memory = memory + float(solve(equation.split()))
                memText.setText("Mem: " + str(memory))
                
            elif buttonText == "M-":
                memory = memory - float(solve(equation.split()))
                memText.setText("Mem: " + str(memory))
                
            elif buttonText == "MR":
                equation = equation + str(memory)
                memText.setText("Mem: " + str(memory))
                
            elif buttonText == "MC":
                memory = 0.0
                memText.setText("Mem: " + str(memory))
                
            # Takes the equation string and concatenates it with the text of the button pressed.
            else:
                equation = equation + buttonText
        # Error message        
        except:
            equation = "Error"
              
        text.setText(equation)
        
main()
