import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("_"*5)

def check_winner(board):
    #check for the rows
    for row in board:
        if row[0]==row[1]==row[2]!=" ":
            return True
    #check for the columns
    for col in range(3):
        if board[0][col]==board[1][col]== board[2][col]!=" ":
            return True
    #check for the diagonals
    if board[0][0]==board[1][1]==board[2][2]!=' ':
        return True
    if board[0][2]==board[1][1]==board[2][0]!=' ':
        return True
    return False

def get_empty_cells(board):
    empty_cells=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                 empty_cells.append((i,j))
    return empty_cells
            
def computer_move(board):
    empty_cells=get_empty_cells(board)
    row,col= random.choice(empty_cells)
    board[row][col]='O'

def user_move(board):
    while True:
        try:
            row =int(input("Enter the value of the row (0,1,2)"))
            col= int(input("Enter the value of the col (0,1,2)"))
            if board[row][col]==' ':
                board[row][col]='X'
                break
            else:
                print("Cell has already selected try again")
        except(ValueError,IndexError):
            print("Invalid input")
def play():
    board=[[" "for _ in range(3)]for _ in range(3)]
    print_board(board)
    while True:
        user_move(board)
        print_board(board)
        
        if check_winner(board):
            print("You won the game")
            break
        if len(get_empty_cells(board))==0:
            print('The match is a tie')
            break
        computer_move(board)
        print("Computers move")
        print_board(board)
        if check_winner(board):
            print("The computer has won the game")
            break
        if len(get_empty_cells(board))==0:
            print('The match is a tie')
            break
play()