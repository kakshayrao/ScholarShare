import tkinter as tk

def create_button(root, text, command):
    button = tk.Button(root, text=text, command=command, width=20, height=2, font=("Plus Jakarta Sans", 14))
    button.pack(pady=10)
    return button

def main():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Year of Study")

    # Background
    background = tk.Frame(root, bg="lightgray", width=400, height=400)
    background.pack_propagate(0)  # To prevent the frame from shrinking
    background.pack()

    # Title
    title_label = tk.Label(background, text="Year of Study", font=("Plus Jakarta Sans", 20, "bold"))
    title_label.pack(pady=10)

    # Year Buttons
    create_button(background, "1st Year", lambda: print("1st Year clicked"))
    create_button(background, "2nd Year", lambda: print("2nd Year clicked"))
    create_button(background, "3rd Year", lambda: print("3rd Year clicked"))
    create_button(background, "4th Year", lambda: print("4th Year clicked"))

    root.mainloop()

if __name__ == "__main__":
    main()
