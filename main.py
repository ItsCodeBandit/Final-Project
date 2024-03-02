# Final Project 
# CIT 3302: Data Structures and Algorithms 
# Address Book Project
# 2/28/2024

import json
import tkinter as tk
from tkinter import messagebox


class AddressBookGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Address Book")

        self.address_book = AddressBook()
        self.master.geometry("400x100")

        self.name_text = tk.Label(master, text="Name:")
        self.name_text.grid(row=0, column=0)
        self.name_textBox = tk.Entry(master, width=30)
        self.name_textBox.grid(row=0, column=1)

        self.phone_text = tk.Label(master, text="phone:")
        self.phone_text.grid(row=1, column=0)
        self.phone_textBox = tk.Entry(master, width=30)
        self.phone_textBox.grid(row=1, column=1)

        self.email_text = tk.Label(master, text="Email:")
        self.email_text.grid(row=2, column=0)
        self.email_textBox = tk.Entry(master, width=30)
        self.email_textBox.grid(row=2, column=1)

        self.add_btn = tk.Button(master, text="Add Contact", command=self.add_contact) 
        self.add_btn.grid(row=3, column=0, padx=2, pady=2)

        self.search_btn = tk.Button(master, text="Search Contact", command=self.Search_Content) 
        self.search_btn.grid(row=3, column=1, padx=2, pady=2)

        self.list_btn = tk.Button(master, text="List all Current Contact", command=self.list_all) 
        self.list_btn.grid(row=3, column=2, padx=2, pady=2)



    def add_contact(self):
        name = self.name_textBox.get()
        phone = self.phone_textBox.get()
        email = self.email_textBox.get()

        if name and phone and email: 
            added_successfully = self.address_book.add_contact(name, phone, email)

            if added_successfully:
                messagebox.showinfo("success", "Contact has been added ^_^ !")
                self.save_to_json()
            else: 
                messagebox.showerror("error", "Detected duplicate contact ~_~ .")
        else:
            messagebox.showerror("Error", "Please fill in all field needed U_U .")

    def save_to_json(self):
        with open ("address_book.json", "w") as json_file: 
            json.dump(self.address_book.contacts, json_file)

    def Search_Content(self): 
        name = self.name_textBox.get()
        if name: 
            contact = self.address_book.Search_Content(name)
            if contact:
                messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
            else: 
                messagebox.showerror("Error", "cannot find contact")
        else: 
            messagebox.showerror("Error", "Please enter a name to search.")

    def list_all(self): 
        contacts = self.address_book.list_all()
        if contacts:
            list_str = "\n".join([f"Name: {con['name']}, Phone: {con['phone']}, Email: {con['email']}" for con in contacts])
            messagebox.showinfo("All Contacts", list_str)
        else: 
            messagebox.showinfo("Empty", "No contact")


class AddressBook:
    def __init__ (self):
        self.contacts = []
    
    def add_contact(self, name, phone_num, email): 
        for contact in self.contacts: 
            if contact['name'] == name: 

                return False
            
        contact = {'name': name, 'phone': phone_num, 'email': email}
        self.contacts.append(contact)
        return True
    
    def Search_Content(self, name): 
        for contact in self.contacts: 
            if contact['name'] == name: 
                return contact 
        return None 
        
    def list_all(self): 
        return self.contacts 
    
def main():
    root = tk.Tk()
    app = AddressBookGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()



   
                
    
    

       
    



        
