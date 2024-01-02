import random

def initialize_doors():
    # Randomly assign the prize to a door
    doors = [0, 0, 0]
    prize_door = random.randint(0, 2)
    doors[prize_door] = 1  # Assign the prize behind one random door
    return doors

def reveal_goat(doors, player_door):
    # Determine which goat door Monty will open
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
