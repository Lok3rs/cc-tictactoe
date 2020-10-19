def init_board() -> list:
    return [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

def get_move(board: list) -> tuple:
    rows_dict = {"A": 0, "B": 1, "C": 2}
    allowed_to_choose = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    while True:
        user_input = input("Provide coordinates:  ")
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
                return f"{win[0]} has won!"
    return "It's a tie!"

def tictactoe_game():
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
        coords = get_move(game_board)
        game_board = mark(coords, player_2, game_board)
        if has_won(game_board) or is_full(game_board):
            break
    

    print(print_result(game_board))

if __name__ == "__main__":
    tictactoe_game()

    