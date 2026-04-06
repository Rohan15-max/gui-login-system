import tkinter as tk
from tkinter import messagebox
import json

# load users
try:
    with open("users.json", "r") as file:
        users = json.load(file)
except:
    users = {}

# functions
def signup():
    username = entry_user.get()
    password = entry_pass.get()

    if username in users:
        messagebox.showerror("Error", "User already exists")
    else:
        users[username] = password
        with open("users.json", "w") as file:
            json.dump(users, file)
        messagebox.showinfo("Success", "Signup successful")

def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Error", "Invalid credentials")

# window
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

# labels
tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

# buttons
tk.Button(root, text="Login", command=login).pack(pady=5)
tk.Button(root, text="Signup", command=signup).pack()

root.mainloop()