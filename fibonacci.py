# fibonacci.py
# This program outputs the nth term of the Fibonacci sequence, as
# inputted by the user.
# Author: Michael Wise 9/24/19 CMPT120

def main():

    numn, num0 = 1, 1
    n = int(input("Enter a number n:"))
            
    for i in range(n-2):
        numn, num0 = numn + num0, numn
    print("The value of that term of the Fibonacci sequence is", numn)
 
main()
