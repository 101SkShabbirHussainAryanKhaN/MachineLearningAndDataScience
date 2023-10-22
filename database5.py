import mysql.connector as con
from tkinter import *
db = con.connect(
    host = 'localhost',
    port='3306',
    user= 'root',
    password = '',
    database ='lab14'
)
print(f"Connection has been made ! {db}")

query = "create table if not exists student1 (rollno int primary key , stdname varchar(50))"
cur = db.cursor()
cur.execute(query)

def insert_stdinfo(rollno , stdname):
    rollno = stdrollno.get()
    stdname = name.get()

    sql = "insert into student1 (rollno , stdname) values(%s, %s)" 
    cur.execute(sql,(rollno , stdname)) 
    db.commit()
    print('Your Data inserted Successfully!')

def retrieve_stdinfo():
    
    sql = "select * from student1"
    cur.execute(sql)
    for table in cur:
        print(table)

def retrieve_ParticularStdinfo():
    rollno = roll.get()
    sql = "select * from student1 where rollno ={}".format(rollno)
    cur.execute(sql,(rollno))
    for row in cur:
        print(row)



sk = Tk()
sk.geometry("800x800")
sk.title("Welcome To SK Graphical User Interface")
name = StringVar()
roll = StringVar()

lab = Label(sk, text= "Name : ")
lab.grid(row=1, column=1)
nameentry = Entry(sk, textvariable=name)


btn = Button(sk, text="RetrieveData", command=retrieve_stdinfo)
btn.grid(row=0, column=1)
btns = Button(sk, text="RetrieveParticularStdinfo", command=retrieve_ParticularStdinfo)
btn.grid(row=1, column=0)
sk.mainloop()

