"""
Program: Montyhallproject

Author: Jennifer Jarrell

Last date modified: 1/1/2024

The Monty Hall Problem is a game where you pick one of three doors to win a prize, 
usually a car, with the other two hiding goats. After you choose, the host, who knows where the prize is, 
opens another door revealing a goat. You then decide to stick with your initial choice or switch to the other unopened door.
Switching doors doubles your chances of winning from 33.33% to 66.66%. 
This Python project lets you play this game interactively using a graphical interface, 
making choices and seeing how your odds change, helping you learn about probability of this puzzle.
"""

import tkinter as tk
from gui import GameGUI 
from montyhall import final_choice, initialize_doors, reveal_goat, player_choice

def main():
    print("Welcome to the Monty Hall Problem Simulation!")

    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:
        doors = initialize_doors()
        print("There are 3 doors in front of you: Door 1, Door 2, and Door 3.")
        player_door = player_choice
        goat_door = reveal_goat(doors, player_door)
        print(f"The host reveals a goat behind Door {goat_door + 1}.")

        switch = input("Do you want to switch doors? (yes/no): ").lower() == "yes"
        win = final_choice(doors, player_door, switching=switch)

        if win:
            print("You win! The car was behind your final choice of door!")
        else:
            print("Sorry, you chose a goat! Better luck next time.")

        play_again = input("Do you want to play again? (yes/no): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()