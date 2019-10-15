# guessing-game.py
# Author: Michael Wise
# CMPT 120 Lab 5

def main():

    while True:
        print("I am thinking of an animal.")
        guess = input("Guess the name of the animal:")
        guess = guess.lower()
        
        if guess == "zebra":
            print("You guessed correctly!")
            break

        elif guess == "quit":
            print("Quitting the game.")
            exit()
            
        else:
            print("That is incorrect! Try again!")
            print()
                
main()
