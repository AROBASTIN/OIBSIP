import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # Install using: pip install pyperclip

def generate_password():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

length_frame = tk.Frame(root)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:").pack(side="left")
length_entry = tk.Entry(length_frame, width=5)
length_entry.pack(side="left")
length_entry.insert(0, "12")

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

options_frame = tk.Frame(root)
options_frame.pack(pady=10)

tk.Checkbutton(options_frame, text="Letters (A-Z)", variable=letters_var).pack(anchor="w")
tk.Checkbutton(options_frame, text="Numbers (0-9)", variable=numbers_var).pack(anchor="w")
tk.Checkbutton(options_frame, text="Symbols (!@#)", variable=symbols_var).pack(anchor="w")

generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", width=20)
generate_btn.pack(pady=10)

password_entry = tk.Entry(root, font=("Helvetica", 12), width=30, justify="center")
password_entry.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_password, bg="#2196F3", fg="white", width=20)
copy_btn.pack(pady=5)

root.mainloop()
