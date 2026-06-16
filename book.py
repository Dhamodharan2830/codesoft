import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


con = sqlite3.connect("contacts.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS contacts(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
phone TEXT,
email TEXT,
address TEXT)
""")
con.commit()

selected_id = None


def load():
    tree.delete(*tree.get_children())
    for row in cur.execute("SELECT * FROM contacts"):
        tree.insert("", tk.END, values=row)

def clear():
    global selected_id
    selected_id = None
    name.set("")
    phone.set("")
    email.set("")
    address.set("")

def add():
    if not name.get() or not phone.get():
        messagebox.showerror("Error", "Name and Phone required")
        return

    cur.execute(
        "INSERT INTO contacts(name,phone,email,address) VALUES(?,?,?,?)",
        (name.get(), phone.get(), email.get(), address.get())
    )
    con.commit()
    load()
    clear()

def select(e):
    global selected_id

    item = tree.focus()
    if item:
        data = tree.item(item)["values"]

        selected_id = data[0]

        name.set(data[1])
        phone.set(data[2])
        email.set(data[3])
        address.set(data[4])

def update():
    if selected_id is None:
        return

    cur.execute("""
    UPDATE contacts
    SET name=?, phone=?, email=?, address=?
    WHERE id=?
    """, (
        name.get(),
        phone.get(),
        email.get(),
        address.get(),
        selected_id
    ))

    con.commit()
    load()
    clear()

def delete():
    if selected_id is None:
        return

    cur.execute(
        "DELETE FROM contacts WHERE id=?",
        (selected_id,)
    )

    con.commit()
    load()
    clear()

def search():
    tree.delete(*tree.get_children())

    key = search_var.get()

    cur.execute("""
    SELECT * FROM contacts
    WHERE name LIKE ? OR phone LIKE ?
    """, (f"%{key}%", f"%{key}%"))

    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)


root = tk.Tk()
root.title("Contact Management System")
root.geometry("900x500")

name = tk.StringVar()
phone = tk.StringVar()
email = tk.StringVar()
address = tk.StringVar()
search_var = tk.StringVar()

frame = tk.LabelFrame(root, text="Contact Details")
frame.pack(fill="x", padx=10, pady=5)

tk.Label(frame, text="Name").grid(row=0, column=0)
tk.Entry(frame, textvariable=name).grid(row=0, column=1)

tk.Label(frame, text="Phone").grid(row=0, column=2)
tk.Entry(frame, textvariable=phone).grid(row=0, column=3)

tk.Label(frame, text="Email").grid(row=1, column=0)
tk.Entry(frame, textvariable=email).grid(row=1, column=1)

tk.Label(frame, text="Address").grid(row=1, column=2)
tk.Entry(frame, textvariable=address).grid(row=1, column=3)

btn = tk.Frame(root)
btn.pack(pady=10)

tk.Button(btn, text="Add", width=12, command=add).grid(row=0, column=0)
tk.Button(btn, text="Update", width=12, command=update).grid(row=0, column=1)
tk.Button(btn, text="Delete", width=12, command=delete).grid(row=0, column=2)
tk.Button(btn, text="Clear", width=12, command=clear).grid(row=0, column=3)

s = tk.Frame(root)
s.pack(fill="x", padx=10)

tk.Entry(s, textvariable=search_var, width=30).pack(side="left")
tk.Button(s, text="Search", command=search).pack(side="left")
tk.Button(s, text="Show All", command=load).pack(side="left")

cols = ("ID", "Name", "Phone", "Email", "Address")

tree = ttk.Treeview(root, columns=cols, show="headings")

for c in cols:
    tree.heading(c, text=c)
    tree.column(c, width=170)

tree.pack(fill="both", expand=True, padx=10, pady=10)

tree.bind("<<TreeviewSelect>>", select)

load()
root.mainloop()