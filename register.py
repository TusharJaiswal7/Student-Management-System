from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
#import sqlite3
import pymysql 
import os
#from login import Login_window
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry("1530x795+0+0")
        self.root.config(bg="white")
        ##========icons======##
        self.bg=ImageTk.PhotoImage(file="C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\side.png")
        bg=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        ############=====================Register Frame====================================================
        frame1=Frame(self.root,bg='black')
        frame1.place(x=480,y=100,width=700,height=500)
        title=Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg='black',fg="green").place(x=50,y=30)
        #self.var_fname=StringVar()
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg='black',fg="white").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg='black',fg="white").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgrey",)
        self.txt_lname.place(x=370,y=130,width=250)
        #####################===row2
        contact=Label(frame1,text="Contact No",font=("times new roman",15,"bold"),bg='black',fg="white").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg='black',fg="white").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_email.place(x=370,y=200,width=250)
        ####===========row3
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold",),bg='black',fg="white").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER,values=("Select","Your First Pet","Your Birth Place","Your Fest Friend Name"))
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg='black',fg="white").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_answer.place(x=370,y=270,width=250)
        #########################========row4
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg='black',fg="white").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg='black',fg="white").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_cpassword.place(x=370,y=340,width=250)

        ########==============Terms
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree the Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg='black',fg='green',font=('times new roman',12)).place(x=50,y=380)
        
        
        self.btn_img=ImageTk.PhotoImage(file="C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\register.png")
        btn_reg=Button(frame1,image=self.btn_img,bd=0,cursor='hand2',command=self.register_data).place(x=50,y=420)
        btn_login=Button(self.root,text='Sign In',font=("times new roman",20),bd=0,cursor='hand2',command=self.sign_in).place(x=200,y=460,width=150)
    def clear(self):
            self.txt_fname.delete(0,END)
            self.txt_lname.delete(0,END)
            self.txt_contact.delete(0,END)
            self.txt_email.delete(0,END)
            self.txt_answer.delete(0,END)
            self.txt_password.delete(0,END)
            self.txt_cpassword.delete(0,END)
            self.cmb_quest.current(0)

    
    def sign_in(self):
            self.root.destroy()
            #self.after(400,self.sign_in)
            os.system("python login.py")
            #import login
    
    def register_data(self):
        if  self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="": 
                messagebox.showerror("Error","ALL Fields Are Required!!!",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
                messagebox.showerror("Error","Password And Confirm Password Should Be Same!!",parent=self.root)
        elif self.var_chk.get()==0:
                messagebox.showerror("Error","Please Agree The Terms And Condition",parent=self.root)
        else:
                try:
                        #for sql
                        #con=sqlite3.connect(database="student.db")
                        # fro xamp 
                        con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                        cur=con.cursor()
                        cur.execute("select * from employee where email=%s",(self.txt_email.get(),))
                        row=cur.fetchone()
                        #print(row)
                        if row!=None:
                                messagebox.showerror("Error","User already Exist,Please try with another email",parent=self.root)
                        else:
                                cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password)values(%s,%s,%s,%s,%s,%s,%s)",
                                        #For xamp in place of ? use %s
                                        (self.txt_fname.get(),
                                        self.txt_lname.get(),
                                        self.txt_contact.get(),
                                        self.txt_email.get(),
                                        self.cmb_quest.get(),
                                        self.txt_answer.get(),
                                        self.txt_password.get()
                                        ))
                                con.commit()
                                con.close()
                                messagebox.showinfo("Success","Register Successfull",parent=self.root)
                                self.clear()
                                self.sign_in()
                except Exception as es:
                        messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    
#if __name__=="__main__":        
root=Tk()
obj=Register(root)
root.mainloop()