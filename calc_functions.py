# calc_functions.py
# CMPT 120: Calculator Project
# Author: Michael Wise
#
import math

def calculator():
    equation = input("Enter an equation using (+,-,*,/)")
    eqlist = equation.split(" ")

    while len(eqlist) > 1:
        for i in range(1, len(eqlist), 2):

            # Addition / Subtraction
            if '+' in eqlist or '-' in eqlist:
                
                if eqlist[i] == '+':
                    result = float(eqlist[i-1]) + float(eqlist[i+1])
                    del eqlist[i-1:i+2]
                    eqlist.insert(i-1, result)
                    break
                
                elif eqlist[i] == '-':
                    result = float(eqlist[i-1]) - float(eqlist[i+1])
                    del eqlist[i-1:i+2]
                    eqlist.insert(i-1, result)
                    break
            
            else:
                print("There was an error in your expression.")

    print(eqlist[0])
    
calculator()
    
