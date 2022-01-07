#module importing 
from datetime import*
import time
from math import *
from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from courses import CourseClass
from student import studentClass
from exam import Exam
from result import resultClass
from tkinter import messagebox
import os
import sqlite3
from report import Report 
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System Created By Tushar")
        self.root.geometry("1530x795+0+0")
        #self.root.config(bg="black")
        self.root.config(bg="#021e2f")
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        ##========icons======##
        self.logo_dash=ImageTk.PhotoImage(file="C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\logo_p.png")
        ##title###
        title=Label(self.root,text="Student Management System",image=self.logo_dash,padx=10,compound=LEFT,font=("goudy old style",20,'bold'),bg="#033054",fg="white",).place(x=0,y=0,relwidth=1,height=50)
        #====###Menu
        M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1510,height=80)

        btn_course=Button(M_Frame,text="Course",font=("gloudy old style",15,"bold"),bg="#08A3D2",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=190,height=40)
        btn_=Button(M_Frame,text="Student",font=("gloudy old style",15,"bold"),bg="#08A3D2",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=190,height=40)
        btn_exam=Button(M_Frame,text="Exam",font=("gloudy old style",15,"bold"),bg="#08A3D2",fg="white",cursor="hand2",command=self.exam).place(x=460,y=5,width=190,height=40)
        btn_result=Button(M_Frame,text="Add Result's",font=("gloudy old style",15,"bold"),bg="#08A3D2",fg="white",cursor="hand2",command=self.add_result).place(x=680,y=5,width=190,height=40)
        btn_view=Button(M_Frame,text=" View Result's",font=("gloudy old style",15,"bold"),bg="#08A3D2",fg="white",cursor="hand2",command=self.check_result).place(x=900,y=5,width=190,height=40)
        btn_logout=Button(M_Frame,text="Log Out",font=("gloudy old style",15,"bold"),bg="#08A3D2",fg="white",cursor="hand2",command=self.logout).place(x=1120,y=5,width=190,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("gloudy old style",15,"bold"),bg="#08A3D2",fg="white",cursor="hand2",command=self.exit_).place(x=1340,y=5,width=155,height=40)
        ##########
        

        #################CLOCK==========================
        
        self.lbl=Label(self.root,text="\nClock",font=("Book Antiqua",25,"bold"),compound=BOTTOM,fg="white",bg="#081923",bd=0)
        self.lbl.place(x=218,y=180,height=449,width=380)
        #self.clock_image()
        self.working()
        #========Footer
        footer=Label(self.root,text="Software Is based On database",font=("Times new roman",14),bg="#262626",fg="White").pack(side=BOTTOM,fill=X)
        
        #Content Window Image Part
        self.bg_img=Image.open("C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=600,y=180,width=920,height=350)
        #==Update Label/details
        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="red",fg="white")
        self.lbl_course.place(x=600,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total Student\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="blue",fg="white")
        self.lbl_student.place(x=910,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Result's\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="green",fg="white")
        self.lbl_result.place(x=1220,y=530,width=300,height=100)
        self.update_details()
    def update_details(self):
        con=sqlite3.connect(database="student.db")
        cur=con.cursor()       
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            
            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            #self.lbl_student.after(200,self.update_details)
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
            #self.lbl_result.after(200,self.update_details)

            self.lbl_course.after(200,self.update_details)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}")
           
        
    ##########=========NEw Window POP UP Course Part
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    
    def add_student(self):
        self.new_win.destroy()
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)
    def exam(self):
        self.new_win.destroy()
        self.new_win=Toplevel(self.root)
        self.new_obj=Exam(self.new_win)
    
    def add_result(self):
        self.new_win.destroy()
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    
    def check_result(self):
        self.new_win.destroy()
        self.new_win=Toplevel(self.root)
        self.new_obj=Report(self.new_win)
    def logout(self):
        op=messagebox.askyesno("Confirm","Are you Sure You Want To LogOut!!",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
    
    def exit_(self):
        op=messagebox.askyesno("Confirm","Are you Sure You Want To Exit!!",parent=self.root)
        if op==True:
            self.root.destroy()
    
    
    
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


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()