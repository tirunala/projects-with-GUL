from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("800x500")
window.title("Body Mass Index")
title="Body Mass Index"
w=StringVar()
h1=StringVar()
h2=StringVar()

def bmi():
    #1foot=0.3048(meters)
    #1inch=0.0254(meters)
    height1=float(h1.get())
    height2=float(h2.get())
    weight=float(w.get())
    height=height1*0.3048+height2*0.0254
    bmi=weight/height**2
    if bmi<18.5:
        res=f"Under weight"
        messagebox.showinfo(title="bmi",message=res)
    elif bmi>=18.5 and bmi<25:
        res=f"Normal weight"
        messagebox.showinfo(title="bmi",message=res)
    elif bmi>=25 and bmi<=29.9:
        res=f"Over weight"
        messagebox.showinfo(title="bmi",message=res)
    else:
        res=f"Obesity"
        messagebox.showinfo(title="bmi",message=res)
L1=Label(window,text="Enter you Weight:")
L1.place(x=150,y=50)
E1=Entry(window,bd=3,textvariable=w)
E1.place(x=320,y=50)
L2=Label(window,text="Enter you Height in Foots:")
L2.place(x=150,y=100)
E2=Entry(window,bd=3,textvariable=h1)
E2.place(x=320,y=100)
L3=Label(window,text="Enter you Height in Inches:")
L3.place(x=150,y=150)
E3=Entry(window,bd=3,textvariable=h2)
E3.place(x=320,y=150)
B1=Button(window,text="BMI",bg="pink",command=bmi)
B1.place(x=320,y=250)

window.mainloop()

