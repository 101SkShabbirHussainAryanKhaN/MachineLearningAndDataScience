from tkinter import *
import mysql.connector as con
db = con.connect(
    host='localhost',
    port='3306',
    user='root',
    password='',
    database='lab14',
    connect_timeout=60
)
print(f"Connection has been made! {db}")
cur = db.cursor()
def insertData():
    stdname = name.get()
    stdclass = student_class.get()
    section = student_section.get()
    query = "CREATE TABLE IF NOT EXISTS std1 (std_reg varchar(20), stdname VARCHAR(50), stdclass VARCHAR(10), section VARCHAR(10))"
    cur.execute(query)
    sql = "INSERT INTO std1 (stdname, stdclass, section) VALUES (%s, %s, %s)"
    data = (stdname, stdclass, section)
    cur.execute(sql, data)
    db.commit()
    print('Your Data inserted Successfully!')

sk = Tk()
sk.geometry("800x800")
sk.title("Welcome To SK Graphical User Interface")
name = StringVar()
student_class = StringVar()
student_section = StringVar()

lab1 = Label(sk, text="Name : ")
lab1.grid(row=1, column=1)
nameentry = Entry(sk, textvariable=name)
nameentry.grid(row=1, column=2)


lab2 = Label(sk, text="Class : ")
lab2.grid(row=2, column=1)
classentry = Entry(sk, textvariable=student_class)
classentry.grid(row=2, column=2)
lab3 = Label(sk, text="Section : ")
lab3.grid(row=3, column=1)
sectionentry = Entry(sk, textvariable=student_section)
sectionentry.grid(row=3, column=2)
btn = Button(sk, text="Submit", command=insertData)
btn.grid(row=4, column=2)
sk.mainloop()
