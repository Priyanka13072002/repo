import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = {}

        
        self.title_label = tk.Label(root, text="Contact Book", font=("Arial", 18))
        self.title_label.pack(pady=10)

        
        self.name_label = tk.Label(root, text="Name")
        self.name_label.pack()
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.pack(pady=5)

        
        self.phone_label = tk.Label(root, text="Phone")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.pack(pady=5)

        
        self.add_contact_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_contact_button.pack(pady=5)

        self.update_contact_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_contact_button.pack(pady=5)

        self.delete_contact_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_contact_button.pack(pady=5)

        
        self.contact_listbox = tk.Listbox(root, width=50, height=10)
        self.contact_listbox.pack(pady=10)
        self.contact_listbox.bind('<<ListboxSelect>>', self.load_contact_details)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts[name] = phone
            self.update_contact_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "You must enter both name and phone number.")

    def update_contact(self):
        try:
            selected_contact = self.contact_listbox.curselection()[0]
            selected_contact_name = self.contact_listbox.get(selected_contact)
            new_name = self.name_entry.get()
            new_phone = self.phone_entry.get()
            if new_name and new_phone:
                del self.contacts[selected_contact_name]
                self.contacts[new_name] = new_phone
                self.update_contact_listbox()
                self.clear_entries()
            else:
                messagebox.showwarning("Warning", "You must enter both name and phone number.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a contact to update.")

    def delete_contact(self):
        try:
            selected_contact = self.contact_listbox.curselection()[0]
            selected_contact_name = self.contact_listbox.get(selected_contact)
            del self.contacts[selected_contact_name]
            self.update_contact_listbox()
            self.clear_entries()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a contact to delete.")

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for name in self.contacts:
            self.contact_listbox.insert(tk.END, name)

    def load_contact_details(self, event):
        try:
            selected_contact = self.contact_listbox.curselection()[0]
            selected_contact_name = self.contact_listbox.get(selected_contact)
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, selected_contact_name)
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, self.contacts[selected_contact_name])
        except IndexError:
            pass

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
