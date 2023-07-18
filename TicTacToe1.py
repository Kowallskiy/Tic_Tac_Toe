import random
import sys

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

current_player = 'X'
# game_running variable will help to loop throug the game
game_running = True
winner = None

# The print_board function makes the board look user-friendly.
def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('_________')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('_________')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# The player finction receives an input from a user
def player(board):
    while True:
        inp = input('Enter a number from 1 to 9: ')
        if inp.isdigit():
            inp = int(inp)
            if 1 <= inp <= 9 and board[inp - 1] == '-':
                board[inp - 1] = current_player
                break
            else:
                print('Invalid number')
        else:
            print('Invalid input')        

# Check_horizontal, check_row and check_diag monitor the board
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True

def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True

def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

# This comp function allows to play against computer, but not very smart one
def comp(board):
    while current_player == 'O':
        rand = random.randint(0, 8)
        if board[rand] == '-':
            board[rand] = 'O'
            switch_player()
        elif '-' not in board:
            break

def check_winner(winner):
    global game_running
    if winner != None:
        print(print_board(board))
        print(f"{winner} won this game!")
        game_running = False
        sys.exit()

def check_tie(board):
    global game_running
    if '-' not in board:
        print_board(board)
        print('This is the draw!')
        game_running = False

def main():
    while game_running:
        print_board(board)
        player(board)
        check_horizontal(board)
        check_row(board)
        check_diag(board)
        check_winner(winner)
        switch_player()
        comp(board)
        check_horizontal(board)
        check_row(board)
        check_diag(board)
        check_winner(winner)
        check_tie(board)

main()
        