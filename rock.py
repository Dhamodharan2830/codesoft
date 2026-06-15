import random
import tkinter as tk
from tkinter import messagebox

user_score = 0
computer_score = 0

def play_round(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice == computer_choice:
        result_text = "🤝 It's a tie!"
    elif (user_choice, computer_choice) in [
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock")
    ]:
        result_text = "🎉 You win this round!"
        user_score += 1
    else:
        result_text = "💻 Computer wins this round!"
        computer_score += 1

    result_label.config(
        text=f"You chose: {user_choice}\n"
             f"Computer chose: {computer_choice}\n\n"
             f"{result_text}"
    )

    score_label.config(
        text=f"📊 Score -> You: {user_score} | Computer: {computer_score}"
    )

def exit_game():
    messagebox.showinfo(
        "Game Over",
        f"Final Score\nYou: {user_score}\nComputer: {computer_score}"
    )
    root.destroy()

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")

tk.Label(root,
         text="🎮 Rock–Paper–Scissors",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root,
         text="rock beats scissors\nscissors beats paper\npaper beats rock").pack()

frame = tk.Frame(root)
frame.pack(pady=20)

for i, choice in enumerate(["rock", "paper", "scissors"]):
    tk.Button(
        frame,
        text=choice.capitalize(),
        width=10,
        command=lambda c=choice: play_round(c)
    ).grid(row=0, column=i, padx=5)

result_label = tk.Label(root, font=("Arial", 11))
result_label.pack(pady=15)

score_label = tk.Label(
    root,
    text="📊 Score -> You: 0 | Computer: 0",
    font=("Arial", 12, "bold")
)
score_label.pack(pady=10)

tk.Button(
    root,
    text="Exit Game",
    bg="red",
    fg="white",
    command=exit_game
).pack(pady=10)

root.mainloop()