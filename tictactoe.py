
board= [["-"],["-"],["-"],
        ["-"],["-"],["-"],
        ["-"],["-"],["-"]]

currentplayer = "x"
winner = None
gammerun = True

def printboard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----------------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----------------")
    print(board[6] + "|" + board[7] + "|" + board[8])

def inputplayer(board): 
    inp = int(input("Enter a number 1-9"))




    
