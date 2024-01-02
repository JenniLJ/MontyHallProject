import random

def initialize_doors():
    # Randomly assign the prize to a door
    # Return doors state
    doors = [0, 0, 0] 
    prize_door = random.randint(0, 2)
    doors[prize_door] = 1 # Assign the prize behind one random door
    return doors

def player_choice(doors):
    # Take player's initial choice
    choice = int(input("Choose a door (1, 2, or 3): ")) - 1  # Subtract 1 for 0-indexed list
    return choice

def reveal_goat(doors, player_door):
    # Reveal a door that has a goat and is not the player's door
    possible_doors = [i for i in range(3) if i != player_door and doors[i] == 0]
    opened_door = random.choice(possible_doors)
    return opened_door

def final_choice(doors, initial_choice, switching=False):
    # If switching, change the player's choice
    # Return whether the player won or not
    if switching:
        # Change the player's choice to the other unopened, unrevealed door
        remaining_doors = [i for i in range(3) if i != initial_choice and i != reveal_goat(doors, initial_choice)]
        final_choice = remaining_doors[0]
    else:
        final_choice = initial_choice

    if doors[final_choice] == 1:
        return True  # The player wins
    else:
        return False  # The player loses
