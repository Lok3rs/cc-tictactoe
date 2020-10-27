from checks import who_wins
from termcolor import colored

'''
for unbeatable AI option we've used minimax algorithm. Those two videos are really usefull with understanding that method
https://www.youtube.com/watch?v=trKjYdBASyQ
https://www.youtube.com/watch?v=l-hh51ncgDI
'''

# function for best "O" moves
def maximum(board):
    # starting maximum score for return (Minimax Algorithm)
    max_score = -2
    # checks who's winning the game, usefull for function recurtion
    result = who_wins(board)

    # assembling points for result
    if result == colored('X', "green"):
        return (-1, 0, 0)
    elif result == colored('O', "blue"):
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)

    # function checks every each move "profitability" by function recurtion
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '.':
                board[i][j] = colored('O', "blue")
                (m, min_i, min_j) = minimum(board)
                # getting best coordinates for next move
                if m > max_score:
                    max_score = m
                    row = i
                    column = j
                # reassembling marked place on a gameboard for "."
                board[i][j] = '.'
    return (max_score, row, column)

# opposite function for "X" moves
def minimum(board):
    min_score = 2


    result = who_wins(board)

    if result == colored('X', "green"):
        return (-1, 0, 0)
    elif result == colored('O', "blue"):
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '.':
                board[i][j] = colored('X', "green")
                (m, max_i, max_j) = maximum(board)
                if m < min_score:
                    min_score = m
                    row = i
                    column = j
                board[i][j] = '.'

    return (min_score, row, column)