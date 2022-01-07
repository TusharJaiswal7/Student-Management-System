from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time 
from math import*
class watch:
    def __init__(self,root):
        self.root=root
        self.root.title("Analog Clock")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#021e2f")
        tilte=Label(self.root,text="GUI ANALOG CLOCK",font=("times new roman",50,"bold"),fg="white",bg="#04444a").place(x=0,y=50,relwidth=1)
        self.lbl=Label(self.root,bg="white")
        self.lbl.place(x=450,y=150,height=400,width=400)
        #self.clock_image()
        self.working()
    
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)
        #####=========For clock Image
        
        
        bg=Image.open("C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\cl.jpg")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        #clock.save("clock_new.png")            
        #########====For Line Hour
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
        #minute
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)
        ########seconds
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="green",width=4)
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("clock_new.png")            

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
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
root=Tk()
obj=watch(root)
root.mainloop()