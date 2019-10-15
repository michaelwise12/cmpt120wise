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
            yesorno = input("Do you like this animal? (type y/n)")
            if yesorno == "y":
                print("That is awesome! I like zebras too.")
            elif yesorno == "n":
                print("YOU MONSTER, HOW DARE YOU HATE ZEBRAS!")
            else:
                print("You did not input a valid answer. Rerun the program.")
            break

        elif guess[0] == "q":
            print("Quitting the game.")
            exit()
            
        else:
            print("That is incorrect! Try again!")
            print()
             
main()
