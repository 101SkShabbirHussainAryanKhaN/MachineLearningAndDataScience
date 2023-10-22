import tkinter as tk
from tkinter import *
# import pymysql
class Employeestystem():
    def __init__(self,sk):
        self.sk = sk
        self.sk.title("Employee payroll manangement System | By Uobs Studemt")
        self.sk.geometry('1400x800')
        self.sk.configure(bg='maroon')
        title1 = Label(self.sk,text="Employee Payroll Manangement System", font=("times new roman bold italic", 20),
        bg="darkblue" ,fg="yellow").place(x=0,y=0,relwidth = 1)



        #------------------------------------------frame 1 ----------------------------------------


        frame1 = Frame(self.sk, bd=5 ,bg='green' ,relief=SOLID)
        frame1.place(x=5, y= 40, width=700, height=700)
        title2 = Label(frame1, text="Employee Details",font=('times new roman',20),bg='darkblue',fg='yellow').place(x=0, y=0,relwidth=1)
        lbl_empcode = Label(frame1, text="Employee code",font=('times new roman',14),fg='red',bg='lightgray')
        lbl_empcode.place(x=0, y=40)
        entry_empcode = Entry(frame1, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_empcode.place(x=140, y=40)

        btn_search = Button(frame1, text='Search',font=('times new roamn',14),fg='red',bg='lightgray',width=10,height=1)
        btn_search.place(x=350,y=40)
        
        lbl_designation = Label(frame1, text="Designation",font=('times new roman',14),bg='lightgray',fg='red')
        lbl_designation.place(x=0, y=80)
        entry_designation = Entry(frame1, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_designation.place(x=120, y=80)


        lbl_name = Label(frame1, text="Name",font=('times new roman',14),bg='lightgray',fg='red')
        lbl_name.place(x=0, y=120)
        entry_name = Entry(frame1, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_name.place(x=120, y=120)

        lbl_age = Label(frame1, text="Age",font=('times new roman',14),bg='lightgray',fg='red')
        lbl_age.place(x=0, y=160)
        entry_age = Entry(frame1, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_age.place(x=120, y=160)

        lbl_gender = Label(frame1, text="Gender",font=('times new roman',14),bg='lightgray',fg='red')
        lbl_gender.place(x=0, y=200)
        entry_gender = Entry(frame1, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_gender.place(x=120, y=200)

        lbl_email = Label(frame1, text="Email",font=('times new roman',14),bg='lightgray',fg='red')
        lbl_email.place(x=0, y=240)
        entry_email = Entry(frame1, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_email.place(x=120, y=240)

        lbl_hireloc = Label(frame1, text="Hired Location",font=('times new roman',14),bg='lightgray',fg='red')
        lbl_hireloc.place(x=0, y=280)
        entry_hireloc = Entry(frame1, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_hireloc.place(x=120, y=280)

        lbl_address = Label(frame1, text="Address",font=('times new roman',14),bg='lightgray',fg='red')
        lbl_address.place(x=0, y=320)
        self.txt_address = Text(frame1, font=('times new roman',14),fg='red',bg='lightyellow',width=55,height=4)
        self.txt_address.place(x=120, y=320)

        lbl_DOB = Label(frame1, text="Date of Birth",font=('times new roman',14),bg='lightgray',fg='red')
        lbl_DOB.place(x=340, y=80)
        entry_DOB = Entry(frame1, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_DOB.place(x=460, y=80)

        lbl_DOj = Label(frame1, text="Date of join",font=('times new roman',14),bg='lightgray',fg='red')
        lbl_DOj.place(x=340, y=120)
        entry_DOB = Entry(frame1, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_DOB.place(x=460, y=120)

        lbl_experience = Label(frame1, text="Experience",font=('times new roman',14),bg='lightgray',fg='red')
        lbl_experience.place(x=345, y=160)
        entry_experience = Entry(frame1, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_experience.place(x=460, y=160)

        lbl_proofid = Label(frame1, text="ProofID",font=('times new roman',14),bg='lightgray',fg='red')
        lbl_proofid.place(x=345, y=200)
        entry_proofid = Entry(frame1, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_proofid.place(x=460, y=200)

        lbl_contact = Label(frame1, text="Contact Number",font=('times new roman',13),bg='lightgray',fg='red')
        lbl_contact.place(x=345, y=240)
        entry_contact = Entry(frame1, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_contact.place(x=475, y=240)

        lbl_status = Label(frame1, text="Status",font=('times new roman',14),bg='lightgray',fg='red')
        lbl_status.place(x=345, y=280)
        entry_status = Entry(frame1, font=('times new roman',14),fg='red',bg='lightgray')
        entry_status.place(x=460, y=280)

        btn_submit = Button(frame1, text='Submit',font=('times new roamn',14),fg='red',bg='lightgray')
        btn_submit.place(x=330,y=420)


         

        
        #------------------------------------------frame 2 ----------------------------------------




        frame2 = Frame(self.sk, bd=5 ,bg='green', relief=SOLID)
        frame2.place(x=710, y= 40, width=700, height=350)
        title2 = Label(frame2, text="Employee Salary Details",font=('times new roman bold',18),bg='darkblue',fg='yellow').place(x=0, y=0,relwidth=1)
        lbl_month = Label(frame2, text="Month",font=('times new roman',14),fg='red',bg='lightgray')
        lbl_month.place(x=0, y=40)
        entry_month = Entry(frame2, font=('times new roman',10),fg='red',bg='lightyellow')
        entry_month.place(x=80, y=40)

        lbl_year = Label(frame2, text="Year",font=('times new roman',14),fg='red',bg='lightgray')
        lbl_year.place(x=210, y=40)
        entry_year = Entry(frame2, font=('times new roman',10),fg='red',bg='lightyellow')
        entry_year.place(x=255, y=40)

        lbl_salary = Label(frame2, text="Salary",font=('times new roman',14),fg='red',bg='lightgray')
        lbl_salary.place(x=380, y=40)
        entry_salary = Entry(frame2, font=('times new roman',10),fg='red',bg='lightyellow')
        entry_salary.place(x=440, y=40)

        lbl_days = Label(frame2, text="Total Days",font=('times new roman',14),fg='red',bg='lightgray')
        lbl_days.place(x=0, y=80)
        entry_days = Entry(frame2, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_days.place(x=90, y=80)

        lbl_absent = Label(frame2, text="Absent",font=('times new roman',14),fg='red',bg='lightgray')
        lbl_absent.place(x=290, y=80)
        entry_absent = Entry(frame2, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_absent.place(x=390, y=80)

        lbl_medical = Label(frame2, text="Medical",font=('times new roman',14),fg='red',bg='lightgray')
        lbl_medical.place(x=0, y=120)
        entry_medical = Entry(frame2, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_medical.place(x=90, y=120)

        lbl_pf = Label(frame2, text="PF",font=('times new roman',14),fg='red',bg='lightgray')
        lbl_pf.place(x=290, y=120)
        entry_pf = Entry(frame2, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_pf.place(x=390, y=120)

        lbl_Conveyance = Label(frame2, text="Conveyance",font=('times new roman',14),fg='red',bg='lightgray')
        lbl_Conveyance.place(x=0, y=160)
        entry_Conveyance = Entry(frame2, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_Conveyance.place(x=100, y=160)


        lbl_netSalary = Label(frame2, text="Net Salary",font=('times new roman',14),fg='red',bg='lightgray')
        lbl_netSalary.place(x=290, y=160)
        entry_netSalary = Entry(frame2, font=('times new roman',14),fg='red',bg='lightyellow')
        entry_netSalary.place(x=390, y=160)

        btn_calculate = Button(frame2, text='Calculate',font=('times new roamn',14),fg='red',bg='lightblue')
        btn_calculate.place(x=150,y=200)

        btn_save = Button(frame2, text='Save',font=('times new roamn',14),fg='red',bg='cyan')
        btn_save.place(x=250,y=200)


        btn_clear = Button(frame2, text='Clear',font=('times new roamn',14),fg='red',bg='aqua')
        btn_clear.place(x=315,y=200)

        btn_Update = Button(frame2, text='Update',font=('times new roamn',14),fg='red',bg='lightgreen')
        btn_Update.place(x=150,y=240,width=120)

        btn_delete = Button(frame2, text='Delete',font=('times new roamn',14),fg='red',bg='darkred')
        btn_delete.place(x=270,y=240, width=110)
        
        

        
        #------------------------------------------frame 3 ----------------------------------------




        self.sk = sk
        self.button_sizes = {
            '7': (50, 35),
            '8': (50, 35),
            '9': (50, 35),
            '/': (50, 50),
            '4': (50, 35),
            '5': (50, 35),
            '6': (50, 35),
            '*': (50, 50),
            '1': (50, 35),
            '2': (50, 35),
            '3': (50, 35),
            '-': (50, 50),
            '0': (50, 35),
            '.': (50, 35),
            '+': (50, 35),
            '=': (50, 50),
            'C': (150, 20)
        }

        frame3 = tk.Frame(self.sk, bd=5, relief=tk.SOLID, bg="green")
        frame3.place(x=710, y= 390, width=215, height=350)
        title3 = tk.Label(frame3, text="Calculator", font=('times new roman bold italic', 20), bg='darkblue', fg='yellow').place(x=0, y=0, relwidth=1)

        # Entry to display calculator input
        self.calculation = tk.Entry(frame3, font=('times new roman bold', 15),justify=RIGHT, fg='red', bg='yellow')
        self.calculation.place(x=0, y=30)

        # Calculator buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+', '=',
            'C'
        ]

        row_val, col_val = 0, 0
        for button in buttons:
            width, height = self.button_sizes[button]
            btn = tk.Button(frame3, text=button, font=('times new roman bold italic', 14),bg="lightgreen",fg='red', command=lambda btn=button: self.button_click(btn))
            btn.place(x=col_val * 50, y=row_val * 40 + 90, width=width, height=height)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, value):
        current = self.calculation.get()
        if value == '=':
            try:
                result = eval(current)
                self.calculation.delete(0, tk.END)
                self.calculation.insert(tk.END, str(result))
            except Exception:
                self.calculation.delete(0, tk.END)
                self.calculation.insert(tk.END, "Error")
        elif value == 'C':
            self.calculation.delete(0, tk.END)
        else:
            self.calculation.insert(tk.END, value)
       
        # entry_month = Entry(frame3, font=('times new roman',15),fg='red',bg='lightyellow')
        # entry_month.place(x=0, y=40)


        

        # btn_seven = Button(frame3, text='7',font=('times new roamn',14),fg='red',bg='lightgray',command=7)
        # btn_seven.place(x=0,y=80 ,width=50)

        # btn_eight = Button(frame3, text='8',font=('times new roamn',14),fg='red',bg='lightgray')
        # btn_eight.place(x=50,y=80,width=50)


        # btn_nine = Button(frame3, text='9',font=('times new roamn',14),fg='red',bg='lightgray')
        # btn_nine.place(x=100,y=80, width=50)

        # btn_divide = Button(frame3, text='/',font=('times new roamn',20),fg='red',bg='lightgray')
        # btn_divide.place(x=150,y=80,width=50 )

        # btn_four = Button(frame3, text='4',font=('times new roamn',14),fg='red',bg='lightgray')
        # btn_four.place(x=0,y=120, width=50)

        # btn_five = Button(frame3, text='5',font=('times new roamn',14),fg='red',bg='lightgray')
        # btn_five.place(x=50,y=120, width=50)

        # btn_six = Button(frame3, text='6',font=('times new roamn',14),fg='red',bg='lightgray')
        # btn_six.place(x=100,y=120, width=50)

        # btn_multiply = Button(frame3, text='*',font=('times new roamn',20),fg='red',bg='lightgray')
        # btn_multiply.place(x=150,y=130,width=50 )

        # btn_one = Button(frame3, text='1',font=('times new roamn',14),fg='red',bg='lightgray')
        # btn_one.place(x=0,y=160, width=50)

        # btn_two = Button(frame3, text='2',font=('times new roamn',14),fg='red',bg='lightgray')
        # btn_two.place(x=50,y=160, width=50)

        # btn_three = Button(frame3, text='3',font=('times new roamn',14),fg='red',bg='lightgray')
        # btn_three.place(x=100,y=160, width=50)

        # btn_minus = Button(frame3, text='-',font=('times new roamn',20),fg='red',bg='lightgray')
        # btn_minus.place(x=150,y=175,width=50 )

        # btn_zero = Button(frame3, text='0',font=('times new roamn',14),fg='red',bg='lightgray')
        # btn_zero.place(x=0,y=200, width=50)

        # btn_dot = Button(frame3, text='.',font=('times new roamn',14),fg='red',bg='lightgray')
        # btn_dot.place(x=50,y=200, width=50)

        # btn_plus = Button(frame3, text='+',font=('times new roamn',14),fg='red',bg='lightgray')
        # btn_plus.place(x=100,y=200, width=50)

        # btn_equal = Button(frame3, text='=',font=('times new roamn',18),fg='red',bg='lightgray')
        # btn_equal.place(x=150,y=225,width=50 )

        # btn_Clear = Button(frame3, text='C',font=('times new roamn',12),fg='red',bg='lightgray')
        # btn_Clear.place(x=0,y=240,width=150 )

sk = tk.Tk()
obj = Employeestystem(sk)
sk.mainloop()
