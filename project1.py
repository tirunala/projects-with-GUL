from tkinter import *
from tkinter import messagebox
from datetime import *
import calendar
window=Tk()
window.geometry("800x500")
window['bg']="cyan"
window.title("syam")
name=StringVar()
entry_dob=StringVar()
def calculate_age():
    gname=name.get()
    try:
        birth_date = datetime.strptime(entry_dob.get(), '%Y-%m-%d')
        today = datetime.today()
        
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day
        wday = calendar.day_name[calendar.weekday(birth_date.year,birth_date.month,birth_date.day)].upper()


        if days < 0:
            months -= 1
            last_month = (today.month - 1) if today.month > 1 else 12
            days_in_last_month = (today.replace(month=last_month, day=1) - timedelta(days=1)).day
            days += days_in_last_month

            if months < 0:
                years -= 1
                months += 12
    
        messagebox.showinfo("Age Calculator", f"Your age is {years} year's, {months} month's, {days} day's are old, you born on '{wday}'.")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format.")

L1=Label(window,bg="cyan",text="Enter your Name: ")
L1.place(x=10,y=100)
E1=Entry(window,bd=3,bg="cyan",textvariable=name)
E1.place(x=320,y=100)
L2=Label(window,bg="cyan",text="Enter your Date Of Birth (yyyy-mm-dd): ")
L2.place(x=10,y=150)
E2=Entry(window,bd=4,bg="cyan",textvariable=entry_dob)
E2.place(x=320,y=150)
B1=Button(window,text="getAge",bg="cyan",command=calculate_age)
B1.place(x=300,y=250)


window.mainloop()
