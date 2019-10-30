# personality.py
# CMPT 120 Intro to Programming
# Lab #7 - Matrices & Lookup
# Author: Michael Wise
# Created: 2019-10-29

# Get the mode of interaction from the user


emotionsAI = ["angry", "disgusted", "fearful", "happy", "sad", "surprised"]
interactions = ["reward", "punish", "threaten", "joke"]
current_state = 3
matrix = [[3, 0, 1, 1], [1, 0, 0, 1], [5, 2, 2, 4], [3, 5, 1, 3], [3, 0, 2, 0], [5, 0, 2, 3]]
expressions = ["You really get on my nerves. (`Д´щ;)",
               "Ugh... How disgusting. (ಠ_ಠ)",
               "I am so scared, please stay away from me you creep! (-_-;)",
               "Wow, I couldn't be happier right now! (✿◠‿◠)",
               "You hurt my feelings, I am sad... (︶^︶)",
               "*gasp* What a surprise! (ó_ò)"]

def getInteraction(interactions):
    while True:
        userInput = input("Please enter an interaction. (reward, punish, threaten, joke): ").lower()
        print()
        if userInput in interactions:
            break
        else:
            print("I don't understand what you mean. Please try again.")
    interaction = interactions.index(userInput)
    return interaction

def lookupEmotion(currEmotion, userAction, emotionsAI, matrix):
    newEmotion = emotionsAI[matrix[emotionsAI.index(currEmotion)][userAction]] 
    return newEmotion

def showEmotion(currEmotion, expressions):
    print(expressions[currEmotion])
    
def main():
    currEmotion = "happy"
    print("Hello, I am AI Bob! Right now I'm feeling", emotionsAI[current_state] + ".")
    print("What do you want to do with me?")

    while True:
        currEmotion = lookupEmotion(currEmotion, getInteraction(interactions), emotionsAI, matrix)
        showEmotion(emotionsAI.index(currEmotion), expressions)   

main()
