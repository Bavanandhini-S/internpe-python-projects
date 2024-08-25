#tic tac toe game in python

#printing the game board

import random

def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
    print("-------------")

#check win or tie
#check in Horizonatl, vertical and diagonal
def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
    (board[3] == player and board[4] == player and board[5] == player) or \
    (board[6] == player and board[7] == player and board[8] == player) or \
    (board[0] == player and board[3] == player and board[6] == player) or \
    (board[1] == player and board[4] == player and board[7] == player) or \
    (board[2] == player and board[5] == player and board[8] == player) or \
    (board[0] == player and board[4] == player and board[8] == player) or \
    (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def check_tie(board):
    if " " not in board:
        return True
    else:
        return False

#computer board
    
def computer_move(board):
    empty_positions = [i for i in range(9) if board[i] == " "]
    return random.choice(empty_positions)

#switching board
    
def tic_tac_toe():
    board = [" " for _ in range(9)]
    player = "X"

    print_board(board)

    while True:
        if player == "X":
            move = input("It's " + player + "'s turn. Enter a position (1-9): ")
            move = int(move) - 1

        else:
            move = computer_move(board)

        if board[move] == " ":
            board[move] = player
            print_board(board)

            if check_win(board, player):
                print("congratulations player"  +  player  +  "wins!")
                break
            elif check_tie(board):
                print("It's a tie!")
                break
            else:
                player = "O" if player == "X" else "X"

        else:
            print("That position is already taken. Try again.")


tic_tac_toe()



            
        

            





    
    

                                                                                                                                                                                                    