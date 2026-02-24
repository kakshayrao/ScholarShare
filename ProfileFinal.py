import tkinter as tk
from tkinter import ttk

class BuildProfileWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Build Profile")
        self.root.configure(bg="#3498db")
        self.create_widgets()

    def create_widgets(self):
        label_title = ttk.Label(self.root, text="Let's Build Your Profile!", font=("Arial", 24, "bold"), foreground="#ecf0f1", background="#3498db")
        label_title.grid(row=0, column=0, columnspan=2, pady=(30, 20))

        fields = ["Username", "Date of Birth", "Gender", "Branch of Study", "Year of Study"]
        self.entries = {}

        for idx, field in enumerate(fields, start=1):
            label = ttk.Label(self.root, text=field, font=("Arial", 14, "bold"), background="#3498db", foreground="#ecf0f1")
            label.grid(row=idx, column=0, pady=(12, 0), padx=16, sticky="w")

            entry = ttk.Entry(self.root, font=("Arial", 12))
            entry.grid(row=idx, column=1, pady=(12, 0), padx=16, sticky="w")
            entry.insert(0, "Enter your " + field)
            entry.bind("<FocusIn>", lambda event, entry=entry, field=field: self.clear_placeholder(event, entry, field))
            entry.bind("<FocusOut>", lambda event, entry=entry, field=field: self.restore_placeholder(event, entry, field))
            self.entries[field] = entry

        button_done = ttk.Button(self.root, text="Done", command=self.done_button_clicked, style="TButton")
        button_done.grid(row=len(fields) + 1, column=0, columnspan=2, pady=(16, 20))
        button_done.config(width=20)

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 14, "bold"), background="#bdc3c7", foreground="#2c3e50")

    def clear_placeholder(self, event, entry, field):
        if entry.get() == "Enter your " + field:
            entry.delete(0, tk.END)

    def restore_placeholder(self, event, entry, field):
        if entry.get() == "":
            entry.insert(0, "Enter your " + field)

    def done_button_clicked(self):
        # Add your logic here for handling the "Done" button click
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = BuildProfileWidget(root)
    root.mainloop()
