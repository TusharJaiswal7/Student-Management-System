from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System Created By Tushar")
        self.root.geometry("1320x480+95+185")
        self.root.config(bg="black")
        self.root.focus_force()
        #==variables
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()
        self.var_rollno=StringVar()
        #title
        title=Label(self.root,text="Add Student Result's",font=("goudy old style",20,'bold'),bg="orange",fg="#262626",).place(x=10,y=15,width=1280,height=50)
        #############################========================Widgets========================
        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="black",fg="white",).place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="black",fg="white",).place(x=50,y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="black",fg="white",).place(x=50,y=220)
        lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="black",fg="white",).place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="black",fg="white",).place(x=50,y=340)

        #txt_select=Entry(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,text="Name",font=("goudy old style",20,"bold"),textvariable=self.var_name,bg="lightgreen",state='readonly').place(x=280,y=160,width=320)
        txt_course=Entry(self.root,text="Course",font=("goudy old style",20,"bold"),textvariable=self.var_course,bg="lightgreen",state='readonly').place(x=280,y=220,width=320)
        txt_marks_ob=Entry(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),textvariable=self.var_marks,bg="lightgreen").place(x=280,y=280,width=320)
        txt_full_marks=Entry(self.root,text="Full Marks",font=("goudy old style",20,"bold"),textvariable=self.var_full_marks,bg="lightgreen").place(x=280,y=340,width=320)


        self.txt_student=ttk.Combobox(self.root,font=("Times New Roman",10),textvariable=self.var_rollno,values=self.roll_list,state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=110,width=200,height=25)
        self.txt_student.set("Select")
        self.btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=500,y=110,width=100,height=28)

        #_________================Button
        btn_add=Button(self.root,text="Submit",font=('times new roman',15),bg='lightgray',activebackground="lightgray",cursor='hand2',command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=('times new roman',15),bg='yellow',activebackground="yellow",cursor='hand2',command=self.clear).place(x=430,y=420,width=120,height=35)
        #====================Image=========================
        self.bg_img=Image.open("C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\result.jpg")
        self.bg_img=self.bg_img.resize((500,300),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=750,y=110)
 #=====================================Functions=========================================================
    def fetch_roll(self):
        con=sqlite3.connect(database="student.db")
        cur=con.cursor()       
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
            
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="student.db")
        cur=con.cursor()       
        try:
            cur.execute("select name,course from student where roll=?",(self.var_rollno.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}")       

    def add(self):
        con=sqlite3.connect(database="student.db")
        cur=con.cursor()       
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please First search student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_rollno.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error", "Result  Already Present",parent=self.root)
                else:
                    per=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    cur.execute("insert into result (roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",(
                        self.var_rollno.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Sucessfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}")
    
    def clear(self):
        self.var_rollno.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set(""),
        






if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()