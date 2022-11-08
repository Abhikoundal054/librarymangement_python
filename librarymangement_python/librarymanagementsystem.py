
from tkinter import *
from tkinter import ttk, StringVar
from tkinter.ttk import Treeview
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime
root = Tk()
root.geometry("1500x800")
root.title("LIBRARY MANAGEMNET SYSTEM")

def adddata():
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="koundal",
        database="pythondb"
    )
    mycursor = conn.cursor()
    mycursor.execute("Insert into  librarymanage values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(namevalue.get(), idvalue.get(), adressvalue.get(),mobilevalue.get(),bookvalue.get(),book1value.get(),dateborrowvalue.get(),dateduevalue.get(),daysvalue.get(),latevalue.get()))
    conn.commit()
    fatchdata()
    conn.close()
    messagebox.showinfo("sucess","Member has been inserted sucessfully")




def fatchdata():
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="koundal",
        database="pythondb"
    )
    mycursor = conn.cursor()
    mycursor.execute("select * from librarymanage")
    rows=mycursor.fetchall()


    for x in rows:
        library_table.insert("",END,values=x)

    conn.commit()
    conn.close()

def showdata():
    textbox.insert(END,"Member \t\t"+namevalue.get()+"\n")
    textbox.insert(END, "Id \t\t" + idvalue.get() + "\n")
    textbox.insert(END, "Adress \t\t" + adressvalue.get() + "\n")
    textbox.insert(END, "Mobile number \t\t" + mobilevalue.get() + "\n")
    textbox.insert(END, "Book Id \t\t" + bookvalue.get() + "\n")
    textbox.insert(END, "Book Title \t\t" + book1value.get() + "\n")
    textbox.insert(END, "Date of Borrow \t\t" +dateborrowvalue.get() + "\n")
    textbox.insert(END, "date due \t\t" + dateduevalue.get() + "\n")
    textbox.insert(END, "days due \t\t" +  daysvalue.get() + "\n")
    textbox.insert(END, "late fess \t\t" + latevalue.get() + "\n")


def reset():
    namevalue.set(""),
    idvalue.set("")
    adressvalue.set(""),
    mobilevalue.set(""),
    bookvalue.set(""),
    book1value.set(""),
    dateborrowvalue.set(""),
    dateduevalue.set(""),
    daysvalue.set(""),
    latevalue.set("")
    textbox.delete("1.0",END)


def exit():
    exit=tkinter.messagebox.askyesno("Library Management System","Do you Want to exit")
    if exit>0:
        root.destroy()
    else:
        return

def update():
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="koundal",
        database="pythondb"
    )
    mycursor = conn.cursor()
    mycursor.execute("UPDATE librarymanage SET Name=%s ,Adress=%s,MobileNo=%s,BookID=%s,BookTitle=%s,DateBorrow=%s,DueDate=%s,DaysOnBook=%s,LateFine=%s WHERE IdNo=%s",(namevalue.get(), adressvalue.get(),mobilevalue.get(),bookvalue.get(),book1value.get(),dateborrowvalue.get(),dateduevalue.get(),daysvalue.get(),latevalue.get(), idvalue.get()))

    conn.commit()
    fatchdata()
    reset()
    conn.close()
    messagebox.showinfo("Sucess","Message has been Updated")


def delete():
    if idvalue.get()=="" or namevalue.get=="":
        messagebox.showerror("Error","First enter Member")
    else:
        conn = mysql.connector.connect(
            host = "localhost",username="root",password="koundal",database="librarymanage")
        mycursor = conn.cursor()
        querry="DELETE FROM librarymanage WHERE IdNo=%s"
        data= [(idvalue.get())]
        mycursor.execute(querry,data)

        conn.commit()
        fatchdata()
        reset()
        conn.close()
        messagebox.showinfo("Sucess","Member has been Delete")



lbtitle=Label(root,text='LIBRARY MANAGEMENT SYSTEM',bg="powder blue",fg="green",bd=20,relief=RIDGE,font='cosmicsansms,50,"bold', padx=20,pady=15)
lbtitle.grid(row=0,column=0,padx=450,pady=3)

###frame adding
frame=Frame(root,bd=12,relief=RIDGE,padx=20,bg='powder blue')
frame.place(x=0,y=130,width=1350,height=450)

labelframe=Label(frame,text='Personal information',font='cosmicsansms 15 bold',bg="powder blue",fg='green')
labelframe.grid(row=0,column=1,pady=10)

#####data frame left
###label section
Member=Label(frame,text='Member full name:',font='cosmicsansms 10 bold',bg='powder blue')
Member.grid(row=1,column=0)
idno=Label(frame,text='ID No.:',font='cosmicsansms 10 bold',bg='powder blue')
idno.grid(row=2,column=0)
adress=Label(frame,text='Address:',font='cosmicsansms 10 bold',bg='powder blue')
adress.grid(row=3,column=0)
mobile=Label(frame,text='Mobile Number:',font='cosmicsansms 10 bold',bg='powder blue')
mobile.grid(row=4,column=0)
###variable for storing values
namevalue=StringVar()
idvalue= StringVar()
adressvalue=StringVar()
mobilevalue=StringVar()

memberentry=Entry(frame,font='cosmicsansms 10 bold',textvariable=namevalue,width=25)
memberentry.grid(row=1,column=1,pady=5)
identry=Entry(frame,font='cosmicsansms 10 bold',textvariable=idvalue,width=25)
identry.grid(row=2,column=1,pady=5)
adressentry=Entry(frame,font='cosmicsansms 10 bold',textvariable=adressvalue,width=25)
adressentry.grid(row=3,column=1,pady=5)
mobileentry=Entry(frame,font='cosmicsansms 10 bold',textvariable=mobilevalue,width=25)
mobileentry.grid(row=4,column=1,pady=5)


###book information
labelframe=Label(frame,text='Book information',font='cosmicsansms 17 bold',bg="powder blue",fg='green')
labelframe.grid(row=5,column=1,pady=10,padx=5)

book=Label(frame,text='Book id:',font='cosmicsansms 10 bold',bg='powder blue')
book.grid(row=6,column=0)
book1=Label(frame,text='Book Title:',font='cosmicsansms 10 bold',bg='powder blue')
book1.grid(row=7,column=0)
dateborrow=Label(frame,text='Date of Borrowed:',font='cosmicsansms 10 bold',bg='powder blue')
dateborrow.grid(row=8,column=0)
datedue=Label(frame,text='Date Due:',font='cosmicsansms 10 bold',bg='powder blue')
datedue.grid(row=9,column=0)
days=Label(frame,text='Days on Book:',font='cosmicsansms 10 bold',bg='powder blue')
days.grid(row=10,column=0)
late=Label(frame,text='Late Return Fine:',font='cosmicsansms 10 bold',bg='powder blue')
late.grid(row=11,column=0)

###variable for storing values
bookvalue=StringVar()
book1value=StringVar()
dateborrowvalue=StringVar()
dateduevalue=StringVar()
daysvalue=StringVar()
latevalue=StringVar()

####entry of books
bookentry=Entry(frame,font='cosmicsansms 10 bold',textvariable=bookvalue,width=25)
bookentry.grid(row=6,column=1,pady=5)
book1entry=Entry(frame,font='cosmicsansms 10 bold',textvariable=book1value,width=25)
book1entry.grid(row=7,column=1,pady=5)
dateborrowentry=Entry(frame,font='cosmicsansms 10 bold',textvariable=dateborrowvalue,width=25)
dateborrowentry.grid(row=8,column=1,pady=5)
datedueentry=Entry(frame,font='cosmicsansms 10 bold',textvariable=dateduevalue,width=25)
datedueentry.grid(row=9,column=1,pady=5)
daysentry=Entry(frame,font='cosmicsansms 10 bold',textvariable=daysvalue,width=25)
daysentry.grid(row=10,column=1,pady=5)
lateentry=Entry(frame,font='cosmicsansms 10 bold',textvariable=latevalue,width=25)
lateentry.grid(row=11,column=1,pady=5)

####data frames for book
bookframe=LabelFrame(frame,bd=12,relief=RIDGE,bg='powder blue',font=('arial',14,'bold'),text='Book Details')
bookframe.place(x=550,y=5,width=700,height=395)

textbox=Text(bookframe,font=('arial',12,'bold'),width=40,height=18,pady=1,padx=10)
textbox.grid(row=0,column=3)

listscrolbar=Scrollbar(bookframe)
listscrolbar.grid(row=0,column=1,sticky='nw')


listbook=['headfirt book','learn python the hard way','python programming','secret Rashsy','python cookbook','into mechine learning',
          'machine tech','elite jungle python','python advance','java learning','c++ learning','python core','mysql book','djanjo','elite programming',
          'jodha akbar','maharana pratap','into the woods','stranger things','call of duety','tcil it','true colors','rambo return','prey' ]


def selectbook(event=""):
    value=str(listbox.get(listbox.curselection()))
    x=value
    if x== 'headfirt book':
        bookvalue.set("BKID2001")
        book1value.set("python mannual")
        d1=datetime.datetime.today()
        d2=datetime.timedelta(days=15)
        d3=d1+d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("15")
        latevalue.set("Rs. 50")

    elif x== 'learn python the hard way':
        bookvalue.set("BKID2004")
        book1value.set("python mannual")
        d1=datetime.datetime.today()
        d2=datetime.timedelta(days=15)
        d3=d1+d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("16")
        latevalue.set("Rs. 60")

    elif x== 'python programming':
        bookvalue.set("BKID2002")
        book1value.set("python mannual")
        d1=datetime.datetime.today()
        d2=datetime.timedelta(days=15)
        d3=d1+d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 70")

    elif x == 'secret Rashsy':
        bookvalue.set("BKID2002")
        book1value.set("secret rashay mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 50")

    elif x == 'python cookbook':
        bookvalue.set("BKID2005")
        book1value.set("python mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 60")

    elif x == 'into mechine learning':
        bookvalue.set("BKID2006")
        book1value.set("into mechine learning mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=8)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 50")

    elif x == 'elite jungle python':
        bookvalue.set("BKID2007")
        book1value.set("djanjo  mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 100")

    elif x == 'python advance':
        bookvalue.set("BKID2008")
        book1value.set("pyhon core with djanjo mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 150")

    elif x == 'java learning':
        bookvalue.set("BKID2009")
        book1value.set("java mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=7)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 50")

    elif x == 'c++ learning':
        bookvalue.set("BKID2010")
        book1value.set("c++ mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 50")

    elif x == 'python core':
        bookvalue.set("BKID2012")
        book1value.set("core mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 50")

    elif x == 'mysql book':
        bookvalue.set("BKID2011")
        book1value.set("mysql  mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 50")

    elif x == 'sdjanjo':
        bookvalue.set("BKID2013")
        book1value.set("djanjo mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 50")

    elif x == 'elite programming':
        bookvalue.set("BKID2014")
        book1value.set("basic mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 50")

    elif x == 'jodha akbar':
        bookvalue.set("BKID2015")
        book1value.set("jodha akbar mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=12)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("17")
        latevalue.set("Rs. 60")

    elif x == 'maharana pratap':
        bookvalue.set("BKID2016")
        book1value.set("maharana pratap mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=25)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 50")

    elif x == 'into the woods':
        bookvalue.set("BKID2017")
        book1value.set("jungle survive mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 50")

    elif x == 'stranger things':
        bookvalue.set("BKID2018")
        book1value.set("horror mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 100")

    elif x == 'call of duety':
        bookvalue.set("BKID2019")
        book1value.set("game mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=30)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 60")


    elif x == 'tcil it':
        bookvalue.set("BKID20")
        book1value.set("tcil it office mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 50")


    elif x == ' true colors':
        bookvalue.set("BKID2021")
        book1value.set("comic mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set("Rs. 50")


    elif x == 'rambo return':
        bookvalue.set("BKID2022")
        book1value.set("rambo story mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set(None)


    elif x == 'prey':
        bookvalue.set("BKID2023")
        book1value.set("preditor mannual")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=13)
        d3 = d1 + d2
        dateborrowvalue.set(d1)
        dateduevalue.set(d3)
        daysvalue.set("10")
        latevalue.set(None)

def get_cursor(event=""):
    cursor_row=library_table.focus()
    content=library_table.item(cursor_row)
    row=content['values']

    namevalue.set(row[0]),
    idvalue.set(row[1]),
    adressvalue.set(row[2]),
    mobilevalue.set(row[3]),
    bookvalue.set(row[4]),
    book1value.set(row[5]),
    dateborrowvalue.set(row[6]),
    dateduevalue.set(row[7]),
    daysvalue.set(row[8]),
    latevalue.set(row[9])



listbox=Listbox(bookframe,font=('arial',12,'bold'),width=28,height=18)
##binding after set values
listbox.bind("<<ListboxSelect>>", selectbook)
listbox.grid(row=0,column=2,padx=4)
listscrolbar.config(command=listbox.yview)

for items in listbook:
    listbox.insert(END,items)

    ######buttons
addbtn=Button(frame,text='ADD DATA',font=('arial',8,'bold'),fg='blue',command=adddata)
addbtn.grid(row=12,column=0,pady=4)

addbtn=Button(frame,text='Show Data',font=('arial',8,'bold'),fg='blue',width=20,command=showdata)
addbtn.grid(row=12,column=1)

addbtn=Button(frame,text='Update',font=('arial',8,'bold'),fg='blue',width=20,command=update)
addbtn.grid(row=12,column=2)

addbtn=Button(frame,text='Delete',font=('arial',8,'bold'),fg='blue',width=20,command=delete)
addbtn.grid(row=12,column=3)

addbtn=Button(frame,text='Reset',font=('arial',8,'bold'),fg='blue',width=20,command=reset)
addbtn.grid(row=12,column=4)

addbtn=Button(frame,text='Exit',font=('arial',8,'bold'),fg='blue',width=20,command=exit)
addbtn.grid(row=12,column=5)

###### information frame #######
frame1=Frame(root,bd=12,relief=RIDGE,padx=20,bg='powder blue')
frame1.place(x=0,y=580,width=1380,height=150)
tableframe=Frame(frame1,bd=6,relief=RIDGE,bg='powder blue')
tableframe.place(width=1350,height=140)

##scroll bar
xscroll=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
yscroll=ttk.Scrollbar(tableframe,orient=VERTICAL)

library_table = ttk.Treeview(tableframe,columns=("membername","idno","adress","mobileno","bookid","booktitle","dateborrow","duedate","daysbook","latefine"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

xscroll.pack(side=BOTTOM,fill=X)
yscroll.pack(side=RIGHT,fill=Y)

xscroll.config(command=library_table.xview)
yscroll.config(command=library_table.yview)
library_table.heading("membername",text="Member Name")
library_table.heading("idno",text="IDNO.")
library_table.heading("adress",text="Adress")
library_table.heading("mobileno",text="Mobile No.")
library_table.heading("bookid",text="Book ID")
library_table.heading("booktitle",text="Book Title")
library_table.heading("dateborrow",text="Date Of Borrow")
library_table.heading("duedate",text="Due Date")
library_table.heading("daysbook",text="Days on Book")
library_table.heading("latefine", text="Late Return Fine")

library_table["show"]="headings"
library_table.pack(fill=BOTH,expand=1)

library_table.column("membername",width=100)
library_table.column("idno",width=100)
library_table.column("adress",width=150)
library_table.column("mobileno",width=100)
library_table.column("bookid",width=100)
library_table.column("booktitle",width=150)
library_table.column("dateborrow",width=150)
library_table.column("duedate",width=150)
library_table.column("daysbook",width=100)
library_table.column("latefine",width=100)

fatchdata()
###from lib_table to form data
library_table.bind("<ButtonRelease-1>",get_cursor)








root.mainloop()
