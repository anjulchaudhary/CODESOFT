import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        self.label = tk.Label(master, text="Password Length:")
        self.label.pack()

        self.length_var = tk.IntVar(value=12)
        self.length_scale = tk.Scale(master, from_=8, to=32, orient=tk.HORIZONTAL, variable=self.length_var)
        self.length_scale.pack()

        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        self.uppercase_check = tk.Checkbutton(master, text="Include Uppercase (A-Z)", variable=self.uppercase_var)
        self.uppercase_check.pack()

        self.lowercase_check = tk.Checkbutton(master, text="Include Lowercase (a-z)", variable=self.lowercase_var)
        self.lowercase_check.pack()

        self.numbers_check = tk.Checkbutton(master, text="Include Numbers (0-9)", variable=self.numbers_var)
        self.numbers_check.pack()

        self.symbols_check = tk.Checkbutton(master, text="Include Symbols (!@#$%^&*)", variable=self.symbols_var)
        self.symbols_check.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(master, text="", font=("Courier", 14))
        self.password_label.pack()

    def generate_password(self):
        length = self.length_var.get()
        characters = ""

        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.numbers_var.get():
            characters += string.digits
        if self.symbols_var.get():
            characters += string.punctuation

        if characters:
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text=password)
        else:
            self.password_label.config(text="Select at least one character type")

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()
