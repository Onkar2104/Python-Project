from tkinter import *
from tkinter import messagebox
import mysql.connector as db
from tkinter import ttk

S = Tk()
S.geometry('600x1000')
S.config(bg='orange')
S.title('Student Details')

l=Label(S,text='Student Information',width=15,font=('bold',15))
l.place(x=170,y=20)

l1=Label(S,text='ID',width=10,font=('bold',10))
l1.place(x=50,y=100)
t1=Entry(S,width=30)
t1.place(x=200,y=100)

l2=Label(S,text='Name',width=10,font=('bold',10))
l2.place(x=50,y=150)
t2=Entry(S,width=30)
t2.place(x=200,y=150)

l3=Label(S,text='Branch',width=10,font=('bold',10))
l3.place(x=50,y=200)
Branch=['A','B','C','D','X',"Y",'S',"F"]
B=StringVar()
droplist=OptionMenu(S,B,*Branch)
droplist.config(width=10)
B.set('Branch')
droplist.place(x=200,y=200)

l4=Label(S,text='Roll No',width=10,font=('bold',10))
l4.place(x=50,y=250)
t4=Entry(S,width=30)
t4.place(x=200,y=250)

l5=Label(S,text='Section',width=10,font=('bold',10))
l5.place(x=50,y=300)
Section=[1,3,45,12,23,17,14]
s=StringVar()
droplist=OptionMenu(S,s,*Section)
s.set('Section')
droplist.config(width=10)
droplist.place(x=200,y=300)

l0=Label(S,text='Marks',width=15,font=('bold',15))
l0.place(x=170,y=350)

l6=Label(S,text='sub1',width=5,font=('bold',10))
l6.place(x=50,y=400)
t6=Entry(S,width=7)
t6.place(x=50,y=450)

l7=Label(S,text='sub2',width=10,font=('bold',10))
l7.place(x=100,y=400)
t7=Entry(S,width=7)
t7.place(x=120,y=450)

l8=Label(S,text='sub3',width=10,font=('bold',10))
l8.place(x=200,y=400)
t8=Entry(S,width=7)
t8.place(x=200,y=450)

l9=Label(S,text='sub4',width=10,font=('bold',10))
l9.place(x=300,y=400)
t9=Entry(S,width=7)
t9.place(x=300,y=450)

l11=Label(S,text='sub5',width=10,font=('bold',10))
l11.place(x=400,y=400)
t11=Entry(S,width=7)
t11.place(x=400,y=450)

l12=Label(S,text='sub6',width=10,font=('bold',10))
l12.place(x=500,y=400)
t12=Entry(S,width=7)
t12.place(x=500,y=450)

l13=Label(S,text='Total Marks',width=10,font=('bold',10))
l13.place(x=100,y=500)
t13=Entry(S,width=10)
t13.place(x=100,y=550)

l14=Label(S,text='Percentage',width=10,font=('bold',10))
l14.place(x=400,y=500)
t14=Entry(S,width=10)
t14.place(x=400,y=550)

def Insert():
    id = t1.get()
    name = t2.get()
    branch = B.get()
    rollno = t4.get()
    section = s.get()
    s1 = int(t6.get())
    s2 = int(t7.get())
    s3 = int(t8.get())
    s4 = int(t9.get())
    s5 = int(t11.get())
    s6 = int(t12.get())
    tot = s1 + s2 + s3 + s4 + s5 + s6
    per = tot / 6
    t13.insert(END, str(tot))
    t14.insert(END, str(per))

    if (
            id == "" or name == '' or branch == '' or rollno == '' or section == '' or s1 == '' or s2 == '' or s3 == '' or s4 == '' or s5 == '' or s6 == '' or tot == '' or per == ''):
        messagebox.showinfo("Insert Status", "All Fields are Required")
    else:
        con = db.connect(host='localhost', user='root', password='', database='python_db')
        c = con.cursor()
        c.execute("Insert into studentinfo values('"+id+"','"+name+"','"+branch+"','"+rollno+"','"+section+"','"+str(s1)+"','"+str(s2)+"','"+str(s3)+
                  "','"+str(s4)+"','"+str(s5)+"','"+str(s6)+"','"+str(tot)+"','"+str(per)+"')")
        con.commit()
        t1.delete(0, 'end')
        t2.delete(0, 'end')
        B.delete(0, 'end')
        t4.delete(0, 'end')
        s.delete(0, 'end')
        t6.delete(0, 'end')
        t7.delete(0, 'end')
        t8.delete(0, 'end')
        t9.delete(0, 'end')
        t11.delete(0, 'end')
        t12.delete(0, 'end')
        t13.delete(0, 'end')
        t14.delete(0, 'end')

        messagebox.showinfo("Information","Inserted Data!!!")
        con.close()
        show()
#------------------------------------------------
def select():
    if(t1.get()==""):
        messagebox.showinfo("Fetch Status","ID is required")
    else:
        con=db.connect(host='localhost',user='root',password='',database='python_db')
        c=con.cursor()
        c.execute("select * from studentinfo where id='"+t1.get()+"'")
        res=c.fetchall()
        for row in res:
            t2.insert(END, row[1])
            B.set(str(Branch[2]))
            t4.insert(END, row[3])
            s.set(str(Section[4]))
            t6.insert(END, row[5])
            t7.insert(END, row[6])
            t8.insert(END, row[7])
            t9.insert(END, row[8])
            t11.insert(END, row[9])
            t12.insert(END, row[10])
            t13.insert(END, row[11])
            t14.insert(END, row[12])
        con.close()

#----------------------------------------------------
def update():
    Id=t1.get()
    Name=t2.get()
    Branch=B.get()
    RollNo=t4.get()
    Section=s.get()
    S1=t6.get()
    S2=t7.get()
    S3=t8.get()
    S4=t9.get()
    S5=t11.get()
    S6=t12.get()
    Totalmarks=t13.get()
    Percentage=t14.get()


    if(Id==""or Name==''or Branch==''or RollNo==''or Section==''or S1==''or S2==''or S3==''or S4==''or S5==''or S6==''or Totalmarks==''or Percentage==''):
        messagebox.showinfo("Update Status","All Fields are Required")
    else:
        con=db.connect(host='localhost',user='root',password='',database='python_db')
        c=con.cursor()
        c.execute("update studentinfo set Name='"+Name+"',Branch='"+Branch+"',RollNo='"+RollNo+"',Section='"+Section+"',s1='"+S1+"',s2='"+S2+"',s3='"+S3+"',s4='"+S4+"',s5='"+S5+"',s6='"+S6+"',totmarks='"+Totalmarks+"',percent='"+Percentage+"' where id='"+Id+"'")
        con.commit()
        t1.delete(0, 'end')
        t2.delete(0, 'end')
        B.set(' ')
        t4.delete(0, 'end')
        s.set(' ')
        t6.delete(0, 'end')
        t7.delete(0, 'end')
        t8.delete(0, 'end')
        t9.delete(0, 'end')
        t11.delete(0, 'end')
        t12.delete(0, 'end')
        t13.delete(0, 'end')
        t14.delete(0, 'end')
        show()
        con.close()
        messagebox.showinfo("Information","Updated DATA!!!")

#=====================================================

def Delete():
    if(t1.get()==""):
        messagebox.showinfo("Delete Status","Id Is Required")
    else:
        con = db.connect(host='localhost', user='root', password='', database='python_db')
        c=con.cursor()
        c.execute("delete from studentinfo where id='"+t1.get()+"'")
        con.commit()
        t1.delete(0, 'end')
        t2.delete(0, 'end')
        B.set(' ')
        t4.delete(0, 'end')
        s.set(' ')
        t6.delete(0, 'end')
        t7.delete(0, 'end')
        t8.delete(0, 'end')
        t9.delete(0, 'end')
        t11.delete(0, 'end')
        t12.delete(0, 'end')
        t13.delete(0, 'end')
        t14.delete(0, 'end')
        show()
        messagebox.showinfo("Information", "Deleted Data!!!")
        con.close()

#=============================================================

def show():
    con=db.connect(host='localhost',user='root',password='',database='python_db')
    c=con.cursor()
    c.execute("select * from studentinfo")
    res=c.fetchall()
    list.delete(0,list.size())
    for row in res:
        insertData=str(row[0])+' '+str(row[1])+' '+str(row[2])+' '+str(row[3])+' '+str(row[3])+' '+str(row[5])+' '+str(
            row[6])+' '+str(row[7])+' '+str(row[8])+' '+str(row[9])+' '+str(row[10])+' '+str(row[11])+' '+str(row[12])
        list.insert(list.size()+1,insertData)
    con.close()

#----------------------------------------------------------------------

Button(S,text="Insert",width=10,bg="black",fg="white",command=Insert).place(x=100,y=600)
Button(S,text="Update",width=10,bg="black",fg="white",command=update).place(x=220,y=600)
Button(S,text="Select",width=10,bg="black",fg="white",command=select).place(x=340,y=600)
Button(S,text="Delete",width=10,bg="black",fg="white",command=Delete).place(x=480,y=600)

list=Listbox(S,width=50)
list.place(x=100,y=650)
show()

S.mainloop()