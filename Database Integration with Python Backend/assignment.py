import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import io
from db_connection import create_connection, close_connection
# Create a global variable to store the loaded image data
loaded_image_data = None
loaded_image_path = None
image_label = None

def create_table():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS student(std_id INT PRIMARY KEY AUTO_INCREMENT, reg_no varchar(100) not null, std_name VARCHAR(100) NOT NULL, std_email VARCHAR(100) NOT NULL, std_contact int not null, std_dob varchar(50) not null, hostelite varchar(100) not null, image_data BLOB)')

    except Exception as err:
        print(f"An error occurred: {err}")
    finally:
        cursor.close()
        close_connection(connection)

# ===== insert method to insert student information =====
def insert_student(reg_no, std_name, std_email, std_contact, std_dob, hostelite, image_data):
    insert_query = "INSERT INTO student(reg_no, std_name, std_email, std_contact, std_dob, hostelite, image_data) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute(insert_query, (reg_no, std_name, std_email, std_contact, std_dob, hostelite,image_data))
            connection.commit()
            messagebox.showinfo('Success', "Data inserted successfully")
        except Exception as err:
            messagebox.showerror('Error', 'Error occurred')
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

# ===== Delete method to delete student information =====
def delete_student(reg_no):
    delete_query = "DELETE FROM student WHERE reg_no = %s"
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute(delete_query, (reg_no.get()))
            connection.commit()
            messagebox.showinfo("Success", "Record Deleted Successfully")
        except Exception as err:
            messagebox.showerror("Error", f"An error occurred: {err}")
            connection.rollback()
        finally:
            connection.close()
            close_connection(connection)
            
def load_image():
    global loaded_image_data, loaded_image_path, image_label
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        loaded_image_path = file_path
        image = Image.open(file_path)
        image = image.resize((100, 100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        if image_label:
            image_label.config(image=photo)
            image_label.photo = photo
        else:
            image_label = tk.Label(window, image=photo)
            image_label.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
        loaded_image_data = open(file_path, 'rb').read()


def display_all_student_data():
    def show_all_data():
        for item in tree.get_children():
            tree.delete(item)

        # Insert all data into the treeview
        for student in data:
            # Convert binary image data to PhotoImage if it's not empty
            image_data = student[7]
            if image_data:
                try:
                    image = Image.open(io.BytesIO(image_data))
                    image = image.resize((100, 100), Image.LANCZOS)
                    photo = ImageTk.PhotoImage(image)
                except Exception as e:
                    # Handle the image loading error
                    print(f"Error loading image: {e}")
                    photo = None  # Set photo to None for corrupted/truncated images
            else:
                # Placeholder image if no image data is available
                photo = None

            # Insert the data into the treeview, aligning it properly
            tree.insert("", "end", values=student[:7] + (photo,), tags=("data",))
            if photo:
                tree.image_add(photo, image=photo)

    def clear_table():
        # Clear the existing data in the treeview
        for item in tree.get_children():
            tree.delete(item)

    connection = create_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student")
        data = cursor.fetchall()

        # Create a new window for displaying all data
        all_data_window = tk.Toplevel()
        all_data_window.title("All Student Data")

        # Create a treeview widget to display data in rows and columns
        columns = ("ID", "Registration Number", "Name", "Email", "Contact", "DOB", "Hostelite", "Image")
        tree = ttk.Treeview(all_data_window, columns=columns, show="headings")

        # Define column headings with anchor to align them properly
        for col in columns:
            tree.heading(col, text=col, anchor='center')
            tree.column(col, width=100)  # Adjust column width as needed

        # Insert all data into the treeview
        for student in data:
            # Convert binary image data to PhotoImage if it's not empty
            image_data = student[7]
            if image_data:
                try:
                    image = Image.open(io.BytesIO(image_data))
                    image = image.resize((50, 50), Image.LANCZOS)
                    photo = ImageTk.PhotoImage(image)
                except Exception as e:
                    # Handle the image loading error
                    print(f"Error loading image: {e}")
                    photo = None  # Set photo to None for corrupted/truncated images
            else:
                # Placeholder image if no image data is available
                photo = None

            # Insert the data into the treeview, aligning it properly
            tree.insert("", "end", values=student[:7] + (photo,), tags=("data",))
            if photo:
                tree.image_add(photo, image=photo)
        
        tree.pack(fill="both", expand=True)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        close_connection(connection)

# Function to clear the input fields
def clear_fields():
    regno_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    hostelite_var.set(False)

# Create the main application window
window = tk.Tk()
window.title("Student Management System")
window.geometry("500x800")
window.configure(padx=20, pady=20)

# Create labels and entry fields for each attribute
regno_label = tk.Label(window, text="Registration Number:",width=20)
regno_label.grid(row=1, column=0, padx=10, pady=5)
regno_entry = tk.Text(window, width=30, height=2)
regno_entry.grid(row=1, column=1, padx=10, pady=5)

name_label = tk.Label(window, text="Student Name:")
name_label.grid(row=2, column=0, padx=10, pady=5)
name_entry = tk.Text(window, width=30, height=2)
name_entry.grid(row=2, column=1, padx=10, pady=5)

email_label = tk.Label(window, text="Student Email:")
email_label.grid(row=3, column=0, padx=10, pady=5)
email_entry = tk.Text(window, width=30, height=2)
email_entry.grid(row=3, column=1, padx=10, pady=5)

contact_label = tk.Label(window, text="Student Contact:")
contact_label.grid(row=4, column=0, padx=10, pady=5)
contact_entry = tk.Text(window, width=30, height=2)
contact_entry.grid(row=4, column=1, padx=10, pady=5)

dob_label = tk.Label(window, text="Date of Birth:")
dob_label.grid(row=5, column=0, padx=10, pady=5)
dob_entry = tk.Text(window, width=30, height=2)
dob_entry.grid(row=5, column=1, padx=10, pady=5)

# hostelite combo box

# Create a Combobox widget for hostelite selection
hostelite_label = tk.Label(window, text="Hostelite:")
hostelite_label.grid(row=6, column=0, padx=10, pady=5)
hostelite_var = tk.StringVar()  # Variable to store the selected value
hostelite_combobox = ttk.Combobox(window, textvariable=hostelite_var, values=["Yes", "No"])
hostelite_combobox.grid(row=6, column=1, padx=10, pady=5)

# Set an initial value for the Combobox (optional)
hostelite_combobox.set("No")

load_image_button = tk.Button(window, text="Load Image", command=load_image)
load_image_button.grid(row=7, column=1, columnspan=3, padx=10, pady=10)

# Function to submit student information
def submit():
    reg_no = regno_entry.get("1.0", "end-1c").strip()
    std_name = name_entry.get("1.0", "end-1c").strip()
    std_email = email_entry.get("1.0", "end-1c").strip()
    std_contact = contact_entry.get("1.0", "end-1c").strip()
    std_dob = dob_entry.get("1.0", "end-1c").strip()
    hostelite = "Yes" if hostelite_var.get() else "No"
    
    global loaded_image_data
    if loaded_image_data:
        # Insert the student information and image data into the database
        insert_student(reg_no, std_name, std_email, std_contact, std_dob, hostelite, loaded_image_data)
        messagebox.showinfo('Success', "Data inserted successfully")
        loaded_image_data = None  # Reset the loaded image data

    # Clear the input fields after submission
    clear_fields()


# Function to display all student data
def display_all_data():
    display_all_student_data()
    

# Create a black frame for the top bar
top_bar_frame = tk.Frame(window, bg="black")
top_bar_frame.grid(row=0, column=0, columnspan=4, sticky="ew")

# Create a label for the title text in white
title_label = tk.Label(top_bar_frame, text="Student Management System", bg="black", fg="white")
title_label.pack(padx=10, pady=5)
    
# Create a black frame to contain the buttons
button_frame = tk.Frame(window, bg="black",width=30)
button_frame.grid(row=8, column=0, columnspan=4, padx=30, pady=10, sticky="ew")

# Create buttons inside the black frame with even spacing
button_height = 2
add_button = tk.Button(button_frame, text="Add", command=submit, bg="white", fg="black", borderwidth=1, relief="sunken",height=button_height,width=5)
delete_button = tk.Button(button_frame, text="Delete", command=delete_student, bg="white", fg="black", borderwidth=1, relief="sunken",height=button_height,width=7)
show_data_button = tk.Button(button_frame, text="Show ", command=display_all_data, bg="white", fg="black", borderwidth=1, relief="sunken",height=button_height,width=7)
clear_button = tk.Button(button_frame, text="Clear", command=clear_fields, bg="white", fg="black", borderwidth=1, relief="sunken",height=button_height,width=5)

# Grid the buttons with even spacing
add_button.grid(row=0, column=0, padx=(0, 15), pady=10)
delete_button.grid(row=0, column=1, padx=15, pady=10)
show_data_button.grid(row=0, column=2, padx=15, pady=10)
clear_button.grid(row=0, column=3, padx=(15, 0), pady=10)

# Set column weights for even spacing
button_frame.columnconfigure(0, weight=2)
button_frame.columnconfigure(1, weight=2)
button_frame.columnconfigure(2, weight=2)
button_frame.columnconfigure(3, weight=2)





# Start the GUI main loop
window.mainloop()

if __name__ == "__main__":
    create_table()
    
