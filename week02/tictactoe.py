# Assignment: W02 Prove: Developer - Solo Code Submission
# Author: Nikkolet Ashby
# Purpose: Program plays Tic Tac Toe game for enjoyment of two users. 
# Date: 4/27/2022

#=======================================Modules============================================
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
#==========================================================================================

def main():
    print("Welcome to Tic Tac Toe!")
    print()
    print("The awesome classic game that allows you to customize your experience!")
    print("What challenge level do you want? ")
    print()
    print("1. Easy - 3 x 3 board")
    print("2. Medium - 4 x 4 board")
    print("3. Hard - 5 x 5 board")
    print("4. Expert - 6 x 6 board")
    print()
    board_size = int(input("Please enter your level number(1-4): "))
    player = next_player("")
    board = create_board(board_size)
    print(board)
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 

def create_board(board_size):
    board = []
    if board_size == 1:
        for square in range(9):
            board.append(square + 1)
        return board
    elif board_size == 2:
        for square in range(16):
            board.append(square + 1)
        return board    
    elif board_size == 3:
        for square in range(25):
            board.append(square + 1)
        return board  
    elif board_size == 4:
        for square in range(36):
            board.append(square + 1)
        return board       
    else:
        print("Oop! You've entered an invalid value. Please try again!")

def display_board(board):
    range3x3 = [1,2,3,4,5,6,7,8,9]
    range4x4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    range5x5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    range6x6 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    
    if board == range3x3:
        print()
        print('┌-----┐')
        print(f"|{board[0]}|{board[1]}|{board[2]}|")
        print('|-+-+-|')
        print(f"|{board[3]}|{board[4]}|{board[5]}|")
        print('|-+-+-|')
        print(f"|{board[6]}|{board[7]}|{board[8]}|")
        print('└-----┘')
        print()
    elif board == range4x4:
        print()
        print('┌-----------┐')
        print(f"| {board[0]}| {board[1]}| {board[2]}| {board[3]}|")
        print('|--+--+--+--|')
        print(f"| {board[4]}| {board[5]}| {board[6]}| {board[7]}|")
        print('|--+--+--+--|')
        print(f"| {board[8]}|{board[9]}|{board[10]}|{board[11]}|")
        print('|--+--+--+--|')
        print(f"|{board[12]}|{board[13]}|{board[14]}|{board[15]}|")
        print('└-----------┘')
        print()
      
    elif board == range5x5:
        print()
        print('┌--------------┐')
        print(f"| {board[0]}| {board[1]}| {board[2]}| {board[3]}| {board[4]}|")
        print('|--+--+--+--+--|')
        print(f"| {board[5]}| {board[6]}| {board[7]}| {board[8]}|{board[9]}|")
        print('|--+--+--+--+--|')
        print(f"|{board[10]}|{board[11]}|{board[12]}|{board[13]}|{board[14]}|")
        print('|--+--+--+--+--|')
        print(f"|{board[15]}|{board[16]}|{board[17]}|{board[18]}|{board[19]}|")
        print('|--+--+--+--+--|')
        print(f"|{board[20]}|{board[21]}|{board[22]}|{board[23]}|{board[24]}|")
        print('└--------------┘')
        print()
    elif board == range6x6:
        print()
        print('┌-----------------┐')
        print(f"| {board[0]}| {board[1]}| {board[2]}| {board[3]}| {board[4]}| {board[5]}|")
        print('|--+--+--+--+--+--|')
        print(f"| {board[6]}| {board[7]}| {board[8]}|{board[9]}|{board[10]}|{board[11]}|")
        print('|--+--+--+--+--+--|')
        print(f"|{board[12]}|{board[13]}|{board[14]}|{board[15]}|{board[16]}|{board[17]}|")
        print('|--+--+--+--+--+--|')
        print(f"|{board[18]}|{board[19]}|{board[20]}|{board[21]}|{board[22]}|{board[23]}|")
        print('|--+--+--+--+--+--|')
        print(f"|{board[24]}|{board[25]}|{board[26]}|{board[27]}|{board[28]}|{board[29]}|")
        print('|--+--+--+--+--+--|')
        print(f"|{board[30]}|{board[31]}|{board[32]}|{board[33]}|{board[34]}|{board[35]}|")
        print('└-----------------┘')
        print()
    else:
        pass
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def has_winner(board):
    range3x3 = [1,2,3,4,5,6,7,8,9]
    range4x4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    range5x5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    range6x6 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

    if board == range3x3:

        return (board[0] == board[1] == board[2] or
                board[3] == board[4] == board[5] or
                board[6] == board[7] == board[8] or
                board[0] == board[3] == board[6] or
                board[1] == board[4] == board[7] or
                board[2] == board[5] == board[8] or
                board[0] == board[4] == board[8] or
                board[2] == board[4] == board[6])

def make_move(player, board):
    range3x3 = [1,2,3,4,5,6,7,8,9]
    range4x4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    range5x5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    range6x6 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

    if board == range3x3:
        square = int(input(f"{player}'s turn to choose a square (1-9): "))
        board[square - 1] = player
    elif board == range4x4:
        square = int(input(f"{player}'s turn to choose a square (1-16): "))
        board[square - 1] = player
    elif board == range4x4:
        square = int(input(f"{player}'s turn to choose a square (1-25): "))
        board[square - 1] = player
    elif board == range4x4:
        square = int(input(f"{player}'s turn to choose a square (1-36): "))
        board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()