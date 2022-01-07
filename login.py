from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time 
from math import*
import pymysql
from tkinter import messagebox,ttk
import os
#import sqlite3
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x795+0+0")#("1350x750+0+0")
        self.root.config(bg="#021e2f")
        #==================BACKGROUND
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        
        ###=FRAME==================
        login_frame=Frame(self.root,bg='black',bd=5)
        login_frame.place(x=250,y=100,width=800,height=500)
        title=Label(login_frame,text="Login Here",font=("times new roman",30,"bold"),bg="black",fg="#08A3D2").place(x=250,y=50)
        email=Label(login_frame,text="Email Address",font=("times new roman",18,"bold"),bg="black",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",18,),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        pwd=Label(login_frame,text="Password",font=("times new roman",18,"bold"),bg="black",fg="gray").place(x=250,y=250)
        self.txt_pwd=Entry(login_frame,font=("times new roman",18,),bg="lightgray")
        self.txt_pwd.place(x=250,y=280,width=350,height=35)

        btn_reg=Button(login_frame,text="Register new Account",font=("times new roman",15),bg='black',bd=0,fg="#B00857",cursor='hand2',command=self.register).place(x=250,y=320)
        btn_forget=Button(login_frame,text="Forget Password?",font=("times new roman",15),bg='black',bd=0,fg="#B00857",cursor='hand2',command=self.forget_password_window).place(x=450,y=320)
        btn_log=Button(login_frame,text="Login",font=("times new roman",20),fg='black',bg="#B00857",cursor='hand2',command=self.login).place(x=250,y=380,width=150,height=40)
        
        #################CLOCK==========================
        
        self.lbl=Label(self.root,text="\nClock",font=("Book Antiqua",25,"bold"),compound=BOTTOM,fg="white",bg="#081923",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        #self.clock_image()
        self.working()
            
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #####=========For clock Image
        
        
        bg=Image.open("C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\c.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        #clock.save("clock_new.png")            
        #########====For Line Hour
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #minute
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="black",width=3)
        ########seconds
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\clock_new.png")            

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        #print(h,m,s)
        #print(hr,min_,sec_)
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def register(self):
        self.root.destroy()
        os.system("python register.py")
    def login(self):
        if self.txt_email.get()=="" or self.txt_pwd.get()=="":
            messagebox.showerror("Warning","All Fields Are Required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                #con=sqlite3.connect(database="student.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_pwd.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username Or Password",parent=self.root)
                else:
                    messagebox.showeinfo("Success",f"Welcome: {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python main.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pwd.delete(0,END)
        self.txt_email.delete(0,END)
    def forget_password(self):
        if self.cmb_quest.get()=="" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                #con=sqlite3.connect(database="student.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and answer=%s",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showinfo("Warning","Please Enter The Valid Security Question Or Answer ",parent=self.root2)
                else:
                    cur.execute("update employee set password=%s where email=%s",(self.txt_new_pass.get(),self.txt_email.get(),))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your Password Has Been Reset Please Login With New PassWord",parent=self.root2)
                    self.reset()
                    self.root2.destroy()
                    
            except Exception as es:
                messagebox.showerror("Warning",f"Error Due to:{str(es)}",parent=self.root)            

    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showinfo("Warning","Please Enter The E-mail Address To reset Your Password ",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                #con=sqlite3.connect(database="student.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showinfo("Warning","Please Enter The Valid E-mail Address To reset Your Password ",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x410+480+150")
                    self.root2.config(bg='black')
                    self.root2.focus_force()
                    self.root2.grab_set()
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg='black',fg='red').place(x=0,y=10,relwidth=1)
                    ###################forget Password
                    question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold",),bg='black',fg="gray").place(x=50,y=90)
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER,values=("Select","Your First Pet","Your Birth Place","Your Fest Friend Name"))
                    self.cmb_quest.place(x=50,y=120,width=250)
                    self.cmb_quest.current(0)
                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg='black',fg="gray").place(x=50,y=160)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgrey")
                    self.txt_answer.place(x=50,y=190,width=250)
                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg='black',fg="gray").place(x=50,y=220)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgrey")
                    self.txt_new_pass.place(x=50,y=250,width=250)
                    btn_reset=Button(self.root2,text="Reset Password",font=("times new roman",20,"bold"),bg='black',fg='green',cursor='hand2',command=self.forget_password).place(x=90,y=320,width=185,height=40)
                
            except Exception as es:
                messagebox.showerror("Warning",f"Error Due to:{str(es)}",parent=self.root)
            
        
                            
                
            
    
            
            
        
        
            
    
    def login(self):
        if self.txt_email.get()=="" or self.txt_pwd.get()=="":
            messagebox.showerror("Warning","All Fields Are Required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                #con=sqlite3.connect(database="student.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_pwd.get(),))
                # ? replace by %s in xamp
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showinfo("Error","Invalid Username Or Password",parent=self.root)
                    
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    os.system("python main.py")
                con.close()
            
            except Exception as es:
                messagebox.showerror("Warning",f"Error Due to:{str(es)}",parent=self.root)
    
    
if __name__=="__main__":
    root=Tk()
    obj=Login_window(root)
    root.mainloop()
