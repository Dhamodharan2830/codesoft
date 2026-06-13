import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def update_task():
    try:
        selected = task_listbox.curselection()[0]
        new_task = task_entry.get().strip()

        if new_task:
            task_listbox.delete(selected)
            task_listbox.insert(selected, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter updated task!")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task first!")


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")


task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Add", width=10, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update", width=10, command=update_task).grid(row=0, column=1, padx=5)


task_listbox = tk.Listbox(root, width=45, height=15)
task_listbox.pack(pady=10)


tk.Button(root, text="Delete Selected", width=20, command=delete_task).pack(pady=5)

root.mainloop()