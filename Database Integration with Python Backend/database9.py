import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
from tkinter import filedialog
from PIL import Image, ImageTk

# Create a database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="",  # Replace with your MySQL password
            database="lab14"
        )
        return connection
    except Error as e:
        messagebox.showerror('Database Error', str(e))
        return None

# Initialize the database connection
connection = create_connection()

# Create the main application window
window = tk.Tk()
window.title("Student Database Management System")
window.geometry("800x500")

# Create a frame for the left side (table display)
left_frame = tk.Frame(window)
left_frame.pack(side="left", padx=20, pady=20)

# Create a treeview widget for displaying the student data
columns = ("Registration No", "Name", "Email", "Contact Number", "Date of Birth", "Hostelite")
treeview = ttk.Treeview(left_frame, columns=columns, show="headings")
treeview.heading("Registration No", text="Registration No")
treeview.heading("Name", text="Name")
treeview.heading("Email", text="Email")
treeview.heading("Contact Number", text="Contact Number")
treeview.heading("Date of Birth", text="Date of Birth")
treeview.heading("Hostelite", text="Hostelite")
treeview.pack(fill="both", expand=True)

# Function to update the table with student data
def update_table():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    treeview.delete(*treeview.get_children())
    for row in rows:
        treeview.insert("", "end", values=row)

# Function to add a new student
def add_student():
    regno = regno_entry.get().strip()
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    contact = contact_entry.get().strip()
    dob = dob_entry.get().strip()
    hostelite = hostelite_var.get()

    if not regno or not name:
        messagebox.showerror("Error", "Registration No and Name are required fields.")
        return

    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO students_dbms (regno, name, email, contact, dob, hostelite) VALUES (%s, %s, %s, %s, %s, %s)",
                       (regno, name, email, contact, dob, hostelite))
        connection.commit()
        update_table()
        clear_fields()
        messagebox.showinfo("Success", "Student added successfully.")
    except Error as e:
        messagebox.showerror("Error", str(e))

# Function to clear input fields
def clear_fields():
    regno_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    hostelite_var.set("No")
    loaded_image_data = None
    image_label.config(image=None)

# Function to delete a student
def delete_student():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a student to delete.")
        return

    regno = treeview.item(selected_item, 'values')[0]

    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM students WHERE regno = %s", (regno,))
        connection.commit()
        update_table()
        clear_fields()
        messagebox.showinfo("Success", "Student deleted successfully.")
    except Error as e:
        messagebox.showerror("Error", str(e))

# Function to load an image
def load_image():
    global loaded_image_data
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if file_path:
        loaded_image_data = open(file_path, "rb").read()
        image = Image.open(file_path)
        image.thumbnail((100, 100))
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.photo = photo

# Function to clear the entire table
def clear_table():
    if messagebox.askyesno("Clear Table", "Do you want to clear the entire table? This action cannot be undone."):
        cursor = connection.cursor()
        try:
            cursor.execute("TRUNCATE TABLE students")
            connection.commit()
            update_table()
            clear_fields()
            messagebox.showinfo("Success", "Table cleared successfully.")
        except Error as e:
            messagebox.showerror("Error", str(e))

# Labels and entry fields for student information
regno_label = tk.Label(window, text="Registration No:")
regno_label.pack()
regno_entry = tk.Entry(window)
regno_entry.pack()

name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

contact_label = tk.Label(window, text="Contact Number:")
contact_label.pack()
contact_entry = tk.Entry(window)
contact_entry.pack()

dob_label = tk.Label(window, text="Date of Birth:")
dob_label.pack()
dob_entry = tk.Entry(window)
dob_entry.pack()

hostelite_var = tk.StringVar(value="No")
hostelite_label = tk.Label(window, text="Hostelite:")
hostelite_label.pack()
hostelite_combobox = ttk.Combobox(window, textvariable=hostelite_var, values=["Yes", "No"])
hostelite_combobox.pack()

load_image_button = tk.Button(window, text="Load Image", command=load_image)
load_image_button.pack()

add_button = tk.Button(window, text="Add Student", command=add_student)
add_button.pack()

delete_button = tk.Button(window, text="Delete Student", command=delete_student)
delete_button.pack()

clear_button = tk.Button(window, text="Clear Fields", command=clear_fields)
clear_button.pack()

clear_table_button = tk.Button(window, text="Clear Table", command=clear_table)
clear_table_button.pack()

image_label = tk.Label(window)
image_label.pack()

# Update the table initially
update_table()

# Start the GUI main loop
window.mainloop()

# Close the database connection when the program exits
connection.close()
