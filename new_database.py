import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as db

x = Tk()
x.geometry("500x500")
#bg = PhotoImage(file="b1.png")
l1 = Label(x)
l1.place(x=0, y=0, relwidth=1, relheight=1)
x.title('Registration form')

l1 = Label(x, text="Registration form", width=36, font=("bold", 10))
l1.place(x=80, y=60)

l2 = Label(x, text="Full Name:", width=15, font=("bold", 10))
l2.place(x=80, y=130)
t1 = Entry(x, width=22)
t1.place(x=240, y=130)

l3 = Label(x, text="Email:", width=15, font=("bold", 10))
l3.place(x=80, y=180)
t2 = Entry(x, width=22)
t2.place(x=240, y=180)

l4 = Label(x, text="Gender:", width=15, font=("bold", 10))
l4.place(x=80, y=230)

rb = StringVar()
Radiobutton(x, text="Male", padx=2, variable=rb, value="Male", font=("bold", 10)).place(x=240, y=230)
Radiobutton(x, text="Female", padx=2, variable=rb, value="Female", font=("bold", 10)).place(x=300, y=230)

l5 = Label(x, text="Country", width=15, font=("bold", 10))
l5.place(x=80, y=280)
country = ['India', 'US', 'UK', 'Germany', 'Austria']

c = StringVar()
droplist = OptionMenu(x, c, *country)
droplist.config(width=15)
c.set('Select Country')
droplist.place(x=240, y=280)

l6 = Label(x, text="Language", width=15, font=('bold', 10))
l6.place(x=80, y=330)
l7 = Label(x, font=("bold", 10), width=50)
l7.place(x=70, y=370)

cb1 = StringVar()
cb1.set('')
Checkbutton(x, text="English", variable=cb1, onvalue="English", offvalue="").place(x=240, y=330)
cb2 = StringVar()
cb2.set('')
Checkbutton(x, text="Hindi", variable=cb2, onvalue="Hindi", offvalue="").place(x=320, y=330)


def Insert():
    fullname = t1.get()
    email = t2.get()
    gender = rb.get()
    country = c.get()
    lang1 = cb1.get()
    lang2 = cb2.get()
    language = lang1 + lang2

    if (fullname == "" or email == "" or gender == "" or country == "" or language == ""):
        messagebox.showinfo("ALERT", "Please enter all fields")
    else:
        con = db.connect(host="localhost", user="root", password="", database="bitdb")
        cursor = con.cursor()
        cursor.execute(
            "insert into register values('" + fullname + "', '" + email + "', '" + gender + "','" + country + "','" + language + "')")
        cursor.execute("commit")

        messagebox.showinfo("Status", "Successfully Inserted")
        con.close();


Button(x, text='Insert', width=12, bg="black", fg='white', command=Insert).place(x=110, y=400)
Button(x, text='Select', width=12, bg="black", fg='white').place(x=190, y=400)
Button(x, text='Update', width=12, bg="black", fg='white').place(x=260, y=400)
Button(x, text='Delete', width=12, bg="black", fg='white').place(x=330, y=400)

x.mainloop()