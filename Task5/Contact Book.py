import tkinter as tk
from tkinter import messagebox

# Global variable to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact = (name, phone, email, address)
        contacts.append(contact)
        update_contact_list()
        save_contacts_to_file()
        clear_fields()
    else:
        messagebox.showerror("Error", "Name and phone number are required.")

# Function to display the list of contacts
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, contact[0] + " - " + contact[1])

# Function to search for a contact
def search_contact():
    query = search_entry.get().lower()
    results = [contact for contact in contacts if query in contact[0].lower() or query in contact[1]]
    contact_list.delete(0, tk.END)
    for contact in results:
        contact_list.insert(tk.END, contact[0] + " - " + contact[1])

# Function to update a contact
def update_selected_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    new_name = name_entry.get()
    new_phone = phone_entry.get()
    new_email = email_entry.get()
    new_address = address_entry.get()

    if selected_contact and new_name and new_phone:
        index = contact_list.index(contact_list.curselection())
        contacts[index] = (new_name, new_phone, new_email, new_address)
        update_contact_list()
        save_contacts_to_file()
        clear_fields()
    else:
        messagebox.showerror("Error", "Name and phone number are required.")

# Function to delete a contact
def delete_selected_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    if selected_contact:
        index = contact_list.index(contact_list.curselection())
        contacts.pop(index)
        update_contact_list()
        save_contacts_to_file()
        clear_fields()

# Function to save contacts to a file
def save_contacts_to_file():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(",".join(contact) + "\n")

# Function to load contacts from a file
def load_contacts_from_file():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                contact = line.strip().split(",")
                contacts.append(tuple(contact))
    except FileNotFoundError:
        pass

# Function to clear the input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create input fields
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Create buttons with space in between
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack(pady=5)

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack(pady=5)

update_button = tk.Button(root, text="Update Contact", command=update_selected_contact)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_selected_contact)
delete_button.pack(pady=5)

# Create a listbox to display contacts
contact_list = tk.Listbox(root)
contact_list.pack()

# Load contacts from a file when the program starts
load_contacts_from_file()
update_contact_list()

# Create a function to save contacts to a file when the program closes
root.protocol("WM_DELETE_WINDOW", save_contacts_to_file)

# Start the main loop
root.mainloop()
