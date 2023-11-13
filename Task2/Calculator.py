import tkinter as tk

# Function to update the entry field
def button_click(number):
    current = entry_field.get()
    entry_field.delete(0, "end")
    entry_field.insert(0, current + str(number))

# Function to perform arithmetic operations
def perform_operation():
    try:
        expression = entry_field.get()
        result = eval(expression)
        entry_field.delete(0, "end")
        entry_field.insert(0, result)
    except Exception:
        entry_field.delete(0, "end")
        entry_field.insert(0, "Error")

# Function to clear the entry field
def clear():
    entry_field.delete(0, "end")

# Create a Tkinter window
window = tk.Tk()
window.title("Calculator")

# Set the window size and position it in the center
window.geometry("400x600")
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window.winfo_width()) // 2
y = (screen_height - window.winfo_height()) // 2
window.geometry("+{}+{}".format(x, y))

# Create the entry field
entry_field = tk.Entry(window, width=20, font=("Arial", 24))
entry_field.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# Create buttons for numbers and operations
button_values = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0
for value in button_values:
    if value == 'C':
        button = tk.Button(window, text=value, width=10, height=2, font=("Arial", 18), command=clear)
    elif value == '=':
        button = tk.Button(window, text=value, width=10, height=2, font=("Arial", 18), command=perform_operation)
    else:
        button = tk.Button(window, text=value, width=5, height=2, font=("Arial", 18), command=lambda v=value: button_click(v))
    button.grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the Tkinter main loop
window.mainloop()
