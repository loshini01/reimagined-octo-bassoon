import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        
        # Contact list
        self.contacts = []
        
        # Labels
        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=0, column=0, sticky="e")
        
        self.label_phone = tk.Label(master, text="Phone:")
        self.label_phone.grid(row=1, column=0, sticky="e")
        
        
        # Entry fields
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)
        
        self.entry_phone = tk.Entry(master)
        self.entry_phone.grid(row=1, column=1)
        
        # Buttons
        self.button_add = tk.Button(master, text="Add", command=self.add_contact)
        self.button_add.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.button_display = tk.Button(master, text="Display", command=self.display_contacts)
        self.button_display.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.button_clear = tk.Button(master, text="Clear", command=self.clear_fields)
        self.button_clear.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.button_delete = tk.Button(master, text="Delete", command=self.delete_contact)
        self.button_delete.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Listbox to display contacts
        self.listbox = tk.Listbox(master)
        self.listbox.grid(row=6, column=0, columnspan=2, pady=10)
        
    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        
        if name and phone:
            self.contacts.append({"Name": name, "Phone": phone})
            self.update_listbox()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in both name and phone fields.")
        
        self.clear_fields()
    
    def display_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"Name: {contact['Name']}, Phone: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")
    
    def clear_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")
    
    def delete_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.update_listbox()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()

