from tkinter import*
import os
from PIL import Image,ImageTk,ImageDraw

class Exam:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x795+0+0")
        
        #self.root.config(bg='#08A3D2')
        self.var_option1=StringVar()
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        # self.logo_dash=Image.open("C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\python.png")
        # self.logo_dash=self.logo_dash.resize((50,100),Image.ANTIALIAS)bg="#033054"
        self.logo_dash=ImageTk.PhotoImage(file="C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\Optimized-python.png")
        
        # ##title###
        title=Label(self.root,text="Student Management System",image=self.logo_dash,compound=LEFT,font=("goudy old style",20,'bold'),bg="#08A3D2",fg="white",).place(x=0,y=0,relwidth=1,height=90)
        #title=Label(self.root,text="Python",font=("times new roman",50,"bold"),fg='red',bg='lightblue').place(x=420,y=10)
        f_name=Label(self.root,text="Full Name-",font=("times new roman",20,"bold"),fg='red').place(x=0,y=150)
        f_name_txt=Entry(self.root,font=("times new roman",20,"bold"),fg='black').place(x=150,y=150)
        roll=Label(self.root,text="Roll No-",font=("times new roman",20,"bold"),fg='red').place(x=600,y=150)
        roll_txt=Entry(self.root,font=("times new roman",20,"bold"),fg='black').place(x=720,y=150)
        q1=Label(self.root,text="Q1. Who invented Python-",font=("times new roman",20,"bold"),fg='green').place(x=0,y=220)
        option=Radiobutton(self.root,text="Guido Van Rossum",font=("times new roman",15,"bold"),value=0,bg='lightblue').place(x=300,y=220,height=20,width=400)
        option=Radiobutton(self.root,text="Guido Van Rossum",font=("times new roman",15,"bold"),value=0,bg='lightblue').place(x=590,y=220,height=20,width=400)
        option=Radiobutton(self.root,text="Guido Van Rossum",font=("times new roman",15,"bold"),value=0,bg='lightblue').place(x=880,y=220,height=20,width=400)
        #option.pack(anchor=W)
        q1=Label(self.root,text="Q2. Which of these is not a python datatype",font=("times new roman",20,"bold"),fg='green').place(x=0,y=270)
        
root=Tk()
obj=Exam(root)
root.mainloop()