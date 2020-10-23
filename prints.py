from checks import has_won

def print_board(board: list) -> None:
    return print(f'''  
        1    2    3  
    A    {board[0][0]} | {board[0][1]} | {board[0][2]}
       ----+---+----
    B    {board[1][0]} | {board[1][1]} | {board[1][2]}
       ----+---+----
    C    {board[2][0]} | {board[2][1]} | {board[2][2]}
    ''')

def print_result(board: list) -> None:
    winning_combinations = [[board[0][0], board[0][1], board[0][2]],
                            [board[1][0], board[1][1], board[1][2]],
                            [board[2][0], board[2][1], board[2][2]],
                            [board[0][0], board[1][0], board[2][0]],
                            [board[0][1], board[1][1], board[2][1]],
                            [board[0][2], board[1][2], board[2][2]],
                            [board[0][0], board[1][1], board[2][2]],
                            [board[0][2], board[1][1], board[2][0]]]
    if has_won(board):
        for win in winning_combinations:
            if win.count("X") == 3 or win.count("O") == 3:
                return print_board(board), print(f"\t{win[0]} has won!")
    
    return print_board(board), print("\tIt's a tie!")
