# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.

import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        # Generate a random number between 1 and 100
        self.random_number = random.randint(1, 100)
        self.guess_count = 0

        # Label for instructions
        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack(padx=20, pady=10)

        # Entry widget for user input
        self.entry = tk.Entry(root)
        self.entry.pack(padx=20, pady=5)

        # Button to submit the guess
        self.guess_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.guess_button.pack(padx=20, pady=10)

        # Label to display result messages
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(padx=20, pady=10)

        # Button to restart the game
        self.restart_button = tk.Button(root, text="Restart Game", command=self.restart_game, state=tk.DISABLED)
        self.restart_button.pack(padx=20, pady=10)

    def check_guess(self):
        """Check the user's guess and provide feedback."""
        try:
            guess = int(self.entry.get())
            self.guess_count += 1

            if guess < self.random_number:
                self.result_label.config(text="Higher number please.")
            elif guess > self.random_number:
                self.result_label.config(text="Lower number please.")
            else:
                self.result_label.config(text=f"Correct! You guessed the number in {self.guess_count} attempts.")
                self.guess_button.config(state=tk.DISABLED)
                self.restart_button.config(state=tk.NORMAL)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def restart_game(self):
        """Restart the game with a new random number."""
        self.random_number = random.randint(1, 100)
        self.guess_count = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.guess_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
