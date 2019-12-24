#-----------Global Variables------------
#Game board
board = ["-","-","-",
                     "-","-","-",
                     "-","-","-"]

#If Game is still going
game_is_still_going = True

#who won
winner = None

#who 's turn is
current_player = "X"



 #----------Defined Functions---------------
def disp_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Handle a single turn of an arbitary player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a Position from 1 - 9 :")
    valid = False
    while not valid:
        while position not in ["1" ,"2","3","4","5","6","7","8","9"]:
            position = input("Invalid Input !!!! . Choose from 1-9")

        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't enter the value over there")

    board[position] = player
    disp_board()


def check_if_tie():
    #Setup Global Variable
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return

def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner

    #check rows
    row_winner = check_rows()
    #check col
    col_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        #there is row winner
        winner = row_winner
    elif col_winner:
        #there is col winner
        winner = col_winner
    elif diagonal_winner:
        #there is a diagonal winner
        winner = diagonal_winner
    else:
        #there is no win
        winner = None

    return

def check_rows():
    #Set up Global Variables
    global game_still_going

    row_1  =  board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #If any row match,Flag that there is a match
    if row_1 or row_2 or row_3 :
        game_still_going = False

     #Return the winner (X or 0)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return

def check_diagonals():
     #Set up Global Variables
    global game_still_going

    diag_1  =  board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    #If any diagonals match,Flag that there is a match
    if diag_1 or diag_2 :
        game_still_going = False

     #Return the winner (X or 0)
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]

    return

def check_columns():
     #Set up Global Variables
    global game_still_going

    col_1  =  board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    #If any col match,Flag that there is a match
    if col_1 or col_2 or col_3 :
        game_still_going = False

     #Return the winner (X or 0)
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return




def flip_player():
    #Set up Global Variables
    global  current_player

    #if the Current Player is X Flip it to O
    if current_player == "X":
        current_player = "O"
    #if the Current Player is O Flip it to X
    elif current_player == "O":
        current_player = "X"
    return

#-------------Actual Execution--------------
def play_game():
    #Setup of Global Variables
    global game_is_still_going

    #Display initial board
    disp_board()
   #while the game is still going
    while game_is_still_going:

        #handle a single turn of an arbitary player
        handle_turn(current_player)

        #Check if the game has ended
        check_if_game_over()

        #Flip to other Player
        flip_player()

        #The Game has Ended
        if winner == "X" or winner =="O":
            print(winner + "won.")
        elif winner == None:
            print("Tie")





play_game()

#Display Board
#board
#display Board
#play Game
#check win
    #check row
    #check column
    #check diagonals
#check tie
#flip Player
