import time
import os
from sys import exit

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
    tabs = "\t" * 7
    user_choose = input(f"{tabs}Choose game option:\n{tabs} 1 - Player vs. Player\n{tabs} 2 - Player vs. AI\n{tabs} 3 - AI vs AI\n{tabs} 0 - exit\n{tabs}")
    while user_choose not in ["1", "2", "3", "0"]:
        user_choose = input("Invalid choose. Try again.")
    os.system("clear || cls")
    if user_choose == "0":
        exit("Thanks for playing! See you again!")
    elif user_choose == "1":
        tictactoe_game()
    elif user_choose == "2":
        tictactoe_game(human_ai= True)
    else:
        tictactoe_game(ai_ai=True)

if __name__ == "__main__":
    
    while True:
        main_menu()
        valid_inputs = ["Y", "N"]
        user_choose = input("Do you want to play again? (Y / N)\n")
        while user_choose.upper() not in valid_inputs:
            user_choose = input("Invalid input, try again.\t")
        if user_choose.upper() == "Y":
            continue
        else:
            os.system("clear || cls")
            exit("Thanks for playing! See you again!")

