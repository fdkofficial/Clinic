# from tkinter import *
# from tkinter import ttk,filedialog
# from ttkthemes import ThemedTk
# from PIL import *
# import os
# import datetime
# if (not os.path.exists("patient.fdk")):
#     with open("patient.fdk",'w') as f:
#         f.write(" ")
# window=ThemedTk(theme="radiance")
# window.geometry("500x500")
# window.title("FDK Clinic")
# name=StringVar()
# age=StringVar()
# img=PhotoImage(file="button (6).png")
# searchvar=StringVar()
# def search1():
#     search_data=searchvar.get() 
#     fh = open('patient.fdk','r')
#     i=" "
#     count=1
#     while (i):
#         i=fh.readline()
#         l=i.split()
#         if search_data in l:
#             count=count+1
#             text2=Text(fr1)
#             text2.place(x=30,y=50,height=250,width=300)
#             text2.insert(INSERT,i)
            
# def Record1():
#     file=filedialog.askopenfile('r')
#     if file is not None:
#         content=file.read()
#         global fr1
#         fr1=Frame(window)
#         fr1.place(x=0,y=0,height=500,width=500)
#         global text
#         text=Text(fr1)
#         text.place(x=30,y=50,height=350,width=400)
#         text.insert(INSERT,content)
#         searchbar=ttk.Entry(fr1,textvariable=searchvar)
#         searchbar.place(x=240,y=15,width=150)
#         searchbut=ttk.Button(fr1,text="Search",command=search1)
#         searchbut.place(x=390,y=10,width=90)
#         scr=ttk.Scrollbar(fr1)
#         scr.pack(side=RIGHT,fill=Y)
#         scr.config(command=text.yview)
#         b2=ttk.Button(fr1,text="Save",command=save)
#         b2.place(x=10,y=10)
#         b3=Button(fr1,image=img,text="Back",bd=0,command=fr1.destroy)
#         b3.place(x=250,y=420)
# def save():
#     with open("patient.fdk",'r') as f:
#         f.read()
#     content=text.get("1.0",END)
#     with open("patient.fdk",'w') as f:
#         f.write(str(content))
# def files():
#     a=name.get()
#     b=age.get()
#     c=en3.get(1.0,END)
#     d=radiovar.get()
#     now=datetime.date.today()
#     pg=0
#     lineno=0
#     with open("patient.fdk",'r') as r:
#         for line in r:
#             pg +=1
#             if pg%4==0:
#                 lineno +=1
#     #lineno=pg+1
#     with open("patient.fdk",'a+') as f:
#         f.write(f'{lineno} ) Name : {a}    {now}\n Age : {b}\n Gender : {d}\n Details : {c}\n ')
# def read1():
#     with open("patient.fdk",'r') as f:
#         print(f.read())
# def reset():
#     #with open("patient.fdk",'w') as f:
#         #f.write("")
#     en1=ttk.Entry(window,text="")
#     en1.place(x=70,y=10,width=200)
#     en2=ttk.Entry(window,text="")
#     en2.place(x=70,y=50)
#     en3=Text(window)
#     en3.place(x=70,y=90,height=150,width=250)
# lab1=Label(window,text="Name : ")
# lab1.place(x=5,y=10)
# lab2=Label(window,text="Age : ")
# lab2.place(x=5,y=50)
# en1=ttk.Entry(window,textvariable=name)
# en1.place(x=70,y=10,width=300)
# en2=ttk.Entry(window,textvariable=age)
# en2.place(x=70,y=50)
# lab3=Label(window,text="Details : ")
# lab3.place(x=5,y=90)
# en3=Text(window)
# en3.place(x=70,y=90,height=270,width=350)
# gender=Label(window,text="Gender :")
# gender.place(x=5,y=368)
# radiovar=StringVar()
# radio1=ttk.Radiobutton(window,text="Male",value="Male",variable=radiovar)
# radio2=ttk.Radiobutton(window,text="Female",value="Female",variable=radiovar)
# radio1.place(x=70,y=370)
# radio2.place(x=145,y=370)
# b1=ttk.Button(window,text="Submit",command=files)
# b1.place(x=180,y=400)
# b2=ttk.Button(window,text="Record",command=Record1)
# b2.place(x=25,y=400)
# b3=ttk.Button(window,text="Clear",command=reset)
# b3.place(x=400,y=20,width=79)
# b4=ttk.Button(window,text="Load",command=read1)
# b4.place(x=25,y=440)
# b5=ttk.Button(window,text="Exit",command=window.destroy)
# b5.place(x=180,y=440)
# intro_frame = Frame(window)
# intro_frame.place(x=0,y=0,height=500,width=500)
# intro_label = Label(intro_frame,text="Welcome! Click Here to Continue ",bd=0,font=("Cooper Black",18))
# intro_label.place(x=80,y=150)
# intro_button = ttk.Button(intro_frame,text="Click me",command=intro_frame.destroy)
# intro_button.place(x=150,y=200)
# window.mainloop()