# Assignment: W02 Prove: Developer - Solo Code Submission
# Author: Nikkolet Ashby
# Purpose: Program plays Tic Tac Toe game for enjoyment of two users. 
# Date: 4/27/2022

#=======================================Modules============================================
# import colorama
# from colorama import Fore, Back, Style
# colorama.init(autoreset=True)

from tkinter import *
from tkinter import messagebox

#==========================================================================================
clicked = True
count = 0
root = Tk()
root.title('Tic Tac Toe Game')

def main():
   
    root.mainloop()
    reset()

def reset():
    global root
    global b1, b2 , b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    b1 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b9))
    b10 = Button(root, text="Reset", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b10))

    #Grid buttons unto screen
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

def disableButtons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkIfWon():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global winner
    winner = False
    #Is X the winner?
    #Row
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("X wins!", "Congratulations!!!")
        disableButtons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("X wins!", "Congratulations!!!")
        disableButtons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("X wins!", "Congratulations!!!")
        disableButtons()
    #Column
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("X wins!", "Congratulations!!!")
        disableButtons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("X wins!", "Congratulations!!!")
        disableButtons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("X wins!", "Congratulations!!!")
        disableButtons()
    #Diagonal
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("X wins!", "Congratulations!!!")
        disableButtons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("X wins!", "Congratulations!!!")
        disableButtons()

    # Is O the winner?
    #Row
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("O wins!", "Congratulations!!!")
        disableButtons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("O wins!", "Congratulations!!!")
        disableButtons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("O wins!", "Congratulations!!!")
        disableButtons()
    #Column
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("O wins!", "Congratulations!!!")
        disableButtons()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("O wins!", "Congratulations!!!")
        disableButtons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("O wins!", "Congratulations!!!")
        disableButtons()
    #Diagonals
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("O wins!", "Congratulations!!!")
        disableButtons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("O wins!", "Congratulations!!!")
        disableButtons()
    
def checkIfTie():
    if count == 9 and winner == False:
        messagebox.showinfo("Tie!", "So Close!!!")
        disableButtons()        
    #Diagonal
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("O wins!", "Congratulations!!!")
        disableButtons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("O wins!", "Congratulations!!!")
        disableButtons()
    
#Button Clicked Function
def b_click(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkIfWon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkIfWon()
    else:
        messagebox.showerror("Oops! Sorry this has already been selected! Try again!")


b1 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b9))
b10 = Button(root, text="Reset", font=("Helvetica", 20), height= 3, width=6, bg="white", command= lambda: b_click(b10))

#Grid buttons unto screen
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

my_menu = Menu(root)
root.config(menu=my_menu)

#Create Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label = "Options", menu=options_menu)
options_menu.add_command(label = "Reset Game", command=reset)
# root.mainloop()

main()