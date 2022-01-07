from tkinter import*
from PIL import ImageDraw,ImageTk,Image
import tkinter
class Exam:
    def __init__(self,root):
        var=IntVar()
        self.root=root
        self.root.geometry("1530x795+0+0")
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        self.root.config()

        self.logo_dash=ImageTk.PhotoImage(file="C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\Optimized-python.png")
        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        right_lbl=Label(self.root,bg="#031F3C",image=self.logo_dash).place(x=0,y=0,relwidth=1,height=90)
        title=Label(self.root,text='Python',image=self.logo_dash,padx=10,compound=LEFT,font=("goudy old style",20,'bold')).place(x=0,y=0,relwidth=1,height=90)



        f_name=Label(self.root,text="Full Name-",font=("times new roman",20,"bold"),fg='black',bg='#08A3D2').place(x=140,y=150)
        f_name_txt=Entry(self.root,font=("times new roman",20,"bold"),fg='black',bg='white').place(x=300,y=150)
        roll=Label(self.root,text="Roll No-",font=("times new roman",20,"bold"),fg='black',bg='#031F3C').place(x=650,y=150)
        roll_txt=Entry(self.root,font=("times new roman",20,"bold"),fg='black',bg='White').place(x=790,y=150)
        q1=Label(self.root,text="Q1. Who invented Python-",font=("times new roman",20,"bold"),fg='green',bg='#08A3D2').place(x=0,y=220)
        r=Radiobutton(self.root,text="Guido Van Rossum",variable=var,font=("times new roman",15,"bold"),value=1,).place(x=330,y=230,height=40,width=400)
        root.pack(anchor=W)
        r1=Radiobutton(self.root,text="Guido Van Rossum",variable=var,font=("times new roman",15,"bold"),value=2,).place(x=620,y=230,height=40,width=400)
        root.pack(anchor=W)
        r2=Radiobutton(self.root,text="Guido Van Rossum",variable=var,font=("times new roman",15,"bold"),value=3,).place(x=910,y=230,height=40,width=400)
        root.pack(anchor=W)
        root=Label(root)
        root.pack()
        
        

        
root=Tk()
obj=Exam(root)
root.mainloop()