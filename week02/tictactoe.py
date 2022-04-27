# Assignment: W02 Prove: Developer - Solo Code Submission
# Author: Nikkolet Ashby
# Purpose: Program plays Tic Tac Toe game for enjoyment of two users. 
# Date: 4/25/2022

#=======================================Modules============================================
import random
from tkinter import *
#==========================================================================================

def main():
    pass

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0] + " wins!"))

            elif check_winner() == "Tie":
                label.config(text="It's a tie!")


def check_winner():
    for row in range(3):
        if buttons[row][column][0]['text'] == buttons[row][1]['text'] == buttons[row][0]['text'] != "":
            return True
    
    for column in range(3):
        if buttons[0][column][0]['text'] == buttons[row][1]['text'] == buttons[row][0]['text'] != "":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons [2][2]['text'] != "":
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons [2][0]['text'] != "":
        return True
    
    elif empty_spaces() is False:
        return "Tie"

    else:
        return False


def empty_spaces():
    pass

def new_game():
    pass

window = Tk()
window.title("Tic Tac Toe")
players = ["X","O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text= player + "'s turn", font=('consolas',40))
label.pack(side="top")


reset_button = Button(text="restart", font=('consolas', 20), command = new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",  font=('consolas',40), width=5, height=2, command = lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)



window.mainloop()