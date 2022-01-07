import os
import math
import random
import smtplib
from tkinter import *
from tkinter import messagebox
import smtplib
import random
from next import Qr_generator
class Mail:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System Created By Tushar")
        self.var_email=StringVar()
        self.var_otp=int()
        self.root.geometry("1300x480+95+185")
        self.root.config(bg="white")
        self.root.focus_force()
        title=Label(self.root,text="Registeration",font=("goudy old style",20,'bold'),bg="#033054",fg="white",).place(x=10,y=15,width=1280,height=35)
        email_label = Label(self.root, text="Enter receiver's Email: ", font=("ariel 15 bold"), relief=FLAT)
        email_label.place(x=400,y=150)
        #email_label.grid(row=0, column=0, padx=15, pady=60)
        self.email_entry = Entry(self.root, font=("ariel 15 bold"),textvariable=self.var_email, width=25, relief=GROOVE, bd=2)
        self.email_entry.place(x=650,y=150)
        otp_label = Label(self.root, text="Enter receiver's Email: ", font=("ariel 15 bold"), relief=FLAT)
        otp_label.place(x=400,y=220)
        #email_label.grid(row=0, column=0, padx=15, pady=60)
        self.txt_otp = Entry(self.root, font=("ariel 15 bold"),textvariable=self.var_otp, width=25, relief=GROOVE, bd=2)
        self.txt_otp.place(x=650,y=220)
        #self.email_entry.grid(row=0, column=1, padx=12, pady=60)
        self.email_entry.focus()

        self.send_button = Button(self.root, text="Send Email", font=("ariel 15 bold"), bg="black", fg="green2", bd=3,command=self.send)
        self.send_button.place(x=500, y=280,width=150)
        self.clear_button = Button(self.root, text="Clear", font=("ariel 15 bold"), bg="black", fg="green2", bd=3,command=self.clear)
        self.clear_button.place(x=700, y=280,width=150)
        self.verify_button = Button(self.root, text="Verify", font=("ariel 15 bold"), bg="black", fg="green2", bd=3,)
        self.verify_button.place(x=975, y=150,width=150,height=30)
        self.step_button = Button(self.root, text="Next", font=("ariel 15 bold"), bg="black", fg="green2", bd=3,command=self.add_step)
        self.step_button.place(x=600, y=350,width=150)
        
    def send(self):
        try: 
            s = smtplib.SMTP("smtp.gmail.com" , 587)  # 587 is a port number 
            s.starttls()
            s.login("random08092001@gmail.com" , 'Tushar08@')
            register = random.randint(100000, 999999)
            register = str(register)
            s.sendmail("random08092001@gmail.com" , self.email_entry.get() , register)
            messagebox.showinfo("Send Registeration Id via Email", f"Registeration Id sent to {self.email_entry.get()}")
            s.quit()
        except:
            messagebox.showinfo("Send Registeration Idation Id via Email", "Please enter the valid email address OR check an internet connection")
    
    def clear(self):
        self.var_email.set("")
    
    def add_step(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Qr_generator(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj=Mail(root)
    root.mainloop()
        
