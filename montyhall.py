import random

def initialize_doors():
    doors = [0, 0, 0]
    prize_door = random.randint(0, 2)
    doors[prize_door] = 1  
    return doors

def player_choice():
    while True:  
        try:
            choice = int(input("Choose a door (1, 2, or 3): ")) - 1  # Subtract 1 for 0-indexed list
            if choice in [0, 1, 2]:  
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:  
            print("Invalid input. Please enter a number.")

def reveal_goat(doors, player_door):
    possible_doors = [i for i in range(3) if i != player_door and doors[i] == 0]
    return random.choice(possible_doors)

def final_choice(doors, initial_choice, switch):
    if switch:
        remaining_doors = [i for i in range(3) if i != initial_choice and doors[i] != 1]
        final_choice = remaining_doors[0]
    else:
        final_choice = initial_choice

    win = doors[final_choice] == 1

    return win, 2/3 if switch else 1/3 
