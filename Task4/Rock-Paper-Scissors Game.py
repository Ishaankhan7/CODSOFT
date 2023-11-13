import tkinter as tk
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def user_choice_handler(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}\n{result}")
    update_scores(result)

def update_scores(result):
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    user_score_label.config(text=f"Your score: {user_score}")
    computer_score_label.config(text=f"Computer's score: {computer_score}")

user_score = 0
computer_score = 0

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

instruction_label = tk.Label(window, text="Choose rock, paper, or scissors:", font=("Arial", 16))
instruction_label.pack()

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: user_choice_handler("rock"))
rock_button.pack(side="left", padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: user_choice_handler("paper"))
paper_button.pack(side="left", padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: user_choice_handler("scissors"))
scissors_button.pack(side="left", padx=10)

result_label = tk.Label(window, text="", font=("Arial", 16))
result_label.pack()

user_score_label = tk.Label(window, text=f"Your score: {user_score}", font=("Arial", 14))
user_score_label.pack()

computer_score_label = tk.Label(window, text=f"Computer's score: {computer_score}", font=("Arial", 14))
computer_score_label.pack()

window.mainloop()
