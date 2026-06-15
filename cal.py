import tkinter as tk
from tkinter import messagebox

def on_click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)   
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalid Input")


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)


entry = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)


buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0

for btn in buttons:
    if btn == "C":
        action = clear
    elif btn == "=":
        action = calculate
    else:
        action = lambda x=btn: on_click(x)

    tk.Button(root, text=btn, width=5, height=2, font=("Arial", 14),
              command=action).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()