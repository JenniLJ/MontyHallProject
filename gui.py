import tkinter as tk
from montyhall import initialize_doors, reveal_goat

class GameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Monty Hall Game")

        self.doors = [0, 0, 0]
        self.user_choice = None
        self.remaining_door = None

        self.door_choice_label = tk.Label(master, text="Choose a door (1, 2, or 3):")
        self.door_choice_entry = tk.Entry(master)
        self.play_button = tk.Button(master, text="Play", command=self.start_game)
        self.result_label = tk.Label(master, text="Results will be displayed here.")
        self.probability_label = tk.Label(master, text="Probability of winning will be shown here.")
        self.switch_button = tk.Button(master, text="Switch", command=self.switch_doors)
        self.stick_button = tk.Button(master, text="Stick", command=self.stick_with_door)

        self.door_choice_label.pack()
        self.door_choice_entry.pack()
        self.play_button.pack()
        self.result_label.pack()
        self.probability_label.pack()

    def start_game(self):
        self.doors = initialize_doors()
        self.result_label.config(text="Good luck!")
        self.probability_label.config(text="")

        try:
            self.user_choice = int(self.door_choice_entry.get()) - 1  # Convert to 0-index
            if self.user_choice not in [0, 1, 2]:
                raise ValueError("Invalid door choice")
        except ValueError:
            self.result_label.config(text="Please enter a valid door number (1, 2, or 3).")
            return

        self.remaining_door = reveal_goat(self.doors, self.user_choice)
        self.result_label.config(text=f"Monty opens door {self.remaining_door + 1} revealing a goat. Do you want to switch or stick?")
        self.switch_button['state'] = tk.NORMAL
        self.stick_button['state'] = tk.NORMAL
        self.switch_button.pack()
        self.stick_button.pack()

    def switch_doors(self):
        self.final_choice(not self.user_choice)

    def stick_with_door(self):
        self.final_choice(self.user_choice)

    def final_choice(self, final_choice):
        win, probability = final_choice(self.doors, self.user_choice, final_choice != self.user_choice)
        result_text = "Congratulations! You won!" if win else "Sorry, you lost."
        self.result_label.config(text=result_text)
        self.probability_label.config(text=f"Probability of winning: {probability*100:.2f}%")
        self.switch_button['state'] = tk.DISABLED
        self.stick_button['state'] = tk.DISABLED

if __name__ == "__main__":
    root = tk.Tk()
    game = GameGUI(root)
    root.mainloop()