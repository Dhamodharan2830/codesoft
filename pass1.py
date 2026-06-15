import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Weak Length",
                "Password length should be at least 4 for strength."
            )
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        password_var.set(password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")



root = tk.Tk()
root.title("Password Generator")
root.geometry("400x220")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)


length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root, width=20)
length_entry.pack(pady=5)


generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password
)
generate_btn.pack(pady=10)


password_var = tk.StringVar()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    width=35,
    font=("Arial", 12)
)
password_entry.pack(pady=10)

root.mainloop()