from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from mail1 import Mail

#from next import Qr_generator
class Report:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System Created By Tushar")
        self.root.geometry("1300x480+95+185")
        #("1200x480+80+170")
        self.root.config(bg="black")
        self.root.focus_force()
        self.var_search=StringVar()
        self.var_id=""
        title=Label(self.root,text="Check Result's",font=("goudy old style",20,'bold'),bg="orange",fg="#262626",).place(x=10,y=15,width=1280,height=50)
        #######################SEARCH#########################
        lbl_select=Label(self.root,text="Search By Roll No:",font=("goudy old style",20,"bold"),bg="white").place(x=310,y=100)
        txt_select=Entry(self.root,font=("goudy old style",20,),textvariable=self.var_search,bg="lightgreen").place(x=540,y=100)
        self.btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=840,y=100,width=100,height=35)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.clear).place(x=950,y=100,width=100,height=35)

        ##################LABELS##########################
        lbl_roll=Label(self.root,text="Roll No",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=180,y=200,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=330,y=200,width=150,height=50)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=480,y=200,width=150,height=50)
        lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=630,y=200,width=150,height=50)
        lbl_total_marks=Label(self.root,text="Total Marks",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=780,y=200,width=150,height=50)
        lbl_per=Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=930,y=200,width=150,height=50)

        self.roll=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=180,y=250,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=330,y=250,width=150,height=50)
        self.course=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=480,y=250,width=150,height=50)
        self.marks_ob=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks_ob.place(x=630,y=250,width=150,height=50)
        self.total_marks=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.total_marks.place(x=780,y=250,width=150,height=50)
        self.per=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=930,y=250,width=150,height=50)
        
        ################Button DELETE################
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=600,y=350,width=120,height=35)

    def search(self):
        con=sqlite3.connect(database="student.db")
        cur=con.cursor()       
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Warning","Please Enter A Roll No To View Result",parent=self.root)
            else:
                cur.execute("select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks_ob.config(text=row[4])
                    self.total_marks.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}")

    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks_ob.config(text="")
        self.total_marks.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    def delete(self):
        con=sqlite3.connect(database="student.db")
        cur=con.cursor()       
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search Student Result First",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error", "Invalid Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=Report(root)
    root.mainloop()