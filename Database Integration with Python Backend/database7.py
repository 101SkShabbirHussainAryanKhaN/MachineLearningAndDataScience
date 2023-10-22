import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import mysql.connector
from PIL import Image, ImageTk

# Connect to MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='lab14'
)

cursor = db.cursor()

# Create student table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        grade VARCHAR(10),
        picture_path VARCHAR(255)
    )
''')
db.commit()

# Function to add a new student record
def add_student():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    picture_path = picture_path_var.get()

    sql = 'INSERT INTO students (first_name, last_name, age, grade, picture_path) VALUES (%s, %s, %s, %s, %s)'
    values = (first_name, last_name, age, grade, picture_path)
    
    cursor.execute(sql, values)
    db.commit()
    clear_fields()
    display_students()

# Function to display student records
def display_students():
    student_list.delete(*student_list.get_children())
    cursor.execute('SELECT * FROM students')
    for row in cursor.fetchall():
        student_list.insert("", "end", values=row)

# Function to clear input fields
def clear_fields():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    picture_path_var.set("")

# Function to upload a picture
def upload_picture():
    file_path = filedialog.askopenfilename()
    picture_path_var.set(file_path)

# Create the main window
root = tk.Tk()
root.title("Student Management System")

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

# Image upload button
upload_button = tk.Button(root, text="Upload Picture", command=upload_picture)
upload_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Display the selected image (if any)
picture_path_var = tk.StringVar()
picture_path_label = tk.Label(root, textvariable=picture_path_var)
picture_path_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Create and place buttons
add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Create a treeview widget to display student records
student_list = ttk.Treeview(root, columns=("ID", "First Name", "Last Name", "Age", "Grade", "Picture Path"), show="headings")
student_list.heading("ID", text="ID")
student_list.heading("First Name", text="First Name")
student_list.heading("Last Name", text="Last Name")
student_list.heading("Age", text="Age")
student_list.heading("Grade", text="Grade")
student_list.heading("Picture Path", text="Picture Path")
student_list.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Display student records
display_students()

# Start the Tkinter main loop
root.mainloop()

# Close the database connection when the application is closed
db.close()
