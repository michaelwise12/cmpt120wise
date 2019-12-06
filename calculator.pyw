# calculator.pyw
# Author: Michael Wise
# CMPT 120: Calculator Project #4

from graphics import *
from calc_functions import *

class Calculator:
    """ Encloses all functionality of the calculator. """
    def __init__(self):
        self.win = GraphWin("Calculator", 500, 600)
        self.win.setBackground("gray25")
        self.win.setCoords(0,0,4,7)
        self.keypad = Keypad(self.win)
        self.display = Display(self.win)
        self.engine = CalcFunctions(self.win)

    def run(self):
        while True:
            click = self.win.getMouse()
            buttonText = self.keypad.getInput(click)
            print(buttonText)
            result = self.engine.processInput(buttonText)
            self.display.update(result)
            if buttonText in ["M+", "M-", "MC", "MR"]:
                self.display.updateMem("Mem: " + str(self.engine.memory))
                self.display.update(result)
            
class Button:
    def __init__(self, win, center, width, height, text, color):
        """ Encloses all functionality for creating buttons. """
        width = width/2
        height = height/2
        x = center.getX()
        y = center.getY()
        self.xmax, self.xmin = x + width, x - width
        self.ymax, self.ymin = y + width, y - width
        self.color = color
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.button = Rectangle(p1, p2)
        self.button.setFill(color)
        self.button.draw(win)
        self.text = Text(center, text)
        self.text.setSize(34)
        self.text.draw(win)

    def getTextlabel(self):
        return self.text.getText()

    def isClicked(self, p):
        if self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax:
            return True
            

class Display:
    """ Encloses all functionality for rendering and updating the display. """
    def __init__(self, win):
        self.display = Rectangle(Point(.25, 6.125), Point(3.75, 6.875))
        self.display.setFill("white")
        self.display.draw(win)
        self.text = Text(Point(2,6.5), "0")
        self.text.setSize(28)
        self.text.draw(win)
        self.memText = Text(Point(.5, 6.25),("Mem: 0.0"))
        self.memText.setSize(8)
        self.memText.draw(win)
        self.memory = 0.0
    def update(self, result):
    # Updates the text on the screen.
        self.text.setText(result)

    def updateMem(self, result):
    # Updates the memory text on the display.
        self.memText.setText(result)

class Keypad:
    """Stores all the functionality for interacting with the keypad."""
    def __init__(self, win):
        self.win = win
    # List of all the button objects (win, center, width, height, text, color)
        self.bList =  [Button(win, Point(.5,  1.5),  .8, .8, "+/-", "OrangeRed1"),
                       Button(win, Point(1.5, 1.5),  .8, .8, "0", "gray50"),
                       Button(win, Point(2.5, 1.5),  .8, .8, ".", "gray50"),
                       Button(win, Point(3.5, 1.5),  .8, .8, "-", "OrangeRed1"),
                       Button(win, Point(.5, 2.5),  .8, .8, "1", "gray50"),
                       Button(win, Point(1.5, 2.5), .8, .8, "2", "gray50"),
                       Button(win, Point(2.5, 2.5), .8, .8, "3", "gray50"),
                       Button(win, Point(3.5, 2.5), .8, .8, "+", "OrangeRed1"),
                       Button(win, Point(.5, 3.5),  .8, .8, "4", "gray50"),
                       Button(win, Point(1.5, 3.5), .8, .8, "5", "gray50"),
                       Button(win, Point(2.5, 3.5), .8, .8, "6", "gray50"),
                       Button(win, Point(3.5, 3.5), .8, .8, "*", "OrangeRed1"),
                       Button(win, Point(.5,  4.5), .8, .8, "7", "gray50"),
                       Button(win, Point(1.5, 4.5), .8, .8, "8", "gray50"),
                       Button(win, Point(2.5, 4.5), .8, .8, "9", "gray50"),
                       Button(win, Point(3.5, 4.5), .8, .8, "/", "OrangeRed1"),
                       Button(win, Point(.5,  5.5), .75, .75, "M+", "red"),
                       Button(win, Point(1.5, 5.5), .75, .75, "M-", "red"),
                       Button(win, Point(2.5, 5.5), .75, .75, "MR", "red"),
                       Button(win, Point(3.5, 5.5), .75, .75, "MC", "red"),
                       Button(win, Point(2.5, .5),  .8, .8, "C", "OrangeRed1"),
                       Button(win, Point(3.5, .5),  .8, .8,  "=", "red")]
        
    # Checks if button is clicked. If so, get the label of the button.
    def getInput(self, p):
        for button in self.bList:
            if button.isClicked(p):
                label = button.getTextlabel()
                return label

class CalcFunctions:
    """ Class that processes the inputs and outputs the current equation. """
    def __init__(self, win):
        self.win = win
        self.equation = ""
        self.memory = 0.0
    # Processes the input recieved and interprets it accordingly.
    def processInput(self, buttonText):
        if self.equation in ["Error", "0", "+", "-", "*", "/"]:
            self.equation = ""
          
        try:
            # Solves equation (using solve() as defined in calc_functions.py)
            if buttonText == "=": 
                result = solve(self.equation.split())
                if result.is_integer():
                    self.equation = str(int(result))
                else:  
                    self.equation = str(result)
                return self.equation
            elif buttonText in ["0","1","2","3","4","5","6","7","8","9"]:
                self.equation = self.equation + buttonText
                return self.equation
            elif buttonText == ".":
                self.equation = self.equation + "."
                return self.equation
            elif buttonText in ["*", "/", "+", "-"]:
                self.equation = self.equation + " " + buttonText + " "
                return self.equation
            # Changes last digit to opposite sign
            elif buttonText == "+/-":
                lastDigit = float(self.equation.split()[-1])
                lastDigit = lastDigit * -1
                self.equation = " ".join(self.equation.split()[:-1]) + " " + str(lastDigit)
                return self.equation
            # Clear calculator
            elif buttonText == "C":
                result = "0"
                self.equation = str(result)
                return self.equation
            # If clicking on a space with no button, does nothing (instead of saying error).
            elif buttonText == "None":
                self.equation = self.equation
                return self.equation
            # Memory functions
            elif buttonText == "M+":
                self.memory = self.memory + float(solve(self.equation.split()))
                return self.equation
            
            elif buttonText == "M-":
                self.memory = self.memory - float(solve(self.equation.split()))
                return self.equation
            
            elif buttonText == "MR":
                self.equation = self.equation + str(self.memory)
                return self.equation
            
            elif buttonText == "MC":
                self.memory = 0.0
                
        # Error message        
        except:
            self.equation = ""
            return "Error"
        
def main():
    # Runs the calculator
    calculator = Calculator()
    calculator.run()
    
main()
