import tkinter as tk

def create_text_label(root, text):
    label = tk.Label(root, text=text, font=('Plus Jakarta Sans', 30))
    label.pack(pady=10)
    return label

def main():
    root = tk.Tk()
    root.geometry("500x400")
    root.title("Account Details")

    # Background
    background = tk.Frame(root, bg="lightgray", width=500, height=400)
    background.pack_propagate(0)  # To prevent the frame from shrinking
    background.pack()

    # Title
    title_label = create_text_label(background, "Profile")

    # User Name
    user_name_label = create_text_label(background, "User Name")

    # Gender
    gender_label = create_text_label(background, "Gender")

    # Date of Birth
    dob_label = create_text_label(background, "Date of Birth")

    # Branch of Study
    branch_label = create_text_label(background, "Branch of Study")

    # Year of Study
    year_label = create_text_label(background, "Year of Study")

    root.mainloop()

if __name__ == "__main__":
    main()
