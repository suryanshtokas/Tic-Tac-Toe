import sys

board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]

# Create a dictionary to find the place on the board from tl, tr, etc.
movesDict = {
    'tl':0, 'tc':1, 'tr':2, 'cl':3,
    'c':4, 'cr':5, 'bl':6,
    'bc':7, 'br':8
}

# Making the tictactoe board
def print_board():
    print(f""" {board[0]} | {board[1]} | {board[2]} """)
    print(f""" {board[3]} | {board[4]} | {board[5]} """)
    print(f""" {board[6]} | {board[7]} | {board[8]} \n""")

def check_result():
    global closeGame
    closeGame = False
    # Check horizontally
    if board[0] == board[1] == board[2] == 'X' or board[0] == board[1] == board[2] == 'O':
        if board[0] == 'X':
            print(f'\nYou Win! :-)')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)
        else:
            print(f'\nYou Lose :(')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)

    elif board[3] == board[4] == board[5] == 'X' or board[3] == board[4] == board[5] == 'O':
        if board[3] == 'X':
            print(f'\nYou Win! :-)')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)
        else:
            print(f'\nYou Lose :(')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)
    elif board[6] == board[7] == board[8] == 'X' or board[6] == board[7] == board[8] == 'O':
        if board[6] == 'X':
            print(f'\nYou Win! :-)')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)
        else:
            print(f'\nYou Lose :(')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)


    # Check Vertically
    elif board[0] == board[3] == board[6] == 'X' or board[0] == board[3] == board[6] == 'O':
        if board[0] == 'X':
            print(f'\nYou Win! :-)')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)
        else:
            print(f'\nYou Lose :(')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)
    elif board[1] == board[4] == board[7] == 'X' or board[1] == board[4] == board[7] == 'O':
        if board[1] == 'X':
            print(f'\nYou Win! :-)')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)
        else:
            print(f'\nYou Lose :(')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)
    elif board[2] == board[5] == board[8] == 'X' or board[2] == board[5] == board[8] == 'O':
        if board[2] == 'X':
            print(f'\nYou Win! :-)')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)
        else:
            print(f'\nYou Lose :(')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)

    # Check Diagonals
    elif board[0] == board[4] == board[8] == 'X' or board[0] == board[4] == board[8] == 'O':
        if board[0] == 'X':
            print(f'\nYou Win! :-)')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)
        else:
            print(f'\nYou Lose :(')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)
    elif board[2] == board[4] == board[6] == 'X' or board[2] == board[4] == board[6] == 'O':
        if board[2] == 'X':
            print(f'\nYou Win! :-)')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)
        else:
            print(f'\nYou Lose :(')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)

    elif '-' not in board:
            print(f'''\nIt's a tie''')
            closeQues = input('Do you want to quit (y/n)')
            if closeQues == 'y':
                sys.exit()
            else:
                closeGame = True
                print(board)


def algorithm(board):
    # Divide the board into rows, columns and Diagonals
    # Rows
    row1 = [board[0], board[1], board[2]]
    row2 = [board[3], board[4], board[5]]
    row3 = [board[6], board[7], board[8]]

    # columns
    col1 = [board[0], board[3], board[6]]
    col2 = [board[1], board[4], board[7]]
    col3 = [board[2], board[5], board[8]]

    # Diagonals
    diag1 = [board[0], board[4], board[8]]
    diag2 = [board[2], board[4], board[6]]

    # Check if the AI can win.
    # If it can, do it.
    # Otherwise stop the player from winning
    # If the player can't win try to take space on the board
    if row1[0] == row1[1] == 'O' and row1[2] == '-':
        return 2
    if row1[2] == row1[1] == 'O' and row1[0] == '-':
        return 0
    if row1[0] == row1[2] == 'O' and row1[1] == '-':
        return 1

    # Check the middle row and return a value accordingly
    if row2[0] == row2[1] == 'O' and row2[2] == '-':
        return 5
    if row2[2] == row2[1] == 'O' and row2[0] == '-':
        return 3
    if row2[0] == row2[2] == 'O' and row2[1] == '-':
        return 4

    # Check the bottom row and return a value accordingly
    if row3[0] == row3[1] == 'O' and row3[2] == '-':
        return 8
    if row3[2] == row3[1] == 'O' and row3[0] == '-':
        return 6
    if row3[0] == row3[2] == 'O' and row3[1] == '-':
        return 7

    # Check Columns
    # Check the top col and return a value accordingly
    if col1[0] == col1[1] == 'O' and col1[2] == '-':
        return 6
    if col1[2] == col1[1] == 'O' and col1[0] == '-':
        return 0
    if col1[0] == col1[2] == 'O' and col1[1] == '-':
        return 3

    # Check the middle col and return a value accordingly
    if col2[0] == col2[1] == 'O' and col2[2] == '-':
        return 7
    if col2[2] == col2[1] == 'O' and col2[0] == '-':
        return 1
    if col2[0] == col2[2] == 'O' and col2[1] == '-':
        return 4

    # Check the bottom col and return a value accordingly
    if col3[0] == col3[1] == 'O' and col3[2] == '-':
        return 8
    if col3[2] == col3[1] == 'O' and col3[0] == '-':
        return 2
    if col3[0] == col3[2] == 'O' and col3[1] == '-':
        return 5

    #Check Diagonals
    # Check the top left diagonal and return a value accordingly
    if diag1[0] == diag1[1] == 'O' and diag1[2] == '-':
        return 8
    if diag1[2] == diag1[1] == 'O' and dia1g[0] == '-':
        return 0
    if diag1[0] == diag1[2] == 'O' and diag1[1] == '-':
        return 4

    # Check the top right diagonal and return a value accordingly
    if diag2[0] == diag2[1] == 'O' and diag2[2] == '-':
        return 6
    if diag2[2] == diag2[1] == 'O' and diag2[0] == '-':
        return 2
    if diag2[0] == diag2[2] == 'O' and diag2[1] == '-':
        return 4


    # Check if the player can win.
    # Check Rows
    # Check the top row and return a value accordingly
    elif row1[0] == row1[1] == 'X' and row1[2] == '-':
        return 2
    elif row1[2] == row1[1] == 'X' and row1[0] == '-':
        return 0
    elif row1[0] == row1[2] == 'X' and row1[1] == '-':
        return 1

    # Check the middle row and return a value accordingly
    elif row2[0] == row2[1] == 'X' and row2[2] == '-':
        return 5
    elif row2[2] == row2[1] == 'X' and row2[0] == '-':
        return 3
    elif row2[0] == row2[2] == 'X' and row2[1] == '-':
        return 4

    # Check the bottom row and return a value accordingly
    elif row3[0] == row3[1] == 'X' and row3[2] == '-':
        return 8
    elif row3[2] == row3[1] == 'X' and row3[0] == '-':
        return 6
    elif row3[0] == row3[2] == 'X' and row3[1] == '-':
        return 7

    # Check Columns
    # Check the top col and return a value accordingly
    elif col1[0] == col1[1] == 'X' and col1[2] == '-':
        return 6
    elif col1[2] == col1[1] == 'X' and col1[0] == '-':
        return 0
    elif col1[0] == col1[2] == 'X' and col1[1] == '-':
        return 3

    # Check the middle col and return a value accordingly
    elif col2[0] == col2[1] == 'X' and col2[2] == '-':
        return 1
    elif col2[2] == col2[1] == 'X' and col2[0] == '-':
        return 7
    elif col2[0] == col2[2] == 'X' and col2[1] == '-':
        return 3

    # Check the bottom col and return a value accordingly
    elif col3[0] == col3[1] == 'X' and col3[2] == '-':
        return 2
    elif col3[2] == col3[1] == 'X' and col3[0] == '-':
        return 8
    elif col3[0] == col3[2] == 'X' and col3[1] == '-':
        return 5

    #Check Diagonals
    # Check the top left diagonal and return a value accordingly
    elif diag1[0] == diag1[1] == 'X' and diag1[2] == '-':
        return 8
    elif diag1[2] == diag1[1] == 'X' and dia1g[0] == '-':
        return 0
    elif diag1[0] == diag1[2] == 'X' and diag1[1] == '-':
        return 4

    # Check the top right diagonal and return a value accordingly
    elif diag2[0] == diag2[1] == 'X' and diag2[2] == '-':
        return 6
    elif diag2[2] == diag2[1] == 'X' and diag2[0] == '-':
        return 2
    elif diag2[0] == diag2[2] == 'X' and diag2[1] == '-':
        return 4

    # Check if there are any O's on the board
    Ocheck = 0
    Onum = 0
    if 'O' in board:
        for i in range(0, len(board)):
            if board[i] == 'O':
                Ocheck = i
                Onum += 1
        if Onum == 1 or Onum == 2:
            if board[7] == 'X' and board[6] == '-':
                return 6
            else:
                if Ocheck == 4 and board[1] == '-':
                    return 1
                elif Ocheck == 4 and board[7] == '-':
                    return 0

                if Ocheck == 0 and board[4] == '-':
                    return 4
                else:
                    return 2

    # If there are no O's on the board
    # Place an O on the center or on the top left corner
    # This will work because there will be no O's in only the first turn
    else:
        if board[4] == '-':
            return 4
        else:
            return 0
moveTick = 1
runFlag = True
while runFlag:
    if moveTick >= 2:
        moveTick = 1
    else:
        moveTick += 1
    print_board()
    check_result()
    if closeGame:
        board = [
            '-', '-', '-',
            '-', '-', '-',
            '-', '-', '-'
        ]

    whereMove = input('Where do you want to play your next move\nFor example- tl for top left  - ')
    try:
        if board[movesDict[whereMove]] == '-':

            board[movesDict[whereMove]] = 'X'
        elif board[movesDict[whereMove]] != '-':
            print('\nYou cannot change a previously entered value')
            continue
    except:
        print('Please enter a valid location')
    algValue = algorithm(board)
    if algValue != None:
        board[algValue] = 'O'
    else:
        pass
