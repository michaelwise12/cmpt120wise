# pi.py
# This program approximates the value of pi using a series.
# Author: Michael Wise 9/24/19 CMPT 120

import math

def main():
    n = int(input("Enter a value n:"))

    result = 0
    sign = 1
    
    for i in range(n):
        result = result + sign * 4/(2*i + 1)
        sign = -sign   # I don't know if this is cheating but it works

    print("The approximated value to pi is:", result)
    print("The difference between approximation and pi is:", math.pi - result)
    
# As n approaches infinity, the number will oscillate closer and closer to pi.

main()
