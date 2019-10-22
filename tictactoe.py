# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Michael Wise
# Created: 2019-10-22

symbol = [ " ", "x", "o" ]

def printRow(row):

    fullRow = "| "
    for ind in row:
        if ind == 0:
            fullRow = fullRow + symbol[0] + " | "
        if ind == 1:
            fullRow = fullRow + symbol[1] + " | "
        if ind == 2:
            fullRow = fullRow + symbol[2] + " | "
    fullRow += ("\n+-----------+")
    print(fullRow)

def printBoard(board):
    print("+-----------+")
    for row in board:
        printRow(row)

def markBoard(board, row, col, player):
    if hasBlanks(board):
        row = int(row)
        col = int(col)
        if player == 1:
            board[row][col] = 1
        elif player == 2:
            board[row][col] = 2
    else:
        return False
    
def getPlayerMove():
    row = input("Enter the row (0,1,2) where you want to play:")
    col = input("Enter the column (0,1,2) where you want to play:")
    return (row,col)

def hasBlanks(board):
    for row in board:
        for col in row:
            if col == 0:
                return True
            else:
                continue

def main():
    board = [[0,0,0],[0,0,0],[0,0,0]] 
    player = 1
    while hasBlanks(board):
        printBoard(board)
        print("It is Player", str(player) + "'s turn.")
        row,col = getPlayerMove()
        row = int(row)
        col = int(col)
        while board[row][col] != 0:
            print("This is not an empty space.")
            print()
            row,col = getPlayerMove()
            row = int(row)
            col = int(col)
        markBoard(board, row, col, player)
        
        player = player % 2 + 1
    print("Game over.")
        
main()
