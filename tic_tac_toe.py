import time
import os
from sys import exit
from termcolor import colored
from prints import print_board, print_result, display_tictactoe_animation
from checks import has_won, is_full
from moves import get_ai_move, get_move, mark


def init_board() -> list:
    return [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

def tictactoe_game(human_ai = False, ai_ai = False):
    game_board = init_board()
    player_mark = "X"
    end_condition = False

    while not end_condition:
        if has_won(game_board) or is_full(game_board):
            end_condition = True
            continue
        os.system("clear || cls")
        print_board(game_board)
        print(f"Player {player_mark} turn:")
        if player_mark == "X":
            if ai_ai:
                time.sleep(1)
                coords = get_ai_move(game_board)
            else:
                coords = get_move(game_board)
            game_board = mark(coords, player_mark, game_board)
            player_mark = "O"
            continue
        if player_mark == "O":
            if human_ai:
                time.sleep(1)
                coords = get_ai_move(game_board, unbeatable_ai=True)
            elif ai_ai:
                time.sleep(1)
                coords = get_ai_move(game_board)
            else:
                coords = get_move(game_board)
            game_board = mark(coords, player_mark, game_board)
            player_mark = "X"
        
    os.system("clear || cls")
    print_result(game_board)

def main_menu():
    os.system("clear || cls")
    display_tictactoe_animation()
    tabs = "\t" * 7
    print(colored(f"{tabs}Choose game option:\n", "cyan"), colored(f"{tabs} 1 - Player vs. Player\n", "green"), colored(f"{tabs} 2 - Player vs. AI\n", "blue"),colored(f"{tabs} 3 - AI vs AI\n", "yellow"), colored(f"{tabs} 0 - exit\n","red"))
    user_choose = input(tabs)
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
        while user_choose.upper() not in ["Y", "N"]:
            user_choose = input("Invalid input, try again.\t")
        if user_choose.upper() == "Y":
            continue
        else:
            os.system("clear || cls")
            exit("Thanks for playing! See you again!")

