import sys
import random

from minimax import minimum, maximum
from checks import is_full

def get_move(board: list) -> tuple:
    rows_dict = {"A": 0, "B": 1, "C": 2}
    allowed_to_choose = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    while True:
        user_input = input("Provide coordinates (quit to close program):  ")
        if user_input.lower() == "quit":
            sys.exit("See you again!")
        # checks if user provide a valid coordinates
        if user_input.upper() in allowed_to_choose:
            coordinates = (rows_dict[user_input[0].upper()], int(user_input[1])-1)
            # if he does, checks if they are unmarked yet. If yes, returns them
            if board[coordinates[0]][coordinates[1]] == ".":
                return coordinates
            else:
                print(f"Sorry, chosen coordinates are already marked by {board[coordinates[0]][coordinates[1]]}")
        else:
            print("Invalid coordinates, try again.")

def get_ai_move(board: list, unbeatable_ai = False) -> tuple or None:
    global win_indexes
    win_indexes = [[(0, 0), (0, 1), (0, 2)],
                [(1, 0), (1,1), (1, 2)],
                [(2, 0), (2, 1), (2, 2)],
                [(0, 0), (1, 0), (2, 0)],
                [(0, 1), (1, 1), (2, 1)],
                [(0, 2), (1, 2), (2, 2)],
                [(0, 0), (1, 1), (2, 2)],
                [(0, 2), (1, 1), (2, 0)],
                ]
    if not unbeatable_ai:
        for win in win_indexes:
            cur_combination = [board[win[0][0]][win[0][1]], board[win[1][0]][win[1][1]], board[win[2][0]][win[2][1]]]
            if cur_combination.count("O") == 2 and "." in cur_combination:
                return win[cur_combination.index(".")]
            elif cur_combination.count("X") == 2 and "." in cur_combination:
                return win[cur_combination.index(".")]

        coordinates = (random.randint(0, 2), random.randint(0, 2))
        if is_full(board):
            return None
        while board[coordinates[0]][coordinates[1]] != ".":
            coordinates = (random.randint(0, 2), random.randint(0, 2))
        return coordinates
    else:
        (m, row, column) = maximum(board)
        print(row, column)
        return (row, column)

def mark(coordinates: tuple, player_mark: str, board: list) -> list:
    try:
        # checks if chosen coordinate isn't marked yet, if True replace "." by players mark
        if board[coordinates[0]][coordinates[1]] == ".":
            board[coordinates[0]][coordinates[1]] = player_mark    
        return board
    # exception for coordinates out of bounds
    except IndexError:
        return board