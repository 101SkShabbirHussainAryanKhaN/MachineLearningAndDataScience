from tkinter import *ch
from tkinter import messagebox, ttk
import mysql.connector as connector
import time
import asyncio
import os
import tempfile


class employsystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employ payroll Management System || by UOBS Students")
        self.root.geometry('1490x750+50+50')
        title1 = Label(self.root, text="Employ Payroll Managment System", font=(
            'Times New Roman', 20), bg='#3b5186', fg='white').place(x=0, y=0, relwidth=1)
        btn_0 = Button(self.root, text='All Employee', font=(
            'times-new-roman', 14), command=self.employee_frame, bg='#124d7a', fg='white').place(x=1300, y=5, width=120, height=30)

        ################################ Frame1  #################################

# ...................................  variables ....................................

        self.var_empcode = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_doj = StringVar()
        self.var_dob = StringVar()
        self.var_experience = StringVar()
        self.var_gander = StringVar()
        self.var_proofid = StringVar()
        self.var_email = StringVar()
        self.var_contact = StringVar()
        self.var_hlocation = StringVar()
        self.var_status = StringVar()
        self.var_address = StringVar()

        frame1 = Frame(self.root, bd=5, relief=RIDGE)
        frame1.place(x=30, y=50, width=650, height=600)
        title2 = Label(frame1, text='Employees Details', font=(
            'times new roman', 15), bg='gray', fg='white',).place(x=0, y=0, height=40, width=640)
# =============================== column 1 ==============================================
        lbl_empcode = Label(frame1, text='Employees Code',
                            font=('times new roman', 16), fg='black')
        lbl_empcode.place(x=0, y=50)
        entry_empcode = Entry(frame1, font=(
            'times new roman', 17), textvariable=self.var_empcode, bg='#e6e2da', fg='black')
        entry_empcode.place(x=150, y=50)

        btn_search = Button(frame1, text='Search', font=(
            'times new roman', 10), command=self.search, bg='#3b5186', fg='lightblue', bd='5', padx=40)
        btn_search.place(x=400, y=50)

        lbl_designation = Label(frame1, text='Designation', font=(
            'times new roman', 14), fg='black').place(x=0, y=100)
        entry_designation = Entry(frame1, font=(
            'times new roman', 14), textvariable=self.var_designation, fg='black', bg='lightyellow').place(x=130, y=100)

        lbl_name = Label(frame1, text='Name', font=(
            'times new roman', 14), fg='black').place(x=0, y=150)

        entry_name = Entry(frame1, font=('times new roman', 14), textvariable=self.var_name,
                           fg='black', bg='lightyellow').place(x=130, y=150)

        lbl_age = Label(frame1, text='Age', font=(
            'times new roman', 14), fg='black').place(x=0, y=200)
        entry_age = Entry(frame1, font=('times new roman', 14), textvariable=self.var_age,
                          fg='black', bg='lightyellow').place(x=130, y=200)

        lbl_gander = Label(frame1, text='Gander', font=(
            'times new roman', 14), fg='black').place(x=0, y=250)
        entry_gander = Entry(frame1, font=(
            'times new roman', 14), textvariable=self.var_gander, fg='black', bg='lightyellow').place(x=130, y=250)

        lbl_email = Label(frame1, text='Email', font=(
            'times new roman', 14), fg='black').place(x=0, y=300)
        entry_email = Entry(frame1, font=('times new roman', 14), textvariable=self.var_email,
                            fg='black', bg='lightyellow').place(x=130, y=300)

        lbl_hireloc = Label(frame1, text='hired Location', font=(
            'times new roman', 14), fg='black').place(x=0, y=350)
        entry_hireloc = Entry(frame1, font=(
            'times new roman', 14), textvariable=self.var_hlocation, fg='black', bg='lightyellow').place(x=130, y=350)

        lbl_address = Label(frame1, text='Address', font=(
            'times new roman', 14), fg='black')
        lbl_address.place(x=0, y=400)
        # textvariable=self.var_address,
        self.text_address = Text(frame1, font=(
            'times new roman', 14), fg='black', bg='lightyellow', bd='3')
        self.text_address.insert("1.0", "Hello!")
        self.text_address.place(x=130, y=400, width=500, height=100)
# ================= column 2 ================================
        lbl_dob = Label(frame1, text='D-O-B', font=('times new roman',
                        14), fg='black').place(x=345, y=100)
        entry_dob = Entry(frame1, font=('times new roman', 14), textvariable=self.var_dob,
                          fg='black', bg='lightyellow').place(x=440, y=100)

        lbl_doj = Label(frame1, text='DOJ', font=(
            'times new roman', 14), fg='black').place(x=345, y=150)
        entry_doj = Entry(frame1, font=('times new roman', 14), textvariable=self.var_doj,
                          fg='black', bg='lightyellow').place(x=440, y=150)

        lbl_experience = Label(frame1, text='experience', font=(
            'times new roman', 14), fg='black').place(x=345, y=200)
        entry_experience = Entry(frame1, font=(
            'times new roman', 14), textvariable=self.var_experience, fg='black', bg='lightyellow').place(x=440, y=200)

        lbl_proofid = Label(frame1, text='proofid', font=(
            'times new roman', 14), fg='black').place(x=345, y=250)
        entry_proofid = Entry(frame1, font=(
            'times new roman', 14), textvariable=self.var_proofid, fg='black', bg='lightyellow').place(x=440, y=250)

        lbl_contact = Label(frame1, text='contact', font=(
            'times new roman', 14), fg='black').place(x=345, y=300)
        entry_contact = Entry(frame1, font=(
            'times new roman', 14), textvariable=self.var_contact, fg='black', bg='lightyellow').place(x=440, y=300)

        lbl_status = Label(frame1, text='status', font=(
            'times new roman', 14), fg='black').place(x=345, y=350)
        entry_status = Entry(frame1, font=(
            'times new roman', 14), textvariable=self.var_status, fg='black', bg='lightyellow').place(x=440, y=350)
###################### frame2 #################################
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_tdays = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_nsalary = StringVar()

        frame2 = Frame(self.root, bd=5, relief=RIDGE)
        frame2.place(x=700, y=50, width=750, height=350)

        title2 = Label(frame2, text='Employees Salary Details', font=(
            'times new roman', 15), bg='gray', fg='white',).place(x=0, y=0, height=40, width=740)

        lbl_month = Label(frame2, text='Month', font=(
            'times new roman', 14), fg='black').place(x=0, y=50)
        entry_month = Entry(frame2, font=('times new roman', 14), textvariable=self.var_month,
                            fg='black', bg='lightyellow').place(x=60, y=50)

        lbl_year = Label(frame2, text='year', font=(
            'times new roman', 14), fg='black').place(x=250, y=50)
        entry_year = Entry(frame2, font=('times new roman', 14), textvariable=self.var_year,
                           fg='black', bg='lightyellow').place(x=300, y=50)

        lbl_salary = Label(frame2, text='salary', font=(
            'times new roman', 14), fg='black').place(x=490, y=50)
        entry_salary = Entry(frame2, font=(
            'times new roman', 14), textvariable=self.var_salary, fg='black', bg='lightyellow').place(x=550, y=50)

        lbl_totalday = Label(frame2, text='Total Days', font=(
            'times new roman', 14), fg='black').place(x=0, y=100)
        entry_totalday = Entry(frame2, font=(
            'times new roman', 14), textvariable=self.var_tdays, fg='black', bg='lightyellow').place(x=100, y=100)

        lbl_absent = Label(frame2, text='Absent', font=(
            'times new roman', 14), fg='black').place(x=350, y=100)
        entry_absent = Entry(frame2, font=(
            'times new roman', 14), textvariable=self.var_absent, fg='black', bg='lightyellow').place(x=450, y=100)

        lbl_medical = Label(frame2, text='Medical', font=(
            'times new roman', 14), fg='black').place(x=0, y=140)
        entry_medical = Entry(frame2, font=(
            'times new roman', 14), textvariable=self.var_medical, fg='black', bg='lightyellow').place(x=100, y=140)

        lbl_pf = Label(frame2, text='PF', font=(
            'times new roman', 14), fg='black').place(x=350, y=140)
        entry_pf = Entry(frame2, font=(
            'times new roman', 14), textvariable=self.var_pf, fg='black', bg='lightyellow').place(x=450, y=140)

        lbl_convence = Label(frame2, text='convence', font=(
            'times new roman', 14), fg='black').place(x=0, y=180)
        entry_convence = Entry(frame2, font=(
            'times new roman', 14), textvariable=self.var_convence, fg='black', bg='lightyellow').place(x=100, y=180)

        lbl_netsalary = Label(frame2, text='Net Salary', font=(
            'times new roman', 14), fg='black').place(x=350, y=180)
        entry_netsalary = Entry(frame2, font=(
            'times new roman', 14), textvariable=self.var_nsalary, fg='black', bg='lightyellow').place(x=450, y=180)
# ===================button frame ===================================#

        btnframe = Frame(frame2, bd=5, relief=RIDGE, bg='gray')
        btnframe.place(x=180, y=230, width=390, height=100)
#  command=self.calculate,
        btn_calculate = Button(btnframe, text='Calculate', font=(
            'times new roman', 16), command=self.calculate, bg='#5ea873', fg='lightblue', bd='5', padx=10)
        btn_calculate.place(x=0, y=0, width=127)

        btn_save = Button(btnframe, text='Save', font=(
            'times new roman', 16), command=self.add, bg='#368216', fg='lightblue', bd='5', padx=10)
        btn_save.place(x=127, y=0, width=127)

        btn_clear = Button(btnframe, text='Clear', font=(
            'times new roman', 16), command=self.clear_fields, bg='#bf6347', fg='lightblue', bd='5', padx=10)
        btn_clear.place(x=255, y=0, width=127)

        btn_update = Button(btnframe, text='Update', font=(
            'times new roman', 16), command=self.update, bg='#03a66a', fg='lightblue', bd='5', padx=10)
        btn_update.place(x=0, y=45, width=190)

        btn_delete = Button(btnframe, text='Delete', font=(
            'times new roman', 16), command=self.delete, bg='#d12637', fg='lightblue', bd='5', padx=10)
        btn_delete.place(x=192, y=45, width=190)


# #####################   frame 3 ===================================

        frame3 = Frame(self.root, bd=5, relief=RIDGE)
        frame3.place(x=700, y=400, width=750, height=350)

# =============  calculator Frame ======================#
        self.var_text = StringVar()
        self.var_operator = ''
# to add text on clicked button

        def btn_click(num):
            self.var_operator = self.var_operator + str(num)
            self.var_text.set(self.var_operator)
            # print(num)
# to show results after evaluating the function

        def result():
            res = str(eval(self.var_operator))
            self.var_text.set(res)
            self.var_operator = ''
# clear the text from the txt_results field

        def clear_cal():
            self.var_text.set('')
            self.var_operator = ''
        cal_frame = Frame(frame3, relief=RIDGE, bd=2,
                          bg='#475c54')
        cal_frame.place(x=2, y=2, width=300, height=287)

        txt_result = Entry(cal_frame, bg='lightyellow', textvariable=self.var_text,
                           font=('times new roman', 18), justify=RIGHT)
        txt_result.place(x=4, y=4, width=290, height=40)

################################   btn's of calculator #################################

# ===================Row1 =================
        btn_7 = Button(cal_frame, text='7', command=lambda: btn_click(7), bg='gray', bd=3, fg='white',
                       font=('times new roman', 20)).place(x=4, y=47, width=70, height=60)

        btn_8 = Button(cal_frame, text='8', command=lambda: btn_click(8), bg='gray', bd=3, fg='white',
                       font=('times new roman', 20)).place(x=77, y=47, width=70, height=60)

        btn_9 = Button(cal_frame, text='9', command=lambda: btn_click(9), bg='gray', bd=3, fg='white',
                       font=('times new roman', 20)).place(x=150, y=47, width=70, height=60)

        btn_div = Button(cal_frame, text='/', command=lambda: btn_click('/'), bg='gray', bd=3, fg='white',
                         font=('times new roman', 20)).place(x=223, y=47, width=70, height=60)

# =================== Row2 =================
        btn_4 = Button(cal_frame, text='4', command=lambda: btn_click(4), bg='gray', bd=3, fg='white',
                       font=('times new roman', 20)).place(x=4, y=107, width=70, height=60)

        btn_5 = Button(cal_frame, text='5', command=lambda: btn_click(5), bg='gray', bd=3, fg='white',
                       font=('times new roman', 20)).place(x=77, y=107, width=70, height=60)

        btn_6 = Button(cal_frame, text='6', command=lambda: btn_click(6), bg='gray', bd=3, fg='white',
                       font=('times new roman', 20)).place(x=150, y=107, width=70, height=60)

        btn_mul = Button(cal_frame, text='*', command=lambda: btn_click('*'), bg='gray', bd=3, fg='white',
                         font=('times new roman', 20)).place(x=223, y=107, width=70, height=60)

# ===================Row3 =================
        btn_1 = Button(cal_frame, text='1', command=lambda: btn_click(1), bg='gray', bd=3, fg='white',
                       font=('times new roman', 20)).place(x=4, y=168, width=70, height=60)

        btn_2 = Button(cal_frame, text='2', command=lambda: btn_click(2), bg='gray', bd=3, fg='white',
                       font=('times new roman', 20)).place(x=77, y=168, width=70, height=60)

        btn_3 = Button(cal_frame, text='3', command=lambda: btn_click(3), bg='gray', bd=3, fg='white',
                       font=('times new roman', 20)).place(x=150, y=168, width=70, height=60)

        btn_sub = Button(cal_frame, text='-', command=lambda: btn_click('-'), bg='gray', bd=3, fg='white',
                         font=('times new roman', 20)).place(x=223, y=168, width=70, height=60)

# ===================Row4 =================
        btn_0 = Button(cal_frame, text='0', command=lambda: btn_click(0), bg='gray', bd=3, fg='white',
                       font=('times new roman', 20)).place(x=4, y=230, width=70, height=50)

        btn_clear = Button(cal_frame, text='C', command=clear_cal, bg='gray', bd=3, fg='white',
                           font=('times new roman', 20)).place(x=77, y=230, width=70, height=50)

        btn_sum = Button(cal_frame, text='+', command=lambda: btn_click('+'), bg='gray', bd=3, fg='white',
                         font=('times new roman', 20)).place(x=150, y=230, width=70, height=50)

        btn_equal = Button(cal_frame, text='=', command=result, bg='gray', bd=3, fg='white',
                           font=('times new roman', 20)).place(x=223, y=230, width=70, height=50)
# ============================================================================================================

# ..........................salary frame ................................

        sal_frame = Frame(frame3, bd=4, relief=RIDGE)
        sal_frame.place(x=305, y=0, width=435, height=290)

        sal_title = Label(sal_frame, text='Salary Receipt', font=(
            'times new roman', 20), bg='#3b5186', fg='white', anchor='w', padx=10).place(x=0, y=0, relwidth=1)

        sal_frame2 = Frame(sal_frame, bd=2, relief=RIDGE)
        sal_frame2.place(x=0, y=38, relwidth=1, height=245)
        # ----------------------------------------------------------------Sample of receipt
        self.sample = f''' \t Company Name : XYZ\n\t Address : XYZ, Shabbir's house
--------------------------------------------------------
    Employee ID\t\t :  ****
    Salary of\t\t :  MM-YYYY
    Generated on\t\t :  DD-MM-YYYY
--------------------------------------------------------
    Total Days \t\t :  DD
    Total Present\t\t :  DD
    Total Absent\t\t :  DD
    Convince  \t\t :  Rs.----
    Medical \t\t :  Rs.----
    PF \t\t :  Rs.----
    Gross Payment\t\t :  Rs.----
    Net Salary \t\t :  Rs.----
---------------------------------------------------------
This is Computer generated slip , not required any
signature

'''

        scroll_y = Scrollbar(sal_frame2, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_salary_receipt = Text(sal_frame2, font=(
            'times new roman', 15), bg='lightyellow', yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END, self.sample)

        btn_delete = Button(frame3, text='Print', font=(
            'times new roman', 16), command=self.print, bg='#7b09b0', fg='lightblue', bd='5', padx=10)
        btn_delete.place(x=600, y=295, width=120)

        self.check_connection()
    # fucntions starting here ========

# -------------------------------------------searching by employee id =================
    def search(self):
        try:
            emp_id = self.var_empcode.get().strip()
            if not emp_id.isdigit():
                messagebox.showerror('Error', 'Invalid Employee ID')
                return

            con = connector.connect(
                host='localhost', port='3306', user='root', password='', database='ems')
            cur = con.cursor()
            cur.execute("SELECT * FROM employee WHERE e_id=%s", (emp_id,))
            row = cur.fetchone()

            if row is None:
                self.clear_fields()
                messagebox.showerror('Error', 'Employee not found')
            else:
                self.var_empcode.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gander.set(row[4])
                self.var_email.set(row[5])
                self.var_hlocation.set(row[6])
                self.var_dob.set(row[7])
                self.var_doj.set(row[8])
                self.var_experience.set(row[9])
                self.var_proofid.set(row[10])
                self.var_contact.set(row[11])
                self.var_status.set(row[12])
                self.var_address.set(row[13])  # Use .set() for StringVar
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_salary.set(row[16])
                self.var_tdays.set(row[17])
                self.var_absent.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_convence.set(row[21])
                self.var_nsalary.set(row[22])
                file_path = 'D:/UOBS2023/Database System/Database+Sql/EmployManagmentSystem/SalaryReceipt/' + \
                    str(row[23])
                file_ = open(file_path, 'r')
                self.txt_salary_receipt.delete('1.0', END)
                for i in file_:
                    self.txt_salary_receipt.insert(END, i)

                file_.close()
        except connector.Error as err:
            messagebox.showerror('Error', f'Database error: {err}')

        except Exception as ex:
            messagebox.showerror('Error', f'An error occurred: {str(ex)}')

# ----------------------Delete from database --------------------
    def delete(self):
        try:
            emp_id = self.var_empcode.get().strip()
            if not emp_id.isdigit():
                messagebox.showerror('Error', 'Invalid Employee ID')
                return
            con = connector.connect(
                host='localhost', port='3306', user='root', password='', database='ems')
            cur = con.cursor()
            cur.execute("SELECT * FROM employee WHERE e_id=%s", (emp_id,))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror('Error', 'Employee not found')
            else:
                op = messagebox.askyesno(
                    'Confirm!', 'Are you really want to delete')
                if op == True:
                    cur.execute('delete from employee where e_id=%s',
                                (self.var_empcode.get(),))
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        'Delete', "Employee deleted successfully ")
                    self.clear_fields()
        except connector.Error as err:
            messagebox.showerror('Error', f'Database error: {err}')

        except Exception as ex:
            messagebox.showerror('Error', f'An error occurred: {str(ex)}')

# -------------------------------------------insert into the database

    def add(self):
        e_id = self.var_empcode.get()
        designation = self.var_designation.get()
        name = self.var_name.get()
        age = self.var_age.get()
        gander = self.var_gander.get()
        email = self.var_email.get()
        hr_location = self.var_hlocation.get()
        designation = self.var_designation.get()
        dob = self.var_dob.get()
        doj = self.var_doj.get()
        experience = self.var_experience.get()
        proofid = self.var_proofid.get()
        contact = self.var_contact.get()
        status = self.var_status.get()
        address = self.var_address.get()
        month = self.var_month.get()
        year = self.var_year.get()
        salary = self.var_salary.get()
        tdays = self.var_tdays.get()
        absent = self.var_absent.get()
        medical = self.var_medical.get()
        pf = self.var_pf.get()
        convince = self.var_convence.get()
        nsalary = self.var_nsalary.get()
        receipt = self.var_empcode.get()+'.txt'

    # Check if any of the required fields are empty
        if (e_id == '' or name == '' or email == ''
                or contact == '' or designation == ''):
            messagebox.showerror('Error!', 'Please fill all the fields.')
        else:
            con = connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='ems'
            )
            cur = con.cursor()

            cur.execute("SELECT * FROM employee WHERE e_id=%s OR email=%s OR contact=%s",
                        (e_id, email, contact))
            existing_user = cur.fetchone()

            if existing_user:
                messagebox.showerror(
                    'Error!', 'User with the same Employee_id, email, or contact already exists.')
            else:
                cur.execute("INSERT INTO employee VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (e_id, designation, name, age, gander, email, hr_location, dob, doj, experience, proofid, contact, status,
                             address, month, year, salary, tdays, absent, medical, pf, convince, nsalary, receipt))
                con.commit()
                con.close()
                file_path = 'D:/UOBS2023/Database System/Database+Sql/EmployManagmentSystem/SalaryReceipt/' + \
                    str(self.var_empcode.get()) + '.txt'
                file_ = open(file_path, 'w')
                file_.write(self.txt_salary_receipt.get('1.0', END))
                file_.close()

                messagebox.showinfo('Success!', 'Data inserted successfully')

# ------------------Update data------------------------
    def update(self):
        e_id = self.var_empcode.get()
        designation = self.var_designation.get()
        name = self.var_name.get()
        age = self.var_age.get()
        gander = self.var_gander.get()
        email = self.var_email.get()
        hr_location = self.var_hlocation.get()
        designation = self.var_designation.get()
        dob = self.var_dob.get()
        doj = self.var_doj.get()
        experience = self.var_experience.get()
        proofid = self.var_proofid.get()
        contact = self.var_contact.get()
        status = self.var_status.get()
        address = self.var_address.get()
        month = self.var_month.get()
        year = self.var_year.get()
        salary = self.var_salary.get()
        tdays = self.var_tdays.get()
        absent = self.var_absent.get()
        medical = self.var_medical.get()
        pf = self.var_pf.get()
        convince = self.var_convence.get()
        nsalary = self.var_nsalary.get()
        receipt = self.var_empcode.get()+'.txt'

    # Check if any of the required fields are empty
        if (e_id == ''):
            messagebox.showerror(
                'Error!', 'Employee Id needs to be Update the data')
        else:
            con = connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='ems'
            )
            cur = con.cursor()
            cur.execute("UPDATE `employee` SET `designation`=%s,`name`=%s,`age`=%s,`gander`=%s,`email`=%s,`hr_location`=%s,`dob`=%s,`doj`=%s,`experience`=%s,`proofid`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`salary`=%s,`tdays`=%s,`absent`=%s,`medical`=%s,`pf`=%s,`convince`=%s,`nsalary`=%s,`salary_receipt`=%s WHERE `e_id`=%s", (designation, name, age, gander, email, hr_location, dob, doj, experience, proofid, contact, status,
                                                                                                                                                                                                                                                                                                                                                               address, month, year, salary, tdays, absent, medical, pf, convince, nsalary, receipt, e_id))
            con.commit()
            con.close()
            file_path = 'D:/UOBS2023/Database System/Database+Sql/EmployManagmentSystem/SalaryReceipt/' + \
                str(self.var_empcode.get()) + '.txt'
            file_ = open(file_path, 'w')
            file_.write(self.txt_salary_receipt.get('1.0', END))
            file_.close()

            messagebox.showinfo('Success!', 'Data Updated successfully')


# =============calculation of the total amount of money -----


    def calculate(self):
        if (self.var_month.get() == '' or self.var_year.get() == '' or self.var_salary.get() == '' or self.var_tdays.get() == '' or self.var_absent.get() == '' or self.var_medical.get() == '' or self.var_pf.get() == '' or self.var_convence.get() == ''):
            messagebox.showerror('error', 'All fields are required')
        else:
            per_day = int(self.var_salary.get()) / int(self.var_tdays.get())
            work_day = int(self.var_tdays.get()) - int(self.var_absent.get())
            sal_ = per_day*work_day
            deduct = int(self.var_medical.get()) + int(self.var_pf.get())
            addition = int(self.var_convence.get())
            net_sal = sal_-(deduct+addition)
            self.var_nsalary.set(int(round(net_sal, 2)))
            # update the receipt
            new_sample = f''' \t Company Name : XYZ\n\t Address : XYZ, Shabbir house
--------------------------------------------------------
    Employee ID\t\t :  {self.var_empcode.get()}
    Salary of\t\t :  {self.var_month.get()}-{self.var_year.get()}
    Generated on\t\t :  {str(time.strftime("%d %m %y"))}
--------------------------------------------------------
    Total Days \t\t :  {self.var_tdays.get()}
    Total Present\t\t :  {str(int(self.var_tdays.get())-int(self.var_absent.get()))}
    Total Absent\t\t :  {self.var_absent.get()}
    Convince  \t\t :  Rs.{self.var_convence.get()}
    Medical \t\t :  Rs.{self.var_medical.get()}
    PF \t\t :  Rs.{self.var_pf.get()}
    Gross Payment\t\t :  Rs.{self.var_salary.get()}
    Net Salary \t\t :  Rs.{self.var_nsalary.get()}
---------------------------------------------------------
This is Computer generated slip , not required any
signature
'''
            self.txt_salary_receipt.delete('1.0', END)
            self.txt_salary_receipt.insert(END, new_sample)

    def clear_fields(self):
        self.var_empcode.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gander.set('')
        self.var_email.set('')
        self.var_hlocation.set('')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_experience.set('')
        self.var_proofid.set('')
        self.var_contact.set('')
        self.var_status.set('')
        self.var_address.set('')
        self.var_month.set('')
        self.var_year.set('')
        self.var_salary.set('')
        self.var_tdays.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_nsalary.set('')
        self.txt_salary_receipt.delete('1.0', END)
        self.txt_salary_receipt.insert(END, self.sample)
# ------------------------------------------------checking the connection-----------------

    def check_connection(self):
        try:
            con = connector.connect(
                host='localhost', port='3306', user='root', password='', database='ems')
            cur = con.cursor()
            cur.execute('select * from employee')
            rows = cur.fetchall()
            # print(rows)
        except Exception as ex:
            messagebox.showerror('Error', f'error due to {str(ex)}')

# -------------------------show All employee details in another frame----------------------------------------------------------------
    def showdetails(self):
        try:
            con = connector.connect(
                host='localhost', port='3306', user='root', password='', database='ems')
            cur = con.cursor()
            cur.execute('select * from employee')
            rows = cur.fetchall()
            # print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for content in rows:
                self.employee_tree.insert('', END, values=content)
            con.close()
        except Exception as ex:
            messagebox.showerror('Error', f'error due to {str(ex)}')

    def employee_frame(self):
        self.root2 = Toplevel(self.root)
        self.root2.title(
            "Employ payroll Management System || by UOBS Students")
        self.root2.geometry('1490x750+50+50')
        self.root2.config(bg='white')
        title1 = Label(self.root2, text="All Employ Details", font=(
            'Times New Roman', 20), bg='#3b5186', fg='white').pack(side=TOP, fill=X)
        self.root2.focus_force()
        Scrolly = Scrollbar(self.root2, orient=VERTICAL)
        Scrollx = Scrollbar(self.root2, orient=HORIZONTAL)

        Scrolly.pack(side=RIGHT, fill=Y)
        Scrollx.pack(side=BOTTOM, fill=X)

        self.employee_tree = ttk.Treeview(self.root2, columns=(
            'e_id', 'designation', 'name', 'age', 'gander', 'email', 'hr_location', 'dob', 'doj', 'experience', 'proofid', 'contact', 'status', 'address', 'month', 'year', 'salary', 'tdays', 'absent', 'medical', 'pf', 'convince', 'nsalary', 'salary_receipt'), yscrollcommand=Scrolly.set, xscrollcommand=Scrollx.set)
        self.employee_tree.heading('e_id', text='EID')
        self.employee_tree.heading('designation', text='DESIGNATION')
        self.employee_tree.heading('name', text='NAME')
        self.employee_tree.heading('age', text='AGE')
        self.employee_tree.heading('gander', text='GANDER')
        self.employee_tree.heading('email', text='EMAIL')
        self.employee_tree.heading('hr_location', text='HIRED LOCATION')
        self.employee_tree.heading('dob', text='D-O-B')
        self.employee_tree.heading('doj', text='D-O-JOIN')
        self.employee_tree.heading('experience', text='EXPERIENCE')
        self.employee_tree.heading('proofid', text='PROOFID')
        self.employee_tree.heading('contact', text='CONTACT')
        self.employee_tree.heading('status', text='STATUS')
        self.employee_tree.heading('address', text='ADDRESS')
        self.employee_tree.heading('month', text='MONTH')
        self.employee_tree.heading('year', text='YEAR')
        self.employee_tree.heading('salary', text='SALARY')
        self.employee_tree.heading('tdays', text='TOTAL DAYS')
        self.employee_tree.heading('absent', text='ABSENT')
        self.employee_tree.heading('medical', text='MEDICAL')
        self.employee_tree.heading('pf', text='PF')
        self.employee_tree.heading('convince', text='CONVINCE')
        self.employee_tree.heading('nsalary', text='NET SALARY')
        self.employee_tree.heading('salary_receipt', text='SALARY RECEIPT')
        self.employee_tree['show'] = 'headings'
        self.employee_tree.column('e_id', width=70)
        self.employee_tree.column('designation', width=100)
        self.employee_tree.column('name', width=100)
        self.employee_tree.column('age', width=100)
        self.employee_tree.column('gander', width=100)
        self.employee_tree.column('email', width=100)
        self.employee_tree.column('hr_location', width=120)
        self.employee_tree.column('dob', width=100)
        self.employee_tree.column('doj', width=100)
        self.employee_tree.column('experience', width=100)
        self.employee_tree.column('proofid', width=100)
        self.employee_tree.column('contact', width=100)
        self.employee_tree.column('status', width=100)
        self.employee_tree.column('address', width=300)
        self.employee_tree.column('month', width=100)
        self.employee_tree.column('year', width=100)
        self.employee_tree.column('salary', width=100)
        self.employee_tree.column('tdays', width=100)
        self.employee_tree.column('absent', width=100)
        self.employee_tree.column('medical', width=100)
        self.employee_tree.column('pf', width=100)
        self.employee_tree.column('convince', width=100)
        self.employee_tree.column('nsalary', width=100)
        self.employee_tree.column('salary_receipt', width=140)

        Scrolly.config(command=self.employee_tree.yview)
        Scrollx.config(command=self.employee_tree.xview)

        self.employee_tree.pack(fill=BOTH, expand=1)
        self.showdetails()
        self.root2.mainloop()

        # =----------------------------print the employee details --------------------------------
    def print(self):
        file_ = tempfile.mktemp(".txt")
        open(file_, 'w').write(self.txt_salary_receipt.get('1.0', END))
        os.startfile(file_, 'print')


root = Tk()
obj = employsystem(root)
root.mainloop()
