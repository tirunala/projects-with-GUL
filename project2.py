from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("800x500")
window['bg']="cyan"
window.title("syam")
fn=StringVar()
sn=StringVar()

def add():
    a=fn.get()
    b=sn.get()
    x=int(a)
    y=int(b)
    z=x+y
    res=f"sum of {x} and {y} is {z}"
    messagebox.showinfo(title="ADD",message=res)
def sub():
    a=fn.get()
    b=sn.get()
    x=int(a)
    y=int(b)
    z=x-y
    res=f"sub of {x} and {y} is {z}"
    messagebox.showinfo(title="SUB",message=res)
def mul():
    a=fn.get()
    b=sn.get()
    x=int(a)
    y=int(b)
    z=x*y
    res=f"mul of {x} and {y} is {z}"
    messagebox.showinfo(title="MUL",message=res)
def div():
    a=fn.get()
    b=sn.get()
    x=int(a)
    y=int(b)
    if y==0:
        error=f"invalid second number {y}"
        messagebox.showerror(title="Error",message=error)
    else:
        z=x/y
        res=f"division of {x} and {y} is {z}"
        messagebox.showinfo(title="DIV",message=res)
def fdiv():
    a=fn.get()
    b=sn.get()
    x=int(a)
    y=int(b)
    if y==0:
        error=f"invalid second number {y}"
        messagebox.showerror(title="Error",message=error)
    else:
        z=x//y
        res=f"Fdiv of {x} and {y} is {z}"
        messagebox.showinfo(title="FDIV",message=res)
def mod():
    a=fn.get()
    b=sn.get()
    x=int(a)
    y=int(b)
    if y==0:
        error=f"invalid second number {y}"
        messagebox.showerror(title="Error",message=error)
    else:
        z=x%y
        res=f"mod of {x} and {y} is {z}"
        messagebox.showinfo(title="MOD",message=res)
def reset():
    fn.set('')
    sn.set('')
def close():
    window.destroy() 

L1=Label(window,bg="cyan",text="Enter your First Number: ")
L1.place(x=10,y=100)
E1=Entry(window,bd=3,bg="cyan",textvariable=fn)
E1.place(x=320,y=100)
L2=Label(window,bg="cyan",text="Enter your Second Number: ")
L2.place(x=10,y=150)
E2=Entry(window,bd=4,bg="cyan",textvariable=sn)
E2.place(x=320,y=150)
B1=Button(window,text="ADD",bg="cyan",command=add)
B1.place(x=50,y=250)
B2=Button(window,text="SUB",bg="cyan",command=sub)
B2.place(x=100,y=250)
B3=Button(window,text="MUL",bg="cyan",command=mul)
B3.place(x=150,y=250)
B4=Button(window,text="DIV",bg="cyan",command=div)
B4.place(x=200,y=250)
B5=Button(window,text="FDIV",bg="cyan",command=fdiv)
B5.place(x=50,y=350)
B6=Button(window,text="MOD",bg="cyan",command=mod)
B6.place(x=100,y=350)
B7=Button(window,text="Clear",bg="cyan",command=reset)
B7.place(x=150,y=350)
B8=Button(window,text="Close",bg="cyan",command=close)
B8.place(x=200,y=350)
window.mainloop()
