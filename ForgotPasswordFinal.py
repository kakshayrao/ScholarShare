import tkinter as tk
from tkinter import messagebox

class ForgotPasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        self.root.configure(bg="#3498db")
        self.create_widgets()
    
    def create_widgets(self):
        # Create a label for "Forgot Password"
        title_label = tk.Label(self.root, text="Forgot Password", font=("Arial", 24, "bold"), foreground="#ecf0f1", background="#3498db")
        title_label.pack(pady=20)
        
        # Create an email input field
        email_label = tk.Label(self.root, text="Your email address:", font=("Arial", 14), background="#3498db", foreground="#ecf0f1")
        email_label.pack()
        
        self.email_entry = tk.Entry(self.root, font=("Arial", 12))
        self.email_entry.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.X)
        
        # Create a "Send Link" button
        send_button = tk.Button(self.root, text="Send Link", command=self.send_link, font=("Arial", 14, "bold"), background="#bdc3c7", foreground="#2c3e50")
        send_button.pack(pady=20)
    
    def send_link(self):
        email = self.email_entry.get()
        if not email:
            # Show an error message if email is empty
            messagebox.showerror("Error", "Email is required!")
        else:
            # Implement the logic to send a reset password link here
            # For now, show a success message
            messagebox.showinfo("Success", f"Password reset link sent to {email}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ForgotPasswordApp(root)
    root.mainloop()
