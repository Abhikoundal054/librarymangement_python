#
# ######important label options
# #text - adds the text
# #bd - background
# #fg - foreground =text color
# ##font - set the font
# #1font=("comicsansms",19,"bold")
# #2font=("comicsansms" 19 "bold")
# #padx - x padding= left,right space
# #pady - padding= upside down space
# #relief - border styling - SUNKIN,RAISED,GROOVE,RIDGE
# .pack()or.grid()
#
# #####important pack option
# # anchor = nw (title_label.pack(side bottom= anchor= 'sw')
# #fill
# #padx
# #pady
#
# ####variable classes in tkinter
# BooleanVar , DoubleVar , IntVar , StringVar
#
# ### 1 - code for text in gui form
# from tkinter import *
# root = Tk()
# root.geometry("444x250")
# root.title("MY First GUI")
#
# title_label = Label(text='''hello user you are doing cource of python in tcil-it
# date= 5 july 2022  to  5 jan 2023
# collage name= Adesh institute of technology gharuan
# branch of user = btech(cse)
# roll no =1817050''',bg='red',fg='white',padx=113,pady=144,font=("comicsansms 19 bold"))
# title_label.pack(side=BOTTOM,anchor='sw')
# root.mainloop()
#
#
# ##### -> important in button
# command=to call functn
#
# from tkinter import *
# root=Tk()
# def hello():
#     print('welcome to button1')
# def bye():
#     print('exit to button2')
# frame=Frame(root,borderwidth=6,bg="black",relief=SUNKEN)
# frame.pack(side=LEFT,anchor='nw')
#
# b1=Button(frame,fg='red',text='welcome',command=hello)
# b1.pack(side=LEFT,padx=13)
#
# b2=Button(frame,fg='red',text='exit',command=bye)
# b2.pack(side=LEFT,padx=13)
#
# root.mainloop()
#
#
#
#
# ####for making user and dance class page
# from tkinter import *
# root=Tk()
# root.geometry("600x300")
# root.title("dance classes")
#
# name=Label(root,text='Enter your name')
# name.grid()
#
# age=Label(root,text='Enter your age')
# age.grid(row=1)
#
# type=Label(root,text='Dance form')
# type.grid(row=2)
#
# namevalue=StringVar()
# agevalue=IntVar()
# typevalue=StringVar()
#
# nameentry=Entry(root,textvariable = namevalue)
# nameentry.grid(row=0,column=1)
# ageentry=Entry(root,text = agevalue )
# ageentry.grid(row=1,column=1)
# typeentry=Entry(root,text=typevalue)
# typeentry.grid(row=2,column=1)
#
# def getvals():
#     print(f"The name student is {namevalue.get()}")
#     print(f"The age student is {agevalue.get()}")
#     print(f"The type of danceclass is {typevalue.get()}")
#
#
# b1=Button(text='Submit',command=getvals)
# b1.grid()
# root.mainloop()
#
#
# ######### for check box , with button##############(airlines
# from tkinter import *
# root=Tk()
# ##heading
# label=Label(root,text='Welcome to indian airline',font="comicsansms 13 bold",pady=15)
# label.grid(row=0,column=3)
#
# #programme for print data after button
# def getvals():
#     print(f'Congrats! Your booking is done!')
#     print(f'{namevalue.get(),phonevalue.get(),gendervalue.get(),paymentmodevalue.get(),food_servicevalue.get()}')
#
#     file=(open('records.text',"a"))
#     file.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),paymentmodevalue.get(),food_servicevalue.get()}\n")
#     file.close()
#
# ##text for froms with packing (.grid mathod)
# name=Label(root,text='Name')
# name.grid(row=1,column=2)
# phone=Label(root,text="Phone")
# phone.grid(row=2,column=2)
# gender=Label(root,text="Gender")
# gender.grid(row=3,column=2)
# paymentmode=Label(root,text="Payment Mode")
# paymentmode.grid(row=4,column=2)
#
# ####variable for storing value
# namevalue = StringVar()
# phonevalue = StringVar()
# gendervalue = StringVar()
# paymentmodevalue = StringVar()
# food_servicevalue = IntVar()
#
# nameentry=Entry(root,textvariable=namevalue)
# nameentry.grid(row=1,column=3)
# phoneentry=Entry(root,textvariable=phonevalue)
# phoneentry.grid(row=2,column=3)
# genderentry=Entry(root,textvariable=gendervalue)
# genderentry.grid(row=3,column=3)
# paymentmodeentry=Entry(root,textvariable=paymentmodevalue)
# paymentmodeentry.grid(row=4,column=3)
# ##for check box with packing
# food_service=Checkbutton(root,text="want to pre-book your meal?",variable=food_servicevalue)
# food_service.grid(row=6,column=3,pady=14)
#
# b1=Button(root,text='Submit your Booking',command=getvals)
# b1.grid(row=7,column=2,pady=15,padx=13)
#
# root.mainloop()
#
#
