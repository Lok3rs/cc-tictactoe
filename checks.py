from termcolor import colored

def has_won(board: list) -> bool:
    global winning_combinations
    # possible winning configurations
    winning_combinations = [[board[0][0], board[0][1], board[0][2]],
                            [board[1][0], board[1][1], board[1][2]],
                            [board[2][0], board[2][1], board[2][2]],
                            [board[0][0], board[1][0], board[2][0]],
                            [board[0][1], board[1][1], board[2][1]],
                            [board[0][2], board[1][2], board[2][2]],
                            [board[0][0], board[1][1], board[2][2]],
                            [board[0][2], board[1][1], board[2][0]]]
    for win in winning_combinations:
        if win.count(colored("X", "green")) == 3 or win.count(colored("O", "blue")) == 3:
            return True
    # that return will only work if for loop won't find any winning configuration
    return False

def is_full(board: list) -> bool:
    # for loop checking every row for empty slots. If there is empty slot returns false
    for row in board:
        if "." in row:
            return False
    return True

# function returning winning player mark (X or O)
def who_wins(board) -> str or None:
    # Vertical win
    for i in range(0, 3):
        if (board[0][i] != '.' and
            board[0][i] == board[1][i] and
            board[1][i] == board[2][i]):
            return board[0][i]

    # Horizontal win
    for i in range(0, 3):
        if (board[i].count("X") == 3):
            return colored('X', "green")
        elif (board[i].count("O") == 3):
            return colored('O', "blue")

    # Main diagonal win
    if (board[0][0] != '.' and
        board[0][0] == board[1][1] and
        board[0][0] == board[2][2]):
        return board[0][0]

    # Second diagonal win
    if (board[0][2] != '.' and
        board[0][2] == board[1][1] and
        board[0][2] == board[2][0]):
        return board[0][2]

    # Is whole board full?
    if not is_full(board):
        return None

    return '.'
     

    