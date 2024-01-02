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