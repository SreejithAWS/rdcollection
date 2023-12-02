import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

class ExcelForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Form")

        # Create DataFrame to store data
        self.df = pd.DataFrame(columns=["Name", "Age", "Email"])

        # Create and set up the form
        self.setup_form()

    def setup_form(self):
        # Label and Entry for Name
        lbl_name = ttk.Label(self.root, text="Name:")
        lbl_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_name = ttk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        # Label and Entry for Age
        lbl_age = ttk.Label(self.root, text="Age:")
        lbl_age.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_age = ttk.Entry(self.root)
        self.entry_age.grid(row=1, column=1, padx=10, pady=10)

        # Label and Entry for Email
        lbl_email = ttk.Label(self.root, text="Email:")
        lbl_email.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_email = ttk.Entry(self.root)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)

        # Save Button
        save_button = ttk.Button(self.root, text="Save", command=self.save_data)
        save_button.grid(row=3, column=0, columnspan=2, pady=20)

        # View Data Button
        view_button = ttk.Button(self.root, text="View Data", command=self.view_data)
        view_button.grid(row=4, column=0, columnspan=2, pady=10)

    def save_data(self):
        # Get values from entries
        name = self.entry_name.get()
        age = self.entry_age.get()
        email = self.entry_email.get()

        # Validate non-empty fields
        if not name or not age or not email:
            messagebox.showerror("Error", "All fields must be filled.")
            return

        # Append data to DataFrame
        new_data = {"Name": name, "Age": age, "Email": email}
        self.df = self.df.append(new_data, ignore_index=True)

        # Clear entry fields
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

        messagebox.showinfo("Success", "Data saved successfully.")

    def view_data(self):
        # Display DataFrame in a new window
        view_window = tk.Toplevel(self.root)
        view_window.title("View Data")

        tree = ttk.Treeview(view_window, columns=list(self.df.columns), show="headings")

        # Set column headings
        for col in self.df.columns:
            tree.heading(col, text=col)

        # Insert data into the Treeview
        for _, row in self.df.iterrows():
            tree.insert("", "end", values=row.tolist())

        tree.pack(expand=True, fill=tk.BOTH)

# Create the main application window
root = tk.Tk()
app = ExcelForm(root)

# Start the Tkinter event loop
root.mainloop()