# Rock-Paper-Scissors GUI
from tkinter import *
import random

def rps(user_choice):
    # Computer's choice: 1 for Rock, 2 for Paper, 3 for Scissors
    computer_choice = random.randint(1, 3)
    outcomes = {
        (1, 3): "Rock crushes Scissors. You win!",
        (1, 2): "Paper covers Rock. You lose!",
        (2, 1): "Paper covers Rock. You win!",
        (2, 3): "Scissors cut Paper. You lose!",
        (3, 2): "Scissors cut Paper. You win!",
        (3, 1): "Rock crushes Scissors. You lose!",
    }

    if user_choice == computer_choice:
        result.set("It's a draw! No points awarded.")
    else:
        result.set(outcomes.get((user_choice, computer_choice), ""))
        if (user_choice, computer_choice) in outcomes:
            score.set(score.get() + 1 if "win" in outcomes[(user_choice, computer_choice)] else score.get() - 1)

# GUI Setup
top = Tk()
top.title("Rock-Paper-Scissors by Md. Shafi Mahmud")
top.geometry("400x200")
top.resizable(False, False)

# Variables
result = StringVar()
result.set("Welcome to Rock-Paper-Scissors!")
score = IntVar()
score.set(0)

# Buttons
Label(top, text="Choose your move:").grid(row=0, column=1, pady=10)
Button(top, text="Rock", command=lambda: rps(1)).grid(row=1, column=0, padx=10)
Button(top, text="Paper", command=lambda: rps(2)).grid(row=1, column=1, padx=10)
Button(top, text="Scissors", command=lambda: rps(3)).grid(row=1, column=2, padx=10)

# Result display
Label(top, textvariable=result).grid(row=2, column=1, pady=10)

# Score display
Label(top, text="Your Score:").grid(row=3, column=0, pady=10)
Label(top, textvariable=score).grid(row=3, column=1, pady=10)

# Footer
Label(top, text="Rock-Paper-Scissors Game | By Md. Shafi Mahmud", fg="gray").grid(row=4, column=1, pady=20)

# Main loop
top.mainloop()
