import json
import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog
from plyer import notification  # Import the notification module from plyer

# Initialize an empty task list
tasks = []

# Function to save tasks to a JSON file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to format and display due date and reminder information
def format_task_info(task):
    info = f"{task['description']} {'(Done)' if task['done'] else ''}"
    if 'due_date' in task:
        info += f" - Due Date: {task['due_date']}"
    if 'reminder' in task:
        info += f" - Reminder: {task['reminder']}"
    return info

# Function to update the listbox with tasks
def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        task_listbox.insert(tk.END, f"{i}. {format_task_info(task)}")

# Function to handle the "Add Task" button
def add_task():
    description = new_task_text.get("1.0", tk.END)
    due_date = due_date_text.get("1.0", tk.END)
    reminder = reminder_text.get("1.0", tk.END)

    task = {"description": description, "done": False}

    if due_date.strip():
        task["due_date"] = due_date
    if reminder.strip():
        task["reminder"] = reminder

    tasks.append(task)
    save_tasks()
    update_task_listbox()

    new_task_text.delete("1.0", tk.END)
    due_date_text.delete("1.0", tk.END)
    reminder_text.delete("1.0", tk.END)

# Function to mark a task as done
def mark_task_done():
    selected_task = task_listbox.curselection()
    if not selected_task:
        messagebox.showerror("Error", "Please select a task to mark as done.")
        return

    task_index = selected_task[0]
    tasks[int(task_index)]["done"] = True
    save_tasks()
    update_task_listbox()

# Function to delete a task
def delete_task():
    selected_task = task_listbox.curselection()
    if not selected_task:
        messagebox.showerror("Error", "Please select a task to delete.")
        return

    task_index = selected_task[0]
    del tasks[int(task_index)]
    save_tasks()
    update_task_listbox()

# Function to check for and show reminders
def check_reminders():
    for task in tasks:
        if 'reminder' in task and task['reminder']:
            reminder = task['reminder'].strip()  # Remove leading/trailing whitespace
            try:
                reminder_time = datetime.datetime.strptime(reminder, '%Y-%m-%d %H:%M')
                current_time = datetime.datetime.now()
                if current_time >= reminder_time:
                    notification_title = "Reminder"
                    notification_text = task['description']
                    notification.notify(
                        title=notification_title,
                        message=notification_text,
                        app_name="To-Do List"
                    )
            except ValueError:
                print(f"Invalid reminder format: {task['reminder']}")

# Function to handle the "Edit Task" button
def edit_task():
    selected_task = task_listbox.curselection()
    if not selected_task:
        messagebox.showerror("Error", "Please select a task to edit.")
        return

    task_index = selected_task[0]
    task = tasks[int(task_index)]
    new_description = simpledialog.askstring("Edit Task", "Edit the task description:", initialvalue=task["description"])
    if new_description is not None:
        task["description"] = new_description
        save_tasks()
        update_task_listbox()

# Load existing tasks when the application starts
tasks = load_tasks()

# Create a GUI window
app = tk.Tk()
app.title("To-Do List")

# Create and configure widgets
new_task_label = tk.Label(app, text="New Task:")
new_task_label.pack()

new_task_text = tk.Text(app, height=4, width=80)
new_task_text.pack()

due_date_label = tk.Label(app, text="Due Date (optional, format: YYYY-MM-DD):")
due_date_label.pack()

due_date_text = tk.Text(app, height=2, width=80)
due_date_text.pack()

reminder_label = tk.Label(app, text="Reminder (optional, format: YYYY-MM-DD HH:MM):")
reminder_label.pack()

reminder_text = tk.Text(app, height=2, width=80)
reminder_text.pack()

add_task_button = tk.Button(app, text="Add Task", command=add_task)
add_task_button.pack()

task_listbox = tk.Listbox(app, height=10, width=100)
task_listbox.pack()

mark_done_button = tk.Button(app, text="Mark as Done", command=mark_task_done)
mark_done_button.pack()

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack()

edit_task_button = tk.Button(app, text="Edit Task", command=edit_task)
edit_task_button.pack()

# Initialize the task list in the GUI
update_task_listbox()

# Start a periodic reminder check (adjust the interval as needed)
app.after(60000, check_reminders)  # Check for reminders every minute

# Start the GUI application
app.mainloop()

