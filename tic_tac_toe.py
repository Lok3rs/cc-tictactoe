import sys
import random

def init_board() -> list:
    return [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

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

def get_ai_move(board: list) -> tuple or None:
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

def mark(coordinates: tuple, player_mark: str, board: list) -> list:
    try:
        # checks if chosen coordinate isn't marked yet, if True replace "." by players mark
        if board[coordinates[0]][coordinates[1]] == ".":
            board[coordinates[0]][coordinates[1]] = player_mark    
        return board
    # exception for coordinates out of bounds
    except IndexError:
        return board

def has_won(board: list) -> bool:
    # possible winning configurations
    global winning_combinations
    winning_combinations = [[board[0][0], board[0][1], board[0][2]],
                            [board[1][0], board[1][1], board[1][2]],
                            [board[2][0], board[2][1], board[2][2]],
                            [board[0][0], board[1][0], board[2][0]],
                            [board[0][1], board[1][1], board[2][1]],
                            [board[0][2], board[1][2], board[2][2]],
                            [board[0][0], board[1][1], board[2][2]],
                            [board[0][2], board[1][1], board[2][0]]]
    for win in winning_combinations:
        if win[0] == win[1] == win[2] != '.':
            return True
    # that return will only work if for loop won't find any winning configuration
    return False

def is_full(board: list) -> bool:
    # for loop checking every row for empty slots. If there is empty slot returns false, because 
    for row in board:
        if "." in row:
            return False
    return True

def print_board(board: list) -> str:
    return(f'''  
        1    2    3  

    A    {board[0][0]} | {board[0][1]} | {board[0][2]}
       ----+---+----
    B    {board[1][0]} | {board[1][1]} | {board[1][2]}
       ----+---+----
    C    {board[2][0]} | {board[2][1]} | {board[2][2]}

    ''')

def print_result(board: list) -> str:
    if has_won(board):
        for win in winning_combinations:
            if win[0] == win[1] == win[2]:
                return f"{print_board(board)}\n\t{win[0]} has won!"
    return "It's a tie!"

def tictactoe_game(human_ai = False):
    game_board = init_board()
    player_1 = "X"
    player_2 = "O"
    win = has_won(game_board)
    full = is_full(game_board)

    while not win or not full:
        print(print_board(game_board))
        print("Player X turn:")
        coords = get_move(game_board)
        game_board = mark(coords, player_1, game_board)
        if has_won(game_board) or is_full(game_board):
            break
        print(print_board(game_board))
        print("Player O turn")
        if human_ai:
            coords = get_ai_move(game_board)
        else:
            coords = get_move(game_board)
        game_board = mark(coords, player_2, game_board)
        if has_won(game_board) or is_full(game_board):
            break
    
    print(print_result(game_board))

def main_menu():
    user_choose = input("Choose game option:\n 1 - Player vs. Player\n 2 - Player vs. AI\n")
    while user_choose not in ["1", "2"]:
        user_choose = input("Invalid choose. Try again.")
    if user_choose == "1":
        tictactoe_game()
    else:
        tictactoe_game(True)

if __name__ == "__main__":
    main_menu()
