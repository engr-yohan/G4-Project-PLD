import tkinter as tk
import re
from tkinter import messagebox, simpledialog, ttk
from database import initialize_database, add_contact, get_all_contacts, update_contact, delete_contact

class AddressBook:
    def __init__(self):
        initialize_database()
        self.contacts = get_all_contacts()
        self.max_entries = 100

        self. root = tk.Tk()
        self.root.title ("Group 4 Address Book")
        self.root.geometry("600x400")
        self.root.configure(bg ="#800000") # Maroon background

        # Style for buttons
        style = ttk.Style()
        style.configure("TButton", background="#FFD700", foreground="#800000", font=("Arial", 10,"bold"))

        # Main Frame
        main_frame = tk.Frame(self.root, bg="#800000")
        main_frame.pack(pady=20)

        # Title label
        title_label = tk.Label(main_frame, text= "Address Book", font=("Arial", 20, "bold"), bg="#800000", fg="#FFD700")
        title_label.pack(pady=10)

        # Buttons
        self.add_btn = ttk.Button(main_frame, text="Add Contact", command=self.add_contact)
        self.add_btn.pack(pady=5)

        self.edit_btn = ttk.Button(main_frame, text="Edit Contact", command=self.edit_contact)
        self.edit_btn.pack (pady=5)

        self.delete_btn = ttk.Button(main_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_btn.pack(pady=5)

        self.view_btn = ttk.Button(main_frame, text="View Contacts", command=self.view_contacts)
        self.view_btn.pack(pady=5)

        self.search_btn = ttk.Button(main_frame, text="Search Contacts", command=self.search_contacts)
        self.search_btn.pack(pady=5)

        self.exit_btn = ttk.Button(main_frame, text="Exit", command=self.exit_app)
        self.exit_btn.pack(pady=5)

    def validate_name(self, name):
            """Validate name: not empy, only letters and spaces."""
            if not name.strip():
                return False, "Name cannot be empty."
            if not re.match(r"^[a-zA-Z\s]+$", name):
                return False, "Name must contain only letters and spaces."
            return True, ""
        
    def validate_address(self, address):
            """validate address: not empty."""
            if not address.strip():
                return False, "Address cannot be empty."
            return True, ""
        
    def validate_number(self, number):
            """Validate contact number: 11 digits, allowing dashes, spaces, parenthesis."""
            cleaned = re.sub(r"[^\d]", "", number)
            if not 10 <= len(cleaned) <= 15:
                return False, " Contact number must be 11 digits."
            return True, ""
        
    def add_contact(self):
        if len(self.contacts) >= self.max_entries:
            messagebox.showerror("Error", "Address book is full (max 100 entries).")
            return
            
        add_win = tk.Toplevel(self.root)
        add_win.title("Add Contact")
        add_win.configure(bg="#800000")
        add_win.geometry("400x300")

        # Labels and entries
        tk.Label(add_win, text="First Name:", bg="#800000", fg="#FFD700"). pack(pady=5)
        first_entry = tk.Entry(add_win)
        first_entry.pack()

        tk.Label(add_win, text="Last Name:", bg="#800000", fg="#FFD700").pack(pady=5)
        last_entry = tk.Entry(add_win)
        last_entry.pack()

        tk.Label(add_win, text="Address:", bg="#800000", fg="#FFD700").pack(pady=5)
        address_entry = tk.Entry(add_win)
        address_entry.pack()

        tk.Label(add_win, text="Contact Number:", bg="#800000", fg="#FFD700").pack(pady=5)
        number_entry = tk.Entry(add_win)
        number_entry.pack()

        def submit():
            first = first_entry.get()
            last = last_entry.get()
            address = address_entry.get()
            number = number_entry.get()

            # Validation
            valid_first, msg_first = self.validate_name(first)
            valid_last, msg_last = self.validate_name(last)
            valid_address, msg_address = self.validate_address(address)
            valid_number, msg_number = self.validate_number(number)

            if not (valid_first and valid_last and valid_address and valid_number):
                error_msg = ""
                if not valid_first: error_msg += msg_first + "\n"
                if not valid_last: error_msg += msg_last + "\n"
                if not valid_address: error_msg += msg_address + "\n"
                if not valid_number: error_msg += msg_number + "\n"
                messagebox.showerror("Validation Error", error_msg)
                return
                
            add_contact(first.strip(), last.strip(), address.strip(), number.strip())
            self.contacts = get_all_contacts()
            messagebox.showinfo("Success", "Contact added successfully.")
            add_win.destroy()

        ttk.Button(add_win, text="Add", command=submit).pack(pady=10)

    def edit_contact(self):
        if not self.contacts:
            messagebox.showerror("Error", "No contacts to edit.")
            return

        num = simpledialog.askinteger("Edit Contact", f"Enter entry number to edit (1-{len(self.contacts)}):")
        if num is None or not (1 <= num <= len(self.contacts)):
            messagebox.showerror("Error", "Invalid entry number.")
            return

        contact = self.contacts[num-1]

        edit_win = tk.Toplevel(self.root)
        edit_win.title("Edit Contact")
        edit_win.configure(bg="#800000")
        edit_win.geometry("400x300")

        # Labels and Entries with prefilled data
        tk.Label(edit_win, text="First Name:", bg="#800000", fg="#FFD700").pack(pady=5)
        first_entry = tk.Entry(edit_win)
        first_entry.insert(0, contact["first"])
        first_entry.pack()

        tk.Label(edit_win, text="Last Name:", bg="#800000", fg="#FFD700").pack(pady=5)
        last_entry = tk.Entry(edit_win)
        last_entry.insert(0, contact["last"])
        last_entry.pack()

        tk.Label(edit_win, text="Address:", bg="#800000", fg="#FFD700").pack(pady=5)
        address_entry = tk.Entry(edit_win)
        address_entry.insert(0, contact["address"])
        address_entry.pack()

        tk.Label(edit_win, text="Contact Number:", bg="#800000", fg="#FFD700").pack(pady=5)
        number_entry = tk.Entry(edit_win)
        number_entry.insert(0, contact["number"])
        number_entry.pack()

        def submit():
            first = first_entry.get()
            last = last_entry.get()
            address = address_entry.get()
            number = number_entry.get()

            # validation
            valid_first, msg_first = self.validate_name(first)
            valid_last, msg_last = self.validate_name(last)
            valid_address, msg_address = self.validate_address(address)
            valid_number, msg_number = self.validate_number(number)

            if not (valid_first and valid_last and valid_address and valid_number):
                error_msg = ""
                if not valid_first: error_msg += msg_first + "\n"
                if not valid_last: error_msg += msg_last +"\n"
                if not valid_address: error_msg += msg_address + "\n"
                if not valid_number: error_msg += msg_number + "\n"
                messagebox.showerror("Validation Error", error_msg)
                return

            update_contact(contact["id"], first.strip(), last.strip(), address.strip(), number.strip())
            self.contacts = get_all_contacts()
            messagebox.showinfo("Success", "Contact edited successfully.")
            edit_win.destroy()

        ttk.Button(edit_win, text="Save", command=submit).pack(pady=10)

    def delete_contact(self):
        if not self.contacts:
            messagebox.showerror("Error", "No contacts to delete.")
            return

        num = simpledialog.askinteger("Delete Contact", f"Enter entry number to delete (1-{len(self.contacts)}):")
        if num is None or not (1 <= num <= len(self.contacts)):
            messagebox.showerror("Error", "Invalid entry number.")
            return
        
        contact = self.contacts[num-1]
        confirm = messagebox.askyesno("Confirm Delete", f"Delete contact: {contact['first']} {contact['last']}?")
        if confirm:
            contact_id = contact.get("id")
            if contact_id is not None:
                delete_contact(contact_id)
                self.contacts = get_all_contacts()
                messagebox.showinfo("Success", "Contact deleted successfully.")
            else:
                messagebox.showerror("Error", "Cannot delete: missing contact ID. Try viewing contacts and deleting again.")

    def view_contacts(self):
        view_win = tk.Toplevel(self.root)
        view_win.title("View Contacts")
        view_win.configure(bg="#800000")
        view_win.geometry("600x400")

        text = tk.Text(view_win, bg="#FFD700", fg="#800000", font=("Arial", 10))
        text.pack(expand=True, fill=tk.BOTH)

        if not self.contacts:
            text.insert(tk.END, "No contacts in the address book.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                text.insert(tk.END, f"{i}. {contact['first']} {contact['last']}\n Address: {contact['address']}\n Number: {contact['number']}\n\n")
            
        text.config(state=tk.DISABLED)
    
    def search_contacts(self):
        if not self.contacts:
            messagebox.showerror("Error", "No contacts to search.")
            return
        
        search_win = tk.Toplevel(self.root)
        search_win.title("Search Contacts")
        search_win.configure(bg="#800000")
        search_win.geometry("400x200")

        tk.Label(search_win, text="Search by:", bg="#800000", fg="#FFD700").pack(pady=5)
        search_type = tk.StringVar(value="first")
        ttk.Combobox(search_win, textvariable=search_type, values=["first", "last", "address", "number"]).pack()

        tk.Label(search_win, text="Query:", bg="#800000", fg="#FFD700").pack(pady=5)
        query_entry = tk.Entry(search_win)
        query_entry.pack()

        def submit ():
            stype = search_type.get()
            query = query_entry.get().strip().lower()
            if not query:
                messagebox.showerror("Error", "Query cannot be empty.")
                return
            
            results = []
            for i, contact in enumerate(self.contacts, 1):
                if stype == "first" and query in contact["first"].lower():
                    results.append((i, contact))
                elif stype == "last" and query in contact["last"].lower():
                    results.append((i, contact))
                elif stype == "address" and query in contact["address"].lower():
                    results.append((i, contact))
                elif stype == "number" and query in contact["number"].lower():
                    results.append((i, contact))
                
            search_win.destroy()

            if not results:
                messagebox.showinfo("No Results", "No contacts match the query.")
                return
            
            result_win = tk.Toplevel(self.root)
            result_win.title("Search Results")
            result_win.configure(bg="#800000")
            result_win.geometry("600x400")

            text = tk.Text(result_win, bg="#FFD700", fg="#800000", font=("Arial", 10))
            text.pack(expand=True, fill=tk.BOTH)

            for num, contact in results:
                text.insert(tk.END, f"{num}. {contact['first']} {contact['last']}\n Address: {contact['address']}\n Number: {contact['number']}\n\n")

            text.config(state=tk.DISABLED)

        ttk.Button(search_win, text="Search", command=submit).pack(pady=10)

    def exit_app(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AddressBook()
    app.run()
