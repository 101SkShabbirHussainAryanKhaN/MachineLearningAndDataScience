import mysql.connector as con
db =con.connect(host ='localhost' ,port='3306', user = 'root', database ='lab14')
print(db)

query = "create table if not exists student (rollno int primary key , stdname varchar(50))"
cur = db.cursor()
cur.execute(query)

def insert_stdinfo(rollno , stdname):
    sql = "insert into student (rollno , stdname) values(%s, %s)" # use placeholders for values
    cur.execute(sql, (rollno, stdname)) # pass the parameters as a tuple
    db.commit()
    print('Done')

# get the user input and store it in variables
rollno = int(input("Enter the roll number: "))
stdname = input("Enter the student name: ")

# call the function with the user input
insert_stdinfo(rollno, stdname)
