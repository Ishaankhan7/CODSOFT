import random
import string
import tkinter as tk

def generate_password(length, complexity):
    if complexity == "easy":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper()
    else:
        return "Invalid complexity level."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    password = generate_password(length, complexity)
    password_display.config(text="Generated Password: " + password)

# Create the main window
window = tk.Tk()
window.title("Creative Password Generator")
window.geometry("400x300")

# Style for labels and buttons
label_style = ("Helvetica", 12)
button_style = ("Helvetica", 14, "bold")

# Header label
header_label = tk.Label(window, text="Password Generator", font=("Helvetica", 20, "bold"), pady=20)
header_label.pack()

# Length input
length_label = tk.Label(window, text="Password Length:", font=label_style)
length_label.pack()
length_entry = tk.Entry(window, font=label_style)
length_entry.pack()

# Complexity level selection
complexity_label = tk.Label(window, text="Complexity Level:", font=label_style)
complexity_label.pack()

complexity_var = tk.StringVar()
complexity_var.set("medium")  # Default value
easy_radio = tk.Radiobutton(window, text="Easy", variable=complexity_var, value="easy", font=label_style)
medium_radio = tk.Radiobutton(window, text="Medium", variable=complexity_var, value="medium", font=label_style)
strong_radio = tk.Radiobutton(window, text="Strong", variable=complexity_var, value="strong", font=label_style)
easy_radio.pack()
medium_radio.pack()
strong_radio.pack()

# Generate password button
generate_button = tk.Button(window, text="Generate Password", command=generate_and_display_password, font=button_style, bg="green", fg="white")
generate_button.pack(pady=20)

# Display generated password
password_display = tk.Label(window, text="", font=("Helvetica", 14))
password_display.pack()

# Start the GUI main loop
window.mainloop()
