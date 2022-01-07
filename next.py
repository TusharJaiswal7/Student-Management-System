from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x480+95+185")
        #("1200x480+80+170")
        self.root.title("                                                                                                       Qr Generator | Developed By Tushar")
        self.root.resizable(False,False)
        self.root.focus_force()
        self.root.config(bg='black')
        title=Label(self.root,text="  Qr Code Generator",font=("goudy old style",40,'bold'),bg="black",fg="white",).place(x=0,y=0,relwidth=1)

        ##student details part
        ###Variable to fetch data
        self.var_stu_code=StringVar()
        self.var_class=StringVar()
        self.var_stream=StringVar()
        self.var_rollno=StringVar()


        stu_Frame=Frame(self.root,bd=2,relief=RIDGE ,bg='lightblue')
        stu_Frame.place(x=150,y=100,width=500,height=360)


        stu_title=Label(stu_Frame,text="Student Details",font=("goudy old style",20),bg="#043256",fg="white").place(x=0,y=0,relwidth=1)
        
        lbl_stu_code=Label(stu_Frame,text="Student ID",font=("Times New Roman",15,'bold'),bg="white").place(x=50,y=60)
        lbl_class=Label(stu_Frame,text="Class",font=("Times New Roman",15,'bold'),bg="white").place(x=50,y=100)
        lbl_stream=Label(stu_Frame,text="Stream",font=("Times New Roman",15,'bold'),bg="white").place(x=50,y=140)
        lbl_rollno=Label(stu_Frame,text="Roll No",font=("Times New Roman",15,'bold'),bg="white").place(x=50,y=180)

                
        txt_stu_code=Entry(stu_Frame,font=("Times New Roman",15,),textvariable=self.var_stu_code,bg="lightyellow").place(x=200,y=60)
        txt_class=Entry(stu_Frame,font=("Times New Roman",15),textvariable=self.var_class,bg="lightyellow").place(x=200,y=100)
        txt_stream=Entry(stu_Frame,font=("Times New Roman",15),textvariable=self.var_stream,bg="lightyellow").place(x=200,y=140)
        txt_rollno=Entry(stu_Frame,font=("Times New Roman",15),textvariable=self.var_rollno,bg="lightyellow").place(x=200,y=180)

        btn_generator=Button(stu_Frame,text="Make QR",command=self.generate,font=("times new roman",18,'bold'),bg='green',fg='white').place(x=50,y=250,width=180,height=30)
        clr_generator=Button(stu_Frame,text="Clear",command=self.clear,font=("times new roman",18,'bold'),bg='green',fg='white').place(x=283,y=250,width=120,height=30)

        self.msg=""
        self.lbl_msg=Label(stu_Frame,text=self.msg,font=("times new roman",20,),bg='lightblue',fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1)

        ##student QR FRAME  part

        qr_Frame=Frame(self.root,bd=2,relief=RIDGE ,bg='lightblue')
        qr_Frame.place(x=900,y=100,width=250,height=360)


        stu_title=Label(qr_Frame,text="Student QR Code",font=("goudy old style",20),bg="#043256",fg="white").place(x=0,y=0,relwidth=1)
        
        self.qr_code=Label(qr_Frame,text="Qr Code \nNot available",font=('times new roman',15),bg="black",fg="white",bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):    
        self.var_stu_code.set("")
        self.var_class.set("")
        self.var_stream.set("")
        self.var_rollno.set("")
        self.msg=""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')
        

    def generate(self):
        if  self.var_stu_code.get()=='' or self.var_class.get()=='' or self.var_stream.get()==''or self.var_rollno.get()=='':
            self.msg="All Fields are necessary!!"
            self.lbl_msg.config(text=self.msg,fg="red",bg='lightblue')
        else:
            qr_data=(f"Student Id :{self.var_stu_code.get()}\n Student Class:{self.var_class.get()}\n Student Stream:{self.var_stream.get()}\n Student Roll No:{self.var_rollno.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\Stu_"+str(self.var_stu_code.get())+'.png')
            #=====qr code image update here
            self.im=ImageTk.PhotoImage(file="C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\Stu_"+str(self.var_stu_code.get())+'.png')
            self.qr_code.config(image=self.im)
            ##updating notification###############
            self.msg="QR created Successfully!!!"
            self.lbl_msg.config(text=self.msg,fg="green",bg='lightblue')

if __name__=="__main__":
    root=Tk()
    obj=Qr_generator(root)
    root.mainloop()
