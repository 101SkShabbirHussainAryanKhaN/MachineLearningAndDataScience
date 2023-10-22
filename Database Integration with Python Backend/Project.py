import tkinter as tk
from tkinter import ttk
import mysql.connector as connector
from tkinter import messagebox

win = tk.Tk()
win.geometry("1400x1000")
win.title('Welcome to Student Management System')

# win.config(bg='#3d2e70')
# ===Main Window =================================================================
title_label = tk.Label(win, text='Student Management System', font=(
    'arial', 30, 'bold'), border=8, relief=tk.GROOVE, bg='green', foreground='yellow')
title_label.pack(side=tk.TOP, fill=tk.X)

# =======data entry frame =======
detail_frame = tk.LabelFrame(win, text='Manage Students Record', font=(
    'arial', 25), border=7, bg='green', fg='yellow')
detail_frame.place(x=10, y=80, width=400, height=600)
# =======data retrieved frame =================
data_frame = tk.Frame(win, border=7, bg='yellow', relief=tk.GROOVE)
data_frame.place(x=420, y=80, width=1020, height=600)

# =============Variables =============================

rollno = tk.StringVar()
name = tk.StringVar()
email = tk.StringVar()
contact = tk.StringVar()
dob = tk.StringVar()
gander = tk.StringVar()
city = tk.StringVar()
address = tk.StringVar()

search_by = tk.StringVar()

# =================================================================

# =======data entry =======

rollno_lbl = tk.Label(detail_frame, text='Reg No :', font=('arial', 15))
rollno_lbl.grid(row=0, column=0, padx=4, pady=4)

rollno_ent = tk.Entry(detail_frame, bd=3, font=(
    'arial', 15), textvariable=rollno)
rollno_ent.grid(row=0, column=1, padx=4, pady=4)

name_lbl = tk.Label(detail_frame, text='Name : ', font=('arial', 15))
name_lbl.grid(row=1, column=0, padx=4, pady=4)

name_ent = tk.Entry(detail_frame, bd=3, font=('arial', 15), textvariable=name)
name_ent.grid(row=1, column=1, padx=4, pady=4)

email_lbl = tk.Label(detail_frame, text='Email : ', font=('arial', 15))
email_lbl.grid(row=2, column=0, padx=4, pady=4)

email_ent = tk.Entry(detail_frame, bd=3, font=(
    'arial', 15), textvariable=email)
email_ent.grid(row=2, column=1, padx=4, pady=4)

contact_lbl = tk.Label(detail_frame, text='Contact No: ', font=('arial', 15))
contact_lbl.grid(row=3, column=0, padx=4, pady=4)

contact_ent = tk.Entry(detail_frame, bd=3, font=(
    'arial', 15), textvariable=contact)
contact_ent.grid(row=3, column=1, padx=4, pady=4)

dob_lbl = tk.Label(detail_frame, text='D-O-B : ',
                   font=('arial', 15))
dob_lbl.grid(row=4, column=0, padx=4, pady=4)

dob_ent = tk.Entry(detail_frame, bd=3, font=('arial', 15), textvariable=dob)
dob_ent.grid(row=4, column=1, padx=4, pady=4)

gander_lbl = tk.Label(detail_frame, text='Gander : ', font=('arial', 15))
gander_lbl.grid(row=5, column=0, padx=4, pady=4)

gander_ent = ttk.Combobox(
    detail_frame, textvariable=gander, font=('arial', 15), state='readonly')
gander_ent['value'] = ('Male', 'Female', 'other')
gander_ent.grid(row=5, column=1, padx=4, pady=4)

city_lbl = tk.Label(detail_frame, text='City : ', font=('arial', 15))
city_lbl.grid(row=6, column=0, padx=4, pady=4)

city_ent = ttk.Combobox(detail_frame, textvariable=city,
                        font=('arial', 15), state='readonly')
city_ent['value'] = ('SKARDU', 'Roundu', 'Sadpara', 'Shigri Kalan', 'Hussainabad',)
city_ent.grid(row=6, column=1, padx=4, pady=4)

address_lbl = tk.Label(detail_frame, text='Address : ', font=('arial', 15))
address_lbl.grid(row=7, column=0, padx=4, pady=4)

address_ent = tk.Entry(detail_frame,
                       bd=3, font=('arial', 15), textvariable=address)
address_ent.grid(row=7, column=1, padx=4, pady=4)

# ============================ Function =====================================

def fetch_data():
    con = connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        database='lab10'
    )
    cur = con.cursor()
    sql = "SELECT * FROM data"
    cur.execute(sql)
    rows = cur.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', tk.END, values=row)
        con.commit()
        con.close()

def add_data():
    if rollno.get == '' or name.get() == '' or email.get() == '' or contact.get() == '' or city.get() == '':
        messagebox.showerror(
            'Error!', 'please fill all the fields with your email address')
    else:
        con = connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='lab10'
        )
        cur = con.cursor()
        cur.execute("INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (rollno.get(), name.get(), email.get(), contact.get(
        ), dob.get(), gander.get(), city.get(), address.get()))
        messagebox.showinfo('Success!', 'Data inserted successfully')
        con.commit()
        fetch_data()
        con.close()
        clear_data()

def get_cursor(event):
    '''this function fetches data from the selected row and returns the data in to the fields'''
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content['values']
    rollno.set(row[0])
    name.set(row[1])
    email.set(row[2])
    contact.set(row[3])
    dob.set(row[4])
    gander.set(row[5])
    city.set(row[6])
    address.set(row[7])

def update_data():
    con = connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        database='lab10'
    )
    cur = con.cursor()
    cur.execute("UPDATE data SET name=%s,email=%s,contact=%s,dob=%s,gander=%s,city=%s,address=%s WHERE rollno=%s", (name.get(), email.get(), contact.get(), dob.get(),
                gander.get(), city.get(), address.get(), rollno.get()))
    con.commit()
    messagebox.showinfo('Success!', 'Data updated successfully')
    fetch_data()
    con.close()
    clear_data()

def delete_data():
    con = connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        database='lab10'
    )
    cur = con.cursor()
    cur.execute("DELETE FROM data WHERE rollno=%s", (rollno.get(),))
    messagebox.showinfo('Success!', 'Data deleted successfully')
    con.commit()
    con.close()
    fetch_data()

def clear_data():
    rollno.set('')
    name.set('')
    email.set('')
    contact.set('')
    dob.set('')
    gander.set('')
    city.set('')
    address.set('')
    fetch_data()
# =============================================================================================================================

def search_data():
    search_query = search_entry.get()

    if not search_query:
        custom_message = "Oops! Something went wrong. Please check your input."
        messagebox.showerror('Custom Error', custom_message)
    else:
        con = connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='lab10'
        )
        cur = con.cursor()
        sql_query = "SELECT * FROM data WHERE name LIKE %s OR rollno LIKE %s OR contact LIKE %s OR email LIKE %s OR city LIKE %s"
        search_pattern = f'%{search_query}%'
        cur.execute(sql_query, (search_pattern, search_pattern,
                    search_pattern, search_pattern, search_pattern))
        search_results = cur.fetchall()
        con.close()

        # Clear the existing data in the table just in the table not in the database
        student_table.delete(*student_table.get_children())

        if search_results:
            for result in search_results:
                student_table.insert('', tk.END, values=result)
        else:
            fetch_data()
            messagebox.showinfo('Information', 'No matching records found')

# =================================================================
# ========button =================================
btn_frame = tk.Frame(detail_frame, bg='green', bd=7, relief=tk.GROOVE)
btn_frame.place(x=5, y=450, width=375, height=100)

add_btn = tk.Button(btn_frame, text='ADD', bg='magenta',
                    foreground='pink', bd=5, width=8, command=add_data)
add_btn.grid(row=0, column=0, padx=9, pady=25)

update_btn = tk.Button(btn_frame, text='UPDATE',
                       bg='magenta', foreground='pink', bd=5, width=8, command=update_data)
update_btn.grid(row=0, column=1, padx=9, pady=25)

delete_btn = tk.Button(btn_frame, text='DELETE',
                       bg='magenta', foreground='pink', bd=5, width=8, command=delete_data)
delete_btn.grid(row=0, column=2, padx=9, pady=25)

clear_btn = tk.Button(btn_frame, text='CLEAR', bg='magenta',
                      foreground='pink', bd=5, width=8, command=clear_data)
clear_btn.grid(row=0, column=3, padx=9, pady=25)

# =================================================================

# =======data retrieved frame =======

search_frame = tk.Frame(data_frame, bg='green', bd=6, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, bg='yellow', bd=4,
                      relief=tk.GROOVE, text='Search: ', font=('arial', 14))
search_lbl.grid(row=0, column=0, padx=4, pady=4)

search_in = ttk.Combobox(search_frame, font=(
    'arial', 15), textvariable=search_by, state='readonly')
search_in['value'] = ('Name', 'Reg No', 'Contact', 'email')
search_in.grid(row=0, column=1, padx=3, pady=3)

# Create a search Entry widget
search_entry = tk.Entry(search_frame, font=('arial', 15))
search_entry.grid(row=0, column=2)

search_btn = tk.Button(search_frame, text="Search",
                       font=('arial', 13), bg='green', bd=3, fg='yellow', width=8, command=search_data)
search_btn.grid(row=0, column=3, padx=40, pady=8)

showall_btn = tk.Button(search_frame, text="Show All",
                        font=('arial', 13), bg='green', bd=3, fg='yellow', width=8, command=fetch_data)
showall_btn.grid(row=0, column=4, padx=40, pady=8)

# ========================database frames =================

main_frame = tk.Frame(data_frame, bd=5, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

student_table = ttk.Treeview(main_frame, columns=(
    'Roll No', 'Name', 'Email', 'Contact No', 'D.O.B', 'Gander', 'City', 'Address'), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

# just for background colors of the table
style = ttk.Style()
style.configure("Treeview", background="yellow")

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading('Roll No', text='Roll No', anchor=tk.W)
student_table.heading('Name', text='Name', anchor=tk.W)
student_table.heading('Email', text='Email', anchor=tk.W)
student_table.heading('Contact No', text='Contact No', anchor=tk.W)
student_table.heading('D.O.B', text='D.O.B', anchor=tk.W)
student_table.heading('Gander', text='Gander', anchor=tk.W)
student_table.heading('City', text='City', anchor=tk.W)
student_table.heading('Address', text='Address', anchor=tk.W)

student_table['show'] = 'headings'

student_table.pack(fill=tk.BOTH, expand=True)

# ========  called func =================================

fetch_data()

student_table.bind('<ButtonRelease-1>', get_cursor)

win.mainloop()
