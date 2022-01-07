from tkinter import *
import tkinter


app = Tk()
app.overrideredirect(True)
app.wm_attributes("-topmost", True)
app.wm_attributes("-transparent", True)
app.config(bg='systemTransparent')

app.geometry("+300+300")

app.image = PhotoImage(file="C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\student management system\\images\\Optimized-python.png")
label = Label(app, image=app.image)
label.config(bg='systemTransparent')

label.pack()
app.mainloop()