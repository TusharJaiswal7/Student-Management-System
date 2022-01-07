from tkinter import*
import os
class Exam:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x480+95+185")
        self.root.config(bg="white")
        title=Label(self.root,text="Exam are the key to Success",font=("times new roman",50,"bold"),bg='black',fg='red').place(x=320,y=10)
        python=Label(self.root,text="Python>>>",font=("times new roman",20,"bold"),fg='red').place(x=200,y=200)
        btn_python=Button(self.root,text="Click Me",font=("times new roman",15),bg='green',fg='black',command=self.python).place(x=400,y=200)
        java=Label(self.root,text="Java>>>",font=("times new roman",20,"bold"),fg='red').place(x=200,y=300)
        btn_java=Button(self.root,text="Click Me",font=("times new roman",15),bg='green',fg='black',command=self.java).place(x=400,y=300)
    def python(self):
        self.root.destroy()
        os.system("python exam1.py")
    
    def java(self):
        self.root.destroy()
        os.system("python exam2.py")
if __name__=="__main":
    root=Tk()
    obj=Exam(root)
    root.mainloop()