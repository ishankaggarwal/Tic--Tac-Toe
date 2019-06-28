# Global variables

# Game Board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# If game is still going
game_still_going = True

# Will tell if there is a winner or a tie
winner = None

#Tells us who the current player is(X goes first)
current_player = 'X'

#----Functions----

def display_board():
    print('\n')
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
    print('\n')


def play_game():
          
    # display initial board
    display_board()

    # while the game is still going
    while game_still_going:
        
        # Allows the player to make his move
        handle_turn(current_player)

        # Check if the game has ended or not
        check_if_game_over()

        # Gives the turn to other player
        flip_player()

    # Game is over
    if winner == 'X' or winner == 'O':
        print(winner + ' won')
    elif winner is None:
        print('There is a tie')


# Allows the player to make his move
def handle_turn(player):
          
    # display the current player
    print(player + "'s turn")

    position = input('Enter a position from 1-9: ')

    # Make sure the input entered by the user is a valid one
    valid = False

    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Invalid position.Choose the position from 1-9 again:')

        # Get the correct index
        position = int(position) - 1

        if board[position] == '-':
            valid = True
        else:
            print("You can't go there. Go again.")
          
    # Put X or O in it's place
    board[position] = player

    display_board()


def check_if_game_over():
    check_for_win()
    check_for_tie()


def check_for_win():
          
    # using global winner variable
    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
          
    global game_still_going

    # checking if any row has all the same values or not
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    # if any row is similar then stop the game
    if row_1 or row_2 or row_3:
        game_still_going = False

    # return the winner(X or O)
    if row_1:
        return board[0]

    elif row_2:
        return board[3]

    elif row_3:
        return board[6]
          
    else:
        return None
          
def check_columns():
          
    global game_still_going

    # checking if any column has all the same values or not
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    # if any column is similar then stop the game
    if column_1 or column_2 or column_3:
        game_still_going = False

    # return the winner(X or O)
    if column_1:
        return board[0]

    elif column_2:
        return board[1]

    elif column_3:
        return board[2]

    else:
          return None


def check_diagonals():
          
    global game_still_going

    # checking if any diagonal has all the same values or not
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'

    # if any diagonal is similar then stop the game
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return the winner(X or O)
    if diagonal_1:
        return board[0]

    elif diagonal_2:
        return board[2]

    else:
          return None


def flip_player():
          
    global current_player

    # if the current player was X change it and vice-versa
    if current_player == 'X':
        current_player = 'O'

    elif current_player == 'O':
        current_player = 'X'


def check_for_tie():
          
    global game_still_going

    # Board is full
    if '-' not in board:
        game_still_going = False
        return True

    else:
          return False


# Calling this function to start the game
play_game()
