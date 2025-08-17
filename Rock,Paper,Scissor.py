import tkinter as tk
import random

options = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    comp_choice = random.choice(options)
    result = ""

    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    user_label.config(text=f"You: {user_choice}")
    comp_label.config(text=f"Computer: {comp_choice}")
    result_label.config(text=result)

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.config(bg="#fdf0d5")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#fdf0d5", fg="#6a040f")
title.pack(pady=20)

user_label = tk.Label(root, text="You: ", font=("Arial", 14), bg="#fdf0d5")
user_label.pack()

comp_label = tk.Label(root, text="Computer: ", font=("Arial", 14), bg="#fdf0d5")
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="#e85d04", bg="#fdf0d5")
result_label.pack(pady=10)

btn_frame = tk.Frame(root, bg="#fdf0d5")
btn_frame.pack(pady=20)

for choice in options:
    tk.Button(btn_frame, text=choice, font=("Arial", 14), width=10, bg="#6a994e", fg="white",
              command=lambda c=choice: play(c)).pack(side="left", padx=10)

root.mainloop()
