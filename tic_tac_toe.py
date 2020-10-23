import time
import os

from prints import print_board, print_result, display_tictactoe_animation
from checks import has_won, is_full
from moves import get_ai_move, get_move, mark


def init_board() -> list:
    return [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

def tictactoe_game(human_ai = False, ai_ai = False):
    game_board = init_board()
    player_1 = "X"
    player_2 = "O"
    end_condition = False

    while not end_condition:
        os.system("clear || cls")
        print_board(game_board)
        print("Player X turn:")
        if ai_ai:
            time.sleep(1)
            coords = get_ai_move(game_board)
        else:
            coords = get_move(game_board)
        game_board = mark(coords, player_1, game_board)
        if has_won(game_board) or is_full(game_board):
            end_condition = True
            continue
        os.system("clear || cls")
        print_board(game_board)
        print("Player O turn")
        if human_ai:
            time.sleep(1)
            coords = get_ai_move(game_board, unbeatable_ai=True)
        elif ai_ai:
            time.sleep(1)
            coords = get_ai_move(game_board)
        else:
            coords = get_move(game_board)
        game_board = mark(coords, player_2, game_board)
        if has_won(game_board) or is_full(game_board):
            end_condition = True

    os.system("clear || cls")
    print_result(game_board)

def main_menu():
    os.system("clear || cls")
    display_tictactoe_animation()
    user_choose = input("Choose game option:\n 1 - Player vs. Player\n 2 - Player vs. AI\n 3 - AI vs AI\n")
    while user_choose not in ["1", "2", "3"]:
        user_choose = input("Invalid choose. Try again.")
    os.system("clear || cls")
    if user_choose == "1":
        tictactoe_game()
    elif user_choose == "2":
        tictactoe_game(human_ai= True)
    else:
        tictactoe_game(ai_ai=True)

if __name__ == "__main__":
    main_menu()