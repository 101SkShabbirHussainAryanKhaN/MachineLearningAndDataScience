"""Description:
Before Run this code you have to start your xampp and create a database named as 
'employeemanangementsystem' then create a table named as 'emp_salary' 
that contain 24 items var_emp_code,  var_Designation , name , age,
gender , email , hiredlo, txt_address , dob , doj , experience,
proofid , contact , status , month , year , salary , medical,
pf , conveyance ,  totaldays , absents ,netsalary , receipt 
make a folder named as receipt and give the folder path in
file_=open("F:/ProGramming SK'S World/PythOn/Database/receipt") """
import tkinter
from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
import pymysql
import time
import os
import tempfile
class employeesystem:
    def __init__(self,root):
        self.root=root
        self.root.title('Employee Payroll Management System | By SK Company pvt Ltd.')
        
        

        self.root.geometry('1450x700+0+0')
        self.root.configure(bg='green')
       

        # Set the window icon
        self.root.iconbitmap(r"F:/Employee Manangement System/skjaan.png")
       



       
        
        title1=Label(self.root,text='Employee PayRoll Management System',font=('times new roman bold italic',20),
        bg='darkblue',fg='white').place(x=0,y=0,relwidth=1)
        btn_show_employees=Button(self.root,text='All Employee Details',font=('times new roman bold italic',14),
                          fg='white',bg='green',command=self.employeeframe).place(x=1070,y=0)
        
        # Add a copyright label
        copyright_label = Label(root, text="© 2023 SK Company Pvt Ltd. All Rights Reserved", fg="white",bg='blue',font=('vardana bold italic',20))
        copyright_label.pack(side="bottom")

        ############### Frame1#########################
        ###########variables###############
        self.var_emp_code=StringVar()
        self.var_Designation=StringVar()
        self.name=StringVar()
        self.age=StringVar()
        self.gender=StringVar()
        self.email=StringVar()
        self.hiredloc=StringVar()
        #self.address=StringVar()
       
        self.dob=StringVar()
        self.doj=StringVar()
        self.experience=StringVar()
        self.proofid=StringVar()
        self.contact=StringVar()
        self.status=StringVar()
        



# ------------------------------------------Frame 1------------------------------------------------------

        frame1=Frame(self.root,bd=5,relief=SOLID,bg='green')
        frame1.place(x=30,y=50,width=650,height=600)
        title2=Label(frame1,text='Employee Details',font=('times new roman bold italic',20),bg='darkblue',fg='white').place(x=0,y=0,relwidth=1)
        lbl_empcode=Label(frame1,text='Employee Code',font=('times new roman bold italic',14),fg='black',bg='lightgray')
        lbl_empcode.place(x=0,y=40)
        self.entry_empcode=Entry(frame1,font=('times new roman bold italic',13),textvariable=self.var_emp_code,fg='black',bg='lightgray')
        self.entry_empcode.place(x=150,y=40)
        
        btn_search=Button(frame1,text='Search',font=('times new roman bold italic',10),command=self.search,fg='black',bg='lightblue')
        btn_search.place(x=340,y=40)
       
        lbl_designation=Label(frame1,text='Designation',font=('times new roman bold italic',14),fg='black').place(x=0,y=80)
        entry_designation=Entry(frame1,font=('times new roman bold italic',14),textvariable=self.var_Designation,fg='black',bg='lightyellow').place(x=120,y=80)
        
        lbl_name=Label(frame1,text='Name',font=('times new roman bold italic',14),fg='black').place(x=0,y=120)
        entry_name=Entry(frame1,font=('times new roman bold italic',14),textvariable=self.name,fg='black',bg='lightyellow').place(x=120,y=120)

        
        lbl_age=Label(frame1,text='Age',font=('times new roman bold italic',14),fg='black').place(x=0,y=160)
        entry_age=Entry(frame1,font=('times new roman bold italic',14),textvariable=self.age,fg='black',bg='lightyellow').place(x=120,y=160)

        

        lbl_gender=Label(frame1,text='Gender',font=('times new roman bold italic',14),fg='black').place(x=0,y=200)
        entry_dgender=Entry(frame1,font=('times new roman bold italic',14),textvariable=self.gender,fg='black',bg='lightyellow').place(x=120,y=200)
        
        lbl_email=Label(frame1,text='Email',font=('times new roman bold italic',14),fg='black').place(x=0,y=240)
        entry_email=Entry(frame1,font=('times new roman bold italic',14),textvariable=self.email,fg='black',bg='lightyellow').place(x=120,y=240)
        
        
        
        lbl_hireloc=Label(frame1,text='Hired Location',font=('times new roman bold italic',14),fg='black').place(x=0,y=280)
        entry_hireloc=Entry(frame1,font=('times new roman bold italic',14),textvariable=self.hiredloc,fg='black',bg='lightyellow').place(x=120,y=280)
        
        
        lbl_address=Label(frame1,text='Address',font=('times new roman bold italic',14),fg='black').place(x=0,y=320)
        self.txt_address=Text(frame1,font=('times new roman bold italic',14),fg='black',bg='lightyellow',width=51,height=3)
        self.txt_address.place(x=120,y=320)

        

        lbl_DOB=Label(frame1,text='DOB',font=('times new roman bold italic',14),fg='black').place(x=345,y=80)
        entry_DOB=Entry(frame1,font=('times new roman bold italic',14),textvariable=self.dob,fg='black',bg='lightyellow').place(x=435,y=80)
        
        lbl_DOJ=Label(frame1,text='DOJ',font=('times new roman bold italic',14),fg='black').place(x=345,y=120)
        entry_DOJ=Entry(frame1,font=('times new roman bold italic',14),textvariable=self.doj,fg='black',bg='lightyellow').place(x=435,y=120)

        
        lbl_experience=Label(frame1,text='Experience',font=('times new roman bold italic',14),fg='black').place(x=345,y=160)
        entry_experience=Entry(frame1,font=('times new roman bold italic',14),textvariable=self.experience,fg='black',bg='lightyellow').place(x=441,y=160)

        
        lbl_proofid=Label(frame1,text='ProofID',font=('times new roman bold italic',14),fg='black').place(x=345,y=200)
        entry_proofid=Entry(frame1,font=('times new roman bold italic',14),textvariable=self.proofid,fg='black',bg='lightyellow').place(x=435,y=200)
        
        lbl_contact=Label(frame1,text='Contact',font=('times new roman bold italic',14),fg='black').place(x=335,y=240)
        entry_contact=Entry(frame1,font=('times new roman bold italic',14),textvariable=self.contact,fg='black',bg='lightyellow').place(x=435,y=240)
        
        lbl_status=Label(frame1,text='Status',font=('times new roman bold italic',14),fg='black').place(x=335,y=280)
        entry_status=Entry(frame1,font=('times new roman bold italic',14),textvariable=self.status,fg='black',bg='lightyellow').place(x=435,y=280)
        
       
        

       
        ############### Frame2#########################
        ##########################variavles##############
        self.month=StringVar()
        self.year=StringVar()
        self.salary=StringVar()
        self.totaldays=StringVar()
        self.absents=StringVar()
        self.medical=StringVar()
        self.conveyance =StringVar()
        self.pf=StringVar()
        self.netsalary=StringVar()

    




# ---------------------------------------- Frame 2 ----------------------------------------------------
        frame2=Frame(self.root,bd=5,relief=SOLID,bg='green')
        frame2.place(x=700,y=50,width=650,height=300)
        title3=Label(frame2,text='Employee Salary Details',font=('times new roman bold italic',20),bg='darkblue',fg='white').place(x=0,y=0,relwidth=1)
        
        
        lbl_month=Label(frame2,text='Month',font=('times new roman bold italic',10),fg='black').place(x=0,y=40)
        entry_month=Entry(frame2,font=('times new roman bold italic',11),textvariable=self.month,fg='black',bg='lightyellow').place(x=45,y=40)
        
        lbl_year=Label(frame2,text='Year',font=('times new roman bold italic',10),fg='black').place(x=200,y=40)
        entry_year=Entry(frame2,font=('times new roman bold italic',11),fg='black',textvariable=self.year,bg='lightyellow').place(x=235,y=40)
        
        lbl_salary=Label(frame2,text='Salary',font=('times new roman bold italic',10),fg='black').place(x=395,y=40)
        entry_salary=Entry(frame2,font=('times new roman bold italic',11),fg='black',textvariable=self.salary,bg='lightyellow').place(x=445,y=40)
        
        lbl_totaldays=Label(frame2,text='Total Days',font=('times new roman bold italic',14),fg='black').place(x=0,y=70)
        entry_totaldays=Entry(frame2,font=('times new roman bold italic',14),textvariable=self.totaldays,fg='black',bg='lightyellow').place(x=95,y=70)

        

        lbl_medical=Label(frame2,text='Medical',font=('times new roman bold italic',14),fg='black').place(x=0,y=100)
        entry_medical=Entry(frame2,font=('times new roman bold italic',14),textvariable=self.medical,fg='black',bg='lightyellow').place(x=95,y=100)
        
        lbl_conveyance =Label(frame2,text='Conveyance',font=('times new roman bold italic',14),fg='black').place(x=0,y=130)
        entry_conveyance =Entry(frame2,font=('times new roman bold italic',14),textvariable=self.conveyance ,fg='black',bg='lightyellow').place(x=102,y=130)

        
        
        lbl_absents=Label(frame2,text='Absent',font=('times new roman bold italic',14),fg='black').place(x=315,y=70)
        entry_absent=Entry(frame2,font=('times new roman bold italic',14),textvariable=self.absents,fg='black',bg='lightyellow').place(x=400,y=70)

        
        lbl_PF=Label(frame2,text='PF',font=('times new roman bold italic',14),fg='black').place(x=315,y=100)
        entry_PF=Entry(frame2,font=('times new roman bold italic',14),textvariable=self.pf,fg='black',bg='lightyellow').place(x=400,y=100)
        
        lbl_netsalary=Label(frame2,text='Net Salary',font=('times new roman bold italic',14),fg='black').place(x=315,y=130)
        entry_netsalary=Entry(frame2,font=('times new roman bold italic',14),textvariable=self.netsalary,fg='black',bg='lightyellow').place(x=405,y=130)
        
        btn_calculate=Button(frame2,text='    Calculate    ',command=self.calculate,font=('times new roman bold italic',14),
                          fg='black',bg='lightblue').place(x=120,y=170)
        
        self.btn_save=Button(frame2,text='        Save        ',command=self.add,font=('times new roman bold italic',14),fg='black',bg='lightcyan')
        self.btn_save.place(x=243,y=170)
        
        btn_clear=Button(frame2,text='        Clear        ',command=self.clear,font=('times new roman bold italic',14),
                          fg='black',bg='aqua').place(x=375,y=170)
      
        self.btn_update=Button(frame2,text='              Update             ',command=self.update,font=('times new roman bold italic',14),
                          fg='black',bg='lightgreen')
        self.btn_update.place(x=120,y=207)
        
        self.btn_delete=Button(frame2,text='             Delete            ',command=self.delete,font=('times new roman bold italic',14),
                          fg='black',bg='crimson')
        self.btn_delete.place(x=323,y=207)
        
        #self.check_connection()
        
# -------------------------------------------- Frame 3 ---------------------------------------------------
        frame3=Frame(self.root,bd=5,relief=SOLID , bg='green')
        frame3.place(x=700,y=350,width=650,height=300)

        self.var_text=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_text.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_text.set(res)
            self.var_operator=''

        def clear_cal():
           self.var_text.set('')
           self.var_operator='' 

        cal_frame=Frame(frame3,bd=5,relief=SOLID, bg='green')
        cal_frame.place(x=0,y=0,width=235,height=280)
        entry_cal=Entry(cal_frame,font=('times new roman',18,'bold'),
                        textvariable=self.var_text,justify=RIGHT,fg='black',bg='lightyellow')
        entry_cal.place(x=0,y=0,width=224,height=50)

        
        btn_n7=Button(cal_frame,text=' 7 ',command=lambda:btn_click(7),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=2,y=52,width=55,height=50)
        
        btn_n8=Button(cal_frame,text=' 8 ',command=lambda:btn_click(8),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=57,y=52,width=55,height=50)
        
        btn_n9=Button(cal_frame,text=' 9 ',command=lambda:btn_click(9),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=112,y=52,width=55,height=50)
        
        btn_ndiv=Button(cal_frame,text=' / ',command=lambda:btn_click('/'),font=('times new roman bold italic',14),
                          fg='white',bg='green').place(x=167,y=52,width=55,height=55)
        
        
        btn_n4=Button(cal_frame,text=' 4 ',command=lambda:btn_click(4),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=2,y=102,width=55,height=50)

        btn_n5=Button(cal_frame,text=' 5 ',command=lambda:btn_click(5),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=57,y=102,width=55,height=50)
        btn_n6=Button(cal_frame,text=' 6 ',command=lambda:btn_click(6),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=112,y=102,width=55,height=50)
        
        btn_nmul=Button(cal_frame,text=' * ',command=lambda:btn_click('*'),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=167,y=107,width=55,height=55)
        
        btn_n1=Button(cal_frame,text=' 1 ',command=lambda:btn_click(1),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=2,y=152,width=55,height=50)
        btn_n2=Button(cal_frame,text=' 2 ',command=lambda:btn_click(2),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=57,y=152,width=55,height=50)
        btn_n3=Button(cal_frame,text=' 3 ',command=lambda:btn_click(3),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=112,y=152,width=55,height=50)
        btn_nsub=Button(cal_frame,command=lambda:btn_click('-'),text=' - ',font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=167,y=162,width=55,height=55)
        
        btn_0=Button(cal_frame,text=' 0 ',command=lambda:btn_click(0),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=2,y=202,width=55,height=50)
        btn_point=Button(cal_frame,text=' . ',command=lambda:btn_click('.'),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=57,y=202,width=55,height=50)
        btn_plus=Button(cal_frame,text=' + ',command=lambda:btn_click('+'),font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=112,y=202,width=55,height=50)
        btn_equal=Button(cal_frame,text=' = ',command=result,font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=167,y=217,width=55,height=55)
        btn_c=Button(cal_frame,text=' C ',command=clear_cal,font=('times new roman bold italic',18),
                          fg='white',bg='green').place(x=2,y=252,width=165,height=20)
        

        
        ##########################Salary Frame############################
        self.sample=f'''\tOrganization Name, SK Company Pvt Ltd\n\tAddress: Skardu,Baltistan
.......................................................................
Employee ID\t\t:  
Salary of\t\t:  Month-Year
Generated On\t\t: DD-MM-YYYY
.......................................................................
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absent\t\t:  DD
Conveyance\t\t:  Rs.----
Medical\t\t:  Rs.----
PF\t\t:  Rs.----
Gross Payment\t\t:  Rs.-----
Net Salary\t\t:  Rs.-----
.......................................................................
This is computer generated slip, not required    any signature

'''     
        sub_frame3=Frame(frame3,bd=5,relief=SOLID, bg='green')
        sub_frame3.place(x=240,y=0,width=400,height=280)
        title3=Label(sub_frame3,text='Salary Receipt',font=('times new roman bold italic',16),bg='darkblue',fg='white')
        title3.place(x=0,y=0,relwidth=1)
        
        sub_frame4=Frame(sub_frame3,bd=5,relief=SOLID,bg='green')
        sub_frame4.place(x=0,y=30,height=212,width=390)
        
        btn_print=Button(sub_frame3,text=' Print ',command=self.print,font=('times new roman bold italic',18),
                          fg='black',bg='blue')
        btn_print.place(x=270,y=240,width=100,height=25)

        
        
        yscrollbar=Scrollbar(sub_frame4,orient=VERTICAL)
        yscrollbar.pack(fill=Y,side=RIGHT)

        self.txt_salary_receipt=Text(sub_frame4,font=('times new roman bold italic',14),bg='green',fg='white')
        self.txt_salary_receipt.pack(fill=BOTH,expand=1)
        yscrollbar.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert('1.0',self.sample)
    

        

    ###################functions#####################
    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=NORMAL)
        self.btn_delete.config(state=NORMAL)
        self.entry_empcode.config(state=NORMAL)

        self.var_emp_code.set('')
        self.var_Designation.set(' ')
        self.name.set(' ')
        self.age.set(' ')
        self.gender.set(' ')
        self.email.set(' ')
        self.hiredloc.set('')
        self.txt_address.delete('1.0',END),
        self.dob.set(' ')
        self.doj.set(' ')
        self.experience.set(' ')
        self.proofid.set(' ')
        self.contact.set(' ')
        self.status.set(' ')
        self.month.set(' ')
        self.year.set(' ')
        self.salary.set(' ')
        self.medical.set(' ')
        self.pf.set(' ')
        self.conveyance .set(' ')
        self.totaldays.set(' ')
        self.absents.set(' ')
        self.netsalary.set(' ')
        #self.var_emp_code.set()+'.txt'
        #file_=open('salaryreceipt/'+str(' '),'r')
        self.txt_salary_receipt.delete('1.0',END)
        
        self.txt_salary_receipt.insert('1.0',self.sample)
    

    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror('Error','Employee ID is required')
        else:
            try:
                
                con=pymysql.connect(host='localhost',user='root',db='employeemanagementsystem')
                cur=con.cursor()
                cur.execute("select * from emp_salary where var_emp_code=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Employee ID,Please a valid ID')
                else:
                    op=messagebox.askyesno('Confirm','Do you want to delete this record?')
                    if op==True:
                        cur.execute('delete  from emp_salary where var_emp_code=%s',(self.var_emp_code.get()))
                        command=self.clear()
                        con.commit()
                        con.close()
                        

            except Exception as ex:
                messagebox.showerror('Error',f'Error due to:{str(ex)}') 




    def search(self):
        try:
                
            con=pymysql.connect(host='localhost',user='root',db='employeemanagementsystem')
            cur=con.cursor()
            cur.execute("select * from emp_salary where var_emp_code=%s",(self.var_emp_code.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid Employee ID,Please try with another ID')
            else:
                
                print(row)
                self.var_emp_code.set(row[0])
                self.var_Designation.set(row[1])
                self.name.set(row[2])
                self.age.set(row[3])
                self.gender.set(row[4])
                self.email.set(row[5])
                self.hiredloc.set(row[6])
                #self.address.set()
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END,row[7])

                self.dob.set(row[8])
                self.doj.set(row[9])
                self.experience.set(row[10])
                self.proofid.set(row[11])
                self.contact.set(row[12])
                self.status.set(row[13])
                self.month.set(row[14])
                self.year.set(row[15])
                self.salary.set(row[16])
                self.medical.set(row[17])
                self.pf.set(row[18])
                self.conveyance .set(row[19])
                self.totaldays.set(row[20])
                self.absents.set(row[21])
                self.netsalary.set(row[22])
                #self.var_emp_code.set()+'.txt'
                file_=open("F:/Employee Manangement System/receipt"+str(row[23]),'r') # the file should be opened in read mood
                self.txt_salary_receipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_receipt.insert('1.0',i)

                file_.close()
                self.btn_save.config(state=NORMAL)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.entry_empcode.config(state=NORMAL)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to:{str(ex)}') 

    def update(self): 

        if self.var_emp_code.get()=='' or self.netsalary.get()=='':
                messagebox.showerror('Error','Employee code is required') 
        else:
            try:
                
                con=pymysql.connect(host='localhost',user='root',db='employeemanagementsystem')
                cur=con.cursor()
                cur.execute("select * from emp_salary where var_emp_code=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','THis employee is invalid. Try again with another ID')
                else:
                    cur.execute(" UPDATE `emp_salary` SET `var_designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hiredloc`=%s,`address`=%s,`dob`=%s,`doj`=%s,`experience`=%s,`proofid`=%s,`contact`=%s,`status`=%s,`month`=%s,`year`=%s,`salary`=%s,`medical`=%s,`pf`=%s,`conveyance`=%s,`totaldays`=%s,`absents`=%s,`netsalary`=%s,`receipt`=%s where `var_emp_code`=%s",
                                (
                                 self.var_Designation.get(),
                                 self.name.get(),
                                 self.age.get(),
                                 self.gender.get(),
                                 self.email.get(),
                                 self.hiredloc.get(),
                                 #self.address.get(),
                                 self.txt_address.get('1.0',END),
                                 self.dob.get(),
                                 self.doj.get(),
                                 self.experience.get(),
                                 self.proofid.get(),
                                 self.contact.get(),
                                 self.status.get(),
                                 self.month.get(),
                                 self.year.get(),
                                 self.salary.get(),
                                 self.medical.get(),
                                 self.pf.get(),
                                 self.conveyance .get(),
                                 self.totaldays.get(),
                                 self.absents.get(),
                                 self.netsalary.get(),
                                 self.var_emp_code.get()+'.txt',
                                 self.var_emp_code.get()
                                 
                                )
                                )
                    con.commit()
                    con.close()
                    file_=open("F:/Employee Manangement System/receipt"+str(self.var_emp_code.get())+'.txt','w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo('Success','Record Updated Successfully')

                                 
            except Exception as ex:
                messagebox.showerror('Error',f'Error due to:{str(ex)}') 


    def add(self): 
        if self.var_emp_code.get()=='':
                messagebox.showerror('Error','Employee code is required') 
        else:
            try:
                
                con=pymysql.connect(host='localhost',user='root',db='employeemanagementsystem')
                cur=con.cursor()
                cur.execute("select * from emp_salary where var_emp_code=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error','THis employee id is already exists')
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.var_emp_code.get(),
                                 self.var_Designation.get(),
                                 self.name.get(),
                                 self.age.get(),
                                 self.gender.get(),
                                 self.email.get(),
                                 self.hiredloc.get(),
                                 #self.address.get(),
                                 self.txt_address.get('1.0',END),
                                 self.dob.get(),
                                 self.doj.get(),
                                 self.experience.get(),
                                 self.proofid.get(),
                                 self.contact.get(),
                                 self.status.get(),
                                 self.month.get(),
                                 self.year.get(),
                                 self.salary.get(),
                                 self.medical.get(),
                                 self.pf.get(),
                                 self.conveyance .get(),
                                 self.totaldays.get(),
                                 self.absents.get(),
                                 self.netsalary.get(),
                                 self.var_emp_code.get()+'.txt'
                                 
                                )
                                )
                    con.commit()
                    con.close()
                    file_=open("F:/Employee Manangement System/receipt" +str(self.var_emp_code.get())+'.txt','w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo('Success','Record added Successfully')
                                 
            except Exception as ex:
                messagebox.showerror('Error',f'Error due to:{str(ex)}') 
    def calculate(self):
        if self.month.get()==''or self.salary.get()=='' or self.year.get() =='' or self.totaldays.get()=='':
            messagebox.showerror('Error','All fields are required')
        else:
            per_day=int(self.salary.get())/int(self.totaldays.get())
            work_day=int(self.totaldays.get())-int(self.absents.get())
            sal_per=per_day*work_day
            add1=int(self.medical.get())+int(self.pf.get())
            add2=int(self.conveyance.get())
            net_sal=add1+add2+sal_per
            self.netsalary.set(str(round(net_sal,2)))
            #########receipt########################
            newsample=f'''\tOrganization Name, SK Company Pvt Ltd\n\tAddress: Skardu,Baltistan
.......................................................................
Employee ID\t\t:  {self.var_emp_code.get()}
Salary of\t\t:  {self.month.get()}-{self.year.get()}
Generated On\t\t: {str(time.strftime('%d-%m-%Y'))}
.......................................................................
Total Days\t\t:  {self.totaldays.get()}
Total Present\t\t:  {str(int(self.totaldays.get())-int(self.absents.get()))}
Total Absent\t\t:  {self.absents.get()}
Conveyance\t\t:  Rs.{self.conveyance.get()}
Medical\t\t:  Rs.{self.medical.get()}
PF\t\t:  Rs.{self.pf.get()}
Gross Payment\t\t:  Rs.{self.salary.get()}
Net Salary\t\t:  Rs{self.netsalary.get()}
......................................................................
This is computer generated slip, not required    
any signature

'''     

            self.txt_salary_receipt.delete('1.0',END)
            self.txt_salary_receipt.insert('1.0',newsample)

    
    def employeeframe(self):
        self.root2=Toplevel(self.root)
        self.root2.title('Employee Payroll Management System | By SK Company Pvt Ltd')
        self.root2.geometry('1300x600+30+20')
        self.root2.configure(bg='green')
       

        # Set the window icon
        self.root2.iconbitmap(r"F:/Employee Manangement System/skjaan.png")
        title1=Label(self.root2,text='Employee Details',font=('times new roman bold italic',20),
        bg='blue',fg='white').pack(side=TOP,fill=X)
        self.root2.focus_force()
        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        self.employee_tree=ttk.Treeview(self.root2,columns=('empcode', 'designation', 'name', 'age', 'gender', 'email', 'hiredloc',
                                                            'address', 'dob', 'doj', 'experience',
                                                            'proofid', 'contact', 'status', 
                                                            'month', 'year', 'salary', 'medical',
                                                            'pf', 'conveyance', 'totaldays', 'absent', 
                                                            'netsalary', 'receipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('empcode' ,text='Emp ID')
        self.employee_tree.heading('designation' ,text='Designation')
        self.employee_tree.heading('name' ,text='Name')
        self.employee_tree.heading('age' ,text='Age')
        self.employee_tree.heading('gender' ,text='Gender')
        self.employee_tree.heading('email' ,text='Email')
        self.employee_tree.heading('hiredloc' ,text='Hired location')
        self.employee_tree.heading('address' ,text='Address')
        self.employee_tree.heading('dob' ,text='Birth Date')
        self.employee_tree.heading('doj' ,text='Joining Date')
        self.employee_tree.heading('experience' ,text='Experience')
        self.employee_tree.heading('proofid' ,text='Proof ID')
        self.employee_tree.heading('contact' ,text='Contact')
        self.employee_tree.heading('status' ,text='Status')
        self.employee_tree.heading('month' ,text='Month')
        self.employee_tree.heading('year' ,text='Year')
        self.employee_tree.heading('salary' ,text='Basic Salary')
        self.employee_tree.heading('medical' ,text='Medical Allowance')
        self.employee_tree.heading('pf' ,text='PF')
        self.employee_tree.heading('conveyance' ,text='Conveyance Allowance')
        self.employee_tree.heading('totaldays' ,text='Total Days')
        self.employee_tree.heading('absent' ,text='Absents')
        self.employee_tree.heading('netsalary' ,text='NetSalary')
        self.employee_tree.heading('receipt' ,text='Salary Receipt')

        self.employee_tree['show']='headings'

        self.employee_tree.column('empcode',width=70)
        self.employee_tree.column('designation',width=120)
        self.employee_tree.column('name',width=150)
        self.employee_tree.column('age',width=30)
        self.employee_tree.column('gender',width=70)

        self.employee_tree.column('email',width=150)
        self.employee_tree.column('hiredloc',width=100)
        self.employee_tree.column('address',width=70)
        self.employee_tree.column('dob',width=70)
        self.employee_tree.column('doj',width=70)
        self.employee_tree.column('experience' ,width=100)
        self.employee_tree.column('proofid' ,width=100)
        self.employee_tree.column('contact' ,width=70)
        self.employee_tree.column('status' ,width=70)
        self.employee_tree.column('month' ,width=70)
        self.employee_tree.column('year' ,width=70)
        self.employee_tree.column('salary' ,width=70)
        self.employee_tree.column('medical' ,width=120)
        self.employee_tree.column('pf' ,width=70)
        self.employee_tree.column('conveyance' ,width=155)
        self.employee_tree.column('totaldays' ,width=120)
        self.employee_tree.column('absent' ,width=70)
        self.employee_tree.column('netsalary' ,width=150)
        self.employee_tree.column('receipt' ,width=150)

        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)

        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()
        self.root2.mainloop()

    def show(self):

            try:
                    
                con=pymysql.connect(host='localhost',user='root',db='employeemanagementsystem')
                cur=con.cursor()
                cur.execute("select * from emp_salary")
                rows=cur.fetchall()
                self.employee_tree.delete(*self.employee_tree.get_children())
                for row in rows:
                    self.employee_tree.insert('',END,values=row)
                con.close()
            except Exception as ex:
                    messagebox.showerror('Error',f'Error due to:{str(ex)}') 

    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_receipt.get('1.0',END))
        os.startfile(file_,'PRINT')
        
       
        
           
rt=Tk()
obj=employeesystem(rt)
rt.mainloop()

