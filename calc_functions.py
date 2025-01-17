# calc_functions.py
# CMPT 120: Calculator Project
# Author: Michael Wise
# v0.2

import math

def solve(eqlist):
    while len(eqlist) > 1:

        for i in range(1, len(eqlist), 2):   # ensures that it only checks for operators
            
            # Multiplication / Division
            if '*' in eqlist or '/' in eqlist:

                if eqlist[i] == '*':
                    result = float(eqlist[i-1]) * float(eqlist[i+1])
                    del eqlist[i-1:i+2]
                    eqlist.insert(i-1, result)
                    break
      
                elif eqlist[i] == '/':
                    result = float(eqlist[i-1]) / float(eqlist[i+1])
                    del eqlist[i-1:i+2]
                    eqlist.insert(i-1, result)
                    break

            # Addition / Subtraction
            elif '+' in eqlist or '-' in eqlist:
                
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

    answer = eqlist[0]
    return answer
