from tkinter import*
import mysql.connector as con
db = con.connect(
    host = 'localhost',
    port='3306',
    user= 'root',
    password = '',
    database ='lab14'
)
print(f"Connection has been made ! {db}")
cur = db.cursor()
def insertData():
    stdname = name.get()
    print(stdname)
    query = "create table if not exists std1 (stdname varchar(50))"
    cur.execute(query)
    sql = "insert into std1 (stdname) values('{} ') ".format(stdname)
    cur.execute(sql)
    db.commit()
    print('Your Data inserted Successfully!')
sk = Tk()
sk.geometry("555x555")
name = StringVar()
lab1 = Label(sk, text=" Name : ")
lab1.grid(row= 1, column = 1)
nameentry = Entry(sk, text= name).grid(row=1, column=2)
btn = Button(sk, text="Submit", command=insertData)
btn.grid(row=3, column=2)
sk.mainloop()




# get the user input and store it in variables
# rollno = int(input("Enter the roll number: "))
# stdname = input("Enter the student name: ")

# call the function with the user input
# insert_stdinfo(rollno, stdname)