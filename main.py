import tkinter as tk
import re
from tkinter import messagebox, simpledialog, ttk
from database import initialize_database, add_contact, get_all_contacts, update_contact, delete_contact

class AddressBook:
    def __init__(self):
        initialize_database()
        self.contacts = get_all_contacts()
        self.max_entries = 100

        self.root = tk.Tk()
        self.root.title("Group 4 Address Book")
        self.root.geometry("600x400")
        self.root.configure(bg="#800000")  # Maroon background

        # Style for buttons
        style = ttk.Style()
        style.configure("TButton", background="#FFD700", foreground="#800000", font=("Arial", 10, "bold"))

        # Main Frame
        self.content_frame = tk.Frame(self.root, bg="#800000")
        self.content_frame.pack(expand=True, fill=tk.BOTH)

        # Menu
        self.show_home()

    def clear_content(self):
        for child in self.content_frame.winfo_children():
            child.destroy()

    def show_home(self):
        self.clear_content()

        title_label = tk.Label(self.content_frame, text="Address Boook", font=("Arial", 20, "bold"), bg="#800000", fg="#FFD700",)
        title_label.pack(pady=20)

        ttk.Button(self.content_frame, text="Add Contact", command=self.add_contact).pack(pady=5)
        ttk.Button(self.content_frame, text="Edit Contact", command=self.edit_contact).pack(pady=5)
        ttk.Button(self.content_frame, text="Delete Contact", command=self.delete_contact).pack(pady=5)
        ttk.Button(self.content_frame, text="View Contacts", command=self.view_contacts).pack(pady=5)
        ttk.Button(self.content_frame, text="Search Contacts", command=self.search_contacts).pack(pady=5)
        ttk.Button(self.content_frame, text="Exit", command=self.exit_app).pack(pady=20)

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
        
        self.clear_content()

        tk.Label(self.content_frame, text="Add Contact", font=("Arial", 16, "bold"), bg="#800000", fg="#FFD700").pack(pady=10)

        form_frame = tk.Frame(self.content_frame, bg="#800000")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="First Name:", bg="#800000", fg="#FFD700").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        first_entry = tk.Entry(form_frame)
        first_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Last Name:", bg="#800000", fg="#FFD700").grid(row=1, column=0, sticky="e", padx=5,pady=5)
        last_entry = tk.Entry(form_frame)
        last_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Address:", bg="#800000", fg="#FFD700").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        address_entry = tk.Entry(form_frame)
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Contact Number:", bg="#800000", fg="#FFD700").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        number_entry = tk.Entry(form_frame)
        number_entry.grid(row=3, column=1, padx=5, pady=5)

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
            self.show_home()

        action_frame = tk.Frame(self.content_frame, bg="#800000")
        action_frame.pack(pady=10)
        ttk.Button(action_frame, text="Add", command=submit).grid(row=0, column=0, padx=5)
        ttk.Button(action_frame, text= "Back", command=self.show_home).grid(row=0, column=1, padx=5)

    def edit_contact(self):
        if not self.contacts:
            messagebox.showerror("Error", "No contacts to edit.")
            return
        
        self.clear_content()

        tk.Label(self.content_frame, text="Edit Contact", font=("Arial", 16, "bold"), bg="#800000", fg="#FFD700").pack(pady=10)

        # Contact Selection
        select_frame = tk.Frame(self.content_frame, bg="#800000")
        select_frame.pack(pady=5)

        tk.Label(select_frame, text= "Select Contact:", bg="#800000", fg="#FFD700").grid(row=0, column=0, padx=5, pady=5)
        options = [f"{i+1}. {c['first']} {c['last']}" for i, c in enumerate(self.contacts)]
        selected_label = tk.StringVar(value=options[0])
        combo = ttk.Combobox(select_frame, textvariable=selected_label, values=options, state="readonly")
        combo.grid(row=0, column=1, padx=5, pady=5)

        # Prefilled Form
        form_frame = tk.Frame(self.content_frame, bg="#800000")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="First Name:", bg="#800000", fg="#FFD700").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        first_entry = tk.Entry(form_frame)
        first_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Last Name:", bg="#800000", fg="#FFD700").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        last_entry = tk.Entry(form_frame)
        last_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Address:", bg="#800000", fg="#FFD700").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        address_entry = tk.Entry(form_frame)
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Contact Number:", bg="#800000", fg="#FFD700").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        number_entry = tk.Entry(form_frame)
        number_entry.grid(row=3, column=1, padx=5, pady=5)

        # Initial form with first contact
        def populate_form(index):
            contact = self.contacts[index]
            first_entry.delete(0, tk.END)
            first_entry.insert(0, contact["first"])
            last_entry.delete(0, tk.END)
            last_entry.insert(0, contact["last"])
            address_entry.delete(0, tk.END)
            address_entry.insert(0, contact["address"])
            number_entry.delete(0, tk.END)
            number_entry.insert(0, contact["number"])

        current_index = 0
        populate_form(current_index)

        def on_select(_event):
            nonlocal current_index
            label = selected_label.get()
            try:
                current_index = options.index(label)
            except ValueError:
                current_index = 0
            populate_form(current_index)

        combo.bind("<<ComboboxSelected>>", on_select)

        def submit():
            contact = self.contacts[current_index]
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
                if not valid_last: error_msg += msg_last + "\n"
                if not valid_address: error_msg += msg_address + "\n"
                if not valid_number: error_msg += msg_number + "\n"
                messagebox.showerror("Validation Error", error_msg)
                return

            update_contact(contact["id"], first.strip(), last.strip(), address.strip(), number.strip())
            self.contacts = get_all_contacts()
            messagebox.showinfo("Success", "Contact edited successfully.")
            self.show_home()

        action_frame = tk.Frame(self.content_frame, bg="#800000")
        action_frame.pack(pady=10)
        ttk.Button(action_frame, text="Save", command=submit).grid(row=0, column=0, padx=5)
        ttk.Button(action_frame, text="Back", command=self.show_home).grid(row=0, column=1, padx=5)

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
        self.clear_content()

        tk.Label(self.content_frame, text="View Contacts", font=("Arial", 16, "bold"), bg="#800000", fg="#FFD700").pack(pady=10)

        text = tk.Text(self.content_frame, bg="#FFD700", fg="#800000", font=("Arial", 10))
        text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.contacts = get_all_contacts()

        if not self.contacts:
            text.insert(tk.END, "No contacts in the address book.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                text.insert(tk.END, f"{i}. {contact['first']} {contact['last']}\n Address: {contact['address']}\n Number: {contact['number']}\n\n")
            
        text.config(state=tk.DISABLED)

        ttk.Button(self.content_frame, text="Back", command=self.show_home).pack(pady=10)
    
    def search_contacts(self):
        if not self.contacts:
            messagebox.showerror("Error", "No contacts to search.")
            return
        
        self.clear_content()

        tk.Label(self.content_frame, text="Search Contacts", font=("Arial", 16, "bold"), bg="#800000", fg="#FFD700").pack(pady=10)

        controls = tk.Frame(self.content_frame, bg="#800000")
        controls.pack(pady=5)

        tk.Label(controls, text="Search by:", bg="#800000", fg="#FFD700").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        search_type = tk.StringVar(value="first")
        ttk.Combobox(controls, textvariable=search_type, values=["first", "last", "address", "number"], state="readonly").grid(row=0, column=1, padx=5, pady=5)

        tk.Label(controls, text="Query:", bg="#800000", fg="#FFD700").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        query_entry = tk.Entry(controls)
        query_entry.grid(row=1, column=1, padx=5, pady=5)

        results_text = tk.Text(self.content_frame, bg="#FFD700", fg="#800000", font=("Arial", 10))
        results_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        results_text.config(state=tk.DISABLED)

        def submit():
            stype = search_type.get()
            query = query_entry.get().strip().lower()
            if not query:
                messagebox.showerror("Error", "Query cannot be empty.")
                return
            
            self.contacts = get_all_contacts()
            
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
                
            results_text.config(state=tk.NORMAL)
            results_text.delete("1.0", tk.END)

            if not results:
                messagebox.showinfo("No Results", "No contacts match the query.")
            else:
                for num, contact in results:
                    results_text.insert(tk.END,f"{num}. {contact['first']} {contact['last']}\n Address: {contact['address']}\n Number: {contact['number']}\n\n")
            
            results_text.config(state=tk.DISABLED)

        actions = tk.Frame(self.content_frame, bg="#800000")
        actions.pack(pady=5)
        ttk.Button(actions, text="Search", command=submit).grid(row=0, column=0, padx=5)
        ttk.Button(actions, text="Back", command=self.show_home).grid(row=0, column=1, padx=5)
        
    def exit_app(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AddressBook()
    app.run()
