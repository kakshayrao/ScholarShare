import tkinter as tk
from tkinter import ttk, messagebox

class CreateAccountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account")
        self.root.configure(bg="#3498db")
        self.create_widgets()

    def create_widgets(self):
        label1 = ttk.Label(self.root, text="Username", font=("Arial", 14, "bold"), background="#3498db", foreground="#ecf0f1")
        label1.pack()
        self.username_entry = ttk.Entry(self.root, font=("Arial", 12))
        self.username_entry.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.X)

        label2 = ttk.Label(self.root, text="Password", font=("Arial", 14, "bold"), background="#3498db", foreground="#ecf0f1")
        label2.pack()
        self.password_entry = ttk.Entry(self.root, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.X)

        label3 = ttk.Label(self.root, text="Confirm Password", font=("Arial", 14, "bold"), background="#3498db", foreground="#ecf0f1")
        label3.pack()
        self.confirm_password_entry = ttk.Entry(self.root, show="*", font=("Arial", 12))
        self.confirm_password_entry.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.X)

        create_button = ttk.Button(self.root, text="Create Account", command=self.create_account, style="TButton")
        create_button.pack(pady=20)

        switch_to_login_button = ttk.Button(self.root, text="Switch to Login", command=self.switch_to_login, style="TButton")
        switch_to_login_button.pack(pady=10)

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 14, "bold"), background="#bdc3c7", foreground="#2c3e50")

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if username and password and confirm_password:
            if password == confirm_password:
                # Here you would typically add code to create the account in your system
                messagebox.showinfo("Account Info", f"Account created for {username}!")
            else:
                messagebox.showerror("Account Info", "Passwords do not match!")
        else:
            messagebox.showerror("Account Info", "All fields are required!")

    def switch_to_login(self):
        self.root.destroy()
        login_root = tk.Tk()
        login_app = LoginApp(login_root)
        login_root.mainloop()

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.configure(bg="#3498db")
        self.create_widgets()

    def create_widgets(self):
        label1 = ttk.Label(self.root, text="Username", font=("Arial", 14, "bold"), background="#3498db", foreground="#ecf0f1")
        label1.pack()
        self.username_entry = ttk.Entry(self.root, font=("Arial", 12))
        self.username_entry.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.X)

        label2 = ttk.Label(self.root, text="Password", font=("Arial", 14, "bold"), background="#3498db", foreground="#ecf0f1")
        label2.pack()
        self.password_entry = ttk.Entry(self.root, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.X)

        login_button = ttk.Button(self.root, text="Login", command=self.login, style="TButton")
        login_button.pack(pady=20)

        switch_to_create_account_button = ttk.Button(self.root, text="Switch to Create Account", command=self.switch_to_create_account, style="TButton")
        switch_to_create_account_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            # Here you would typically add code to check the provided credentials
            messagebox.showinfo("Login Info", f"Welcome {username}!")
        else:
            messagebox.showerror("Login Info", "Username and password are required!")

    def switch_to_create_account(self):
        self.root.destroy()
        create_account_root = tk.Tk()
        create_account_app = CreateAccountApp(create_account_root)
        create_account_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    create_account_app = CreateAccountApp(root)
    root.mainloop()
