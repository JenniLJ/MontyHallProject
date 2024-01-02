import tkinter as tk
from gui import MontyHallGameGUI  # Ensure this matches the class name in gui.py

def main():
    root = tk.Tk()
    app = MontyHallGameGUI(root)  # Instantiate your GUI application
    root.mainloop()

if __name__ == "__main__":
    main()