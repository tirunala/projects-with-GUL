from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("400x500")
window['bg']="cyan"
window.title("Number System")

x=IntVar()
def binary():
    num=bin(x.get())
    res=f"Binary Number {num}"
    messagebox.showinfo("Bin",message=res)

def dec():
    num=x.get()
    res=f"Decimal Number {num}"
    messagebox.showinfo(title="ADD",message=res)

def octal():
    num=oct(x.get())
    res=f"Octal Number {num}"
    messagebox.showinfo(title="ADD",message=res)

def hexa():
    num=hex(x.get())
    res=f"hexa Number {num}"
    messagebox.showinfo(title="HEX",message=res)
    
def reset():
    x.set(' ')

def close():
    window.destroy()    

    
L1=Label(window,bg="cyan",text="Enter your Number: ")
L1.place(x=10,y=150)
E1=Entry(window,bd=4,bg="cyan",textvariable=x)
E1.place(x=150,y=150)
B1=Button(window,text="Binary",bg="cyan",command=binary)
B1.place(x=50,y=250)
B2=Button(window,text="Decimal",bg="cyan",command=dec)
B2.place(x=150,y=250)
B3=Button(window,text="Octal",bg="cyan",command=octal)
B3.place(x=250,y=250)
B4=Button(window,text="Hexadecimal",bg="cyan",command=hexa)
B4.place(x=50,y=300)
B5=Button(window,text="Clear",bg="cyan",command=reset)
B5.place(x=150,y=300)
B6=Button(window,text="close",bg="cyan",command=close)
B6.place(x=250,y=300)

window.mainloop()
