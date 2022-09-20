'''
Tic-Tac-Toe: A Solution
Author: Angelica Leon
'''
def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or draw(board)):
        print_board(board)
        make_move(player, board)
        player = next_player(player)
    print_board(board)
    print("Good game. Thanks for playing!") 


def create_board():
    board = [ 1 ,2, 3,
              4 ,5, 6,
              7 ,8, 9]
    
    return board

def print_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("------")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("------")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def draw(board):
    for slot in board:
        for slot in range(9):
            if board[slot] != "x" and board[slot] != "o":
                return False
        return True 

def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    slot = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[slot - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
    

if __name__ == "__main__":
    main()




    
