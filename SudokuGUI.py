import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
#from constants import *
#from sudoku_generator import *
#from board_cell import *


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.root.geometry("540x610")  # Set window size

        # Load the background image
        self.background_image = Image.open("background_image.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a label to display the background image
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Main menu frame
        self.menu_frame = tk.Frame(root, bg="white")
        self.menu_frame.pack(pady=20)

        # Title text
        self.title_label = tk.Label(self.menu_frame, text="Welcome to Sudoku", bg="white", fg="black",
                                    font=("Arial", 30))
        self.title_label.pack(pady=(0, 20))

        # Instructions
        self.instruction_label = tk.Label(self.menu_frame, text="Select Game Mode:", bg="white", fg="black",
                                          font=("Arial", 20))
        self.instruction_label.pack()

        # Mode selection combobox
        self.mode_combobox = ttk.Combobox(self.menu_frame, values=["Easy", "Medium", "Hard"], font=("Arial", 16))
        self.mode_combobox.pack(pady=10)
        self.mode_combobox.set("Easy")

        # Start game button
        self.start_button = tk.Button(self.menu_frame, text="Start Game", command=self.start_game, font=("Arial", 16))
        self.start_button.pack(pady=10)

        # Quit game button
        self.quit_button = tk.Button(self.menu_frame, text="Quit Game", command=self.quit_game, font=("Arial", 16))
        self.quit_button.pack(pady=10)

    def start_game(self):
        mode = self.mode_combobox.get()
        if mode == "Easy":
            difficulty = 30
        elif mode == "Medium":
            difficulty = 40
        else:
            difficulty = 50

        self.root.destroy()  # Close the start menu window
        # Call the main function with selected difficulty
        main(difficulty)

    def quit_game(self):
        self.root.destroy()


def start_menu():
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

def main(difficulty):
    # Initialize your game logic here
    pass


if __name__ == "__main__":
    start_menu()