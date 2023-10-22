import tkinter as tk
from tkinter import ttk
import sqlite3

# Create a database connection (or create the database if it doesn't exist)
conn = sqlite3.connect("student_database.db")
cursor = conn.cursor()

# Create a table to store student information
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        grade TEXT
    )
""")
conn.commit()

# Function to insert a new student record
def insert_student():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    
    cursor.execute("INSERT INTO students (first_name, last_name, age, grade) VALUES (?, ?, ?, ?)",
                   (first_name, last_name, age, grade))
    conn.commit()
    clear_entries()
    display_students()

# Function to display all student records
def display_students():
    student_list.delete(*student_list.get_children())
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        student_list.insert("", "end", values=row)

# Function to clear input entries
def clear_entries():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Student Database Management System")

# Create and place labels and entry widgets
first_name_label = tk.Label(root, text="First Name:")
first_name_label.grid(row=0, column=0, padx=10, pady=5)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=0, column=1, padx=10, pady=5)

last_name_label = tk.Label(root, text="Last Name:")
last_name_label.grid(row=1, column=0, padx=10, pady=5)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=1, column=1, padx=10, pady=5)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=2, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

grade_label = tk.Label(root, text="Grade:")
grade_label.grid(row=3, column=0, padx=10, pady=5)
grade_entry = tk.Entry(root)
grade_entry.grid(row=3, column=1, padx=10, pady=5)

# Create and place buttons
insert_button = tk.Button(root, text="Insert Student", command=insert_student)
insert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Create a treeview widget to display student records
student_list = ttk.Treeview(root, columns=("ID", "First Name", "Last Name", "Age", "Grade"), show="headings")
student_list.heading("ID", text="ID")
student_list.heading("First Name", text="First Name")
student_list.heading("Last Name", text="Last Name")
student_list.heading("Age", text="Age")
student_list.heading("Grade", text="Grade")
student_list.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Display the student records
display_students()

# Start the Tkinter main loop
root.mainloop()

# Close the database connection when the application is closed
conn.close()
