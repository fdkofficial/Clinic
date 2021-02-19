from tkinter import *
from tkinter import ttk,filedialog
from ttkthemes import ThemedTk
from PIL import *
import os
import datetime
if (not os.path.exists("patient.fdk")):
    with open("patient.fdk",'w') as f:
        f.write(" ")
window=ThemedTk(theme="radiance")
window.geometry("500x500")
window.title("FDK Clinic")
name=StringVar()
age=StringVar()
img=PhotoImage(file="button (6).png")
searchvar=StringVar()
ent=StringVar()
def search1():
    search_data=searchvar.get() 
    fh = open('patient.fdk','r')
    i=" "
    count=1
    while (i):
        i=fh.readline()
        l=i.split()
        if search_data in l:
            count=count+1
            text2=Text(fr1)
            text2.place(x=30,y=50,height=250,width=300)
            text2.insert(INSERT,i)
            
def Record1():
    def go():
        frpass.destroy()
        match=apass.get()
        if match=="123":
            # file=filedialog.askopenfile('r')
            # if file is not None:
            #     content=file.read()
            file=open("patient.fdk")
            content=file.read()
            global fr1
            fr1=Frame(window)
            fr1.place(x=0,y=0,height=500,width=500)
            global text
            text=Text(fr1)
            text.place(x=30,y=50,height=350,width=400)
            text.insert(INSERT,content)
            searchbar=ttk.Entry(fr1,textvariable=searchvar)
            searchbar.place(x=240,y=15,width=150)
            searchbut=ttk.Button(fr1,text="Search",command=search1)
            searchbut.place(x=390,y=10,width=90)
            scr=ttk.Scrollbar(fr1)
            scr.pack(side=RIGHT,fill=Y)
            scr.config(command=text.yview)
            b2=ttk.Button(fr1,text="Save",command=save)
            b2.place(x=10,y=10)
            b3=Button(fr1,image=img,text="Back",bd=0,command=fr1.destroy)
            b3.place(x=250,y=420)
        else:
            frpass.destroy
    apass=StringVar()
    frpass=Frame(window,highlightbackground="black")
    frpass.config(background="white",highlightthickness=1)
    frpass.place(x=100,y=200,height=100,width=350)
    labpas=Label(frpass,text="Enter Password : ",bg="white")
    labpas.place(x=10,y=5)
    entpas=Entry(frpass,textvariable=apass)
    entpas.place(x=150,y=5)
    butpass=Button(frpass,text="Done",command=go)
    butpass.place(x=70,y=50)
def save():
    with open("patient.fdk",'r') as f:
        f.read()
    content=text.get("1.0",END)
    with open("patient.fdk",'w') as f:
        f.write(str(content))
def files():
    a=name.get()
    b=age.get()
    c=en3.get(1.0,END)
    d=radiovar.get()
    e=ent.get()
    now=datetime.date.today()
    pg=0
    lineno=0
    with open("patient.fdk",'r') as r:
        for line in r:
            pg +=1
            if pg%5==0:
                lineno +=1
    #lineno=pg+1
    with open("patient.fdk",'a+') as f:
        f.write(f'{lineno} ) Name : {a}    {now}\n Age : {b}\n Gender : {d}\n Payment : {e} Rs\n Details : {c}\n')
def read1():
    with open("patient.fdk",'r') as f:
        print(f.read())
def reset():
    #with open("patient.fdk",'w') as f:
        #f.write("")
    en1=ttk.Entry(window,text="")
    en1.place(x=70,y=10,width=300)
    en2=ttk.Entry(window,text="")
    en2.place(x=70,y=50)
    en3=Text(window)
    en3.place(x=70,y=90,height=150,width=250)
def show(c):
    ent.set(ent.get()+c)
def equal(rs):
    ex=ent.get()
    ent.set(eval(ex))
def clr():
    a=""
    ent.set(a)
def startfile1():
    os.startfile(os.listdir()[ebt])
def pfd():
    global ebt
    ebt=0
    frpdf=Frame(window)
    frpdf.place(x=0,y=0,height=500,width=500)
    for v,each in enumerate(os.listdir("PDFs/")):
        lis=v,each
    labpdf=Label(frpdf,text=lis,font=("Cooper black",10))
    labpdf.place(x=10,y=10)
    etpdf=ttk.Entry(frpdf,textvariable=ebt)
    etpdf.place(x=40,y=455,width=150)
    bu=ttk.Button(frpdf,text="Open",command=startfile1)
    bu.place(x=200,y=450)
    bu2=ttk.Button(frpdf,text="Back",command=frpdf.destroy)
    bu2.place(x=330,y=450)
    #file=filedialog.askopenfile('r')
def medicine():
    frmed=Frame(window)
    frmed.place(x=0,y=0,height=500,width=500)
    with open("medicines.fdk","r") as r:
        readcont=r.read()
    global textmed
    textmed=Text(frmed)
    textmed.place(x=25,y=100,height=350,width=450)
    textmed.insert(INSERT,readcont)
    labmed=Label(frmed,text="List of Medicines :-",font=("cooper black","15"))
    labmed.place(x=25,y=5)
    butmed=ttk.Button(frmed,text="Save",command=medsave)
    butmed.place(x=50,y=35)
    medback=ttk.Button(frmed,text="Back",command=frmed.destroy)
    medback.place(x=200,y=35)
def medsave():
    if not os._exists("medicines.fdk"):
        with open("medicines.fdk",'w') as w:
            w.write(" ")
    meddetail=textmed.get("1.0",END)
    with open("medicines.fdk",'w') as w:
        w.write(str(meddetail))
lab1=Label(window,text="Name : ")
lab1.place(x=5,y=10)
lab2=Label(window,text="Age : ")
lab2.place(x=5,y=50)
en1=ttk.Entry(window,textvariable=name)
en1.place(x=70,y=10,width=300)
en2=ttk.Entry(window,textvariable=age)
en2.place(x=70,y=50)
lab3=Label(window,text="Details : ")
lab3.place(x=5,y=90)
en3=Text(window)
en3.place(x=70,y=90,height=150,width=350)
gender=Label(window,text="Gender :")
gender.place(x=5,y=250)
radiovar=StringVar()
radio1=ttk.Radiobutton(window,text="Male",value="Male",variable=radiovar)
radio2=ttk.Radiobutton(window,text="Female",value="Female",variable=radiovar)
radio1.place(x=70,y=252)
radio2.place(x=145,y=252)
fees=Label(window,text="Fees : ")
fees.place(x=5,y=285)
feeset=ttk.Entry(window,textvariable=ent)
feeset.place(x=70,y=285,width=200)
plus=ttk.Button(window,text="+",command=lambda:show("+") )
plus.place(x=85,y=310,width=50)
minus=ttk.Button(window,text="-",command=lambda:show("-") )
minus.place(x=150,y=310,width=50)
mult=ttk.Button(window,text="*",command=lambda:show("*") )
mult.place(x=85,y=350,width=50)
div=ttk.Button(window,text="/",command=lambda:show("/") )
div.place(x=150,y=350,width=50)
equ=ttk.Button(window,text="=",command=lambda:equal("rs"))
equ.place(x=210,y=310,width=50)
clear=ttk.Button(window,text="Clr",command=clr)
clear.place(x=210,y=350,width=50)
calbut=ttk.Button(window,text="7",command=lambda:show("7"))
calbut.place(x=300,y=250,width=50)
calbut=ttk.Button(window,text="8",command=lambda:show("8"))
calbut.place(x=350,y=250,width=50)
calbut=ttk.Button(window,text="9",command=lambda:show("9"))
calbut.place(x=400,y=250,width=50)
calbut=ttk.Button(window,text="4",command=lambda:show("4"))
calbut.place(x=300,y=290,width=50)
calbut=ttk.Button(window,text="5",command=lambda:show("5"))
calbut.place(x=350,y=290,width=50)
calbut=ttk.Button(window,text="6",command=lambda:show("6"))
calbut.place(x=400,y=290,width=50)
calbut=ttk.Button(window,text="1",command=lambda:show("1"))
calbut.place(x=300,y=330,width=50)
calbut=ttk.Button(window,text="2",command=lambda:show("2"))
calbut.place(x=350,y=330,width=50)
calbut=ttk.Button(window,text="3",command=lambda:show("3"))
calbut.place(x=400,y=330,width=50)
calbut=ttk.Button(window,text="0",command=lambda:show("0"))
calbut.place(x=350,y=370,width=50)
b1=ttk.Button(window,text="Submit",command=files)
b1.place(x=180,y=400)
b2=ttk.Button(window,text="Record",command=Record1)
b2.place(x=25,y=400)
b3=ttk.Button(window,text="Clear",command=reset)
b3.place(x=400,y=20,width=79)
b4=ttk.Button(window,text="Load",command=read1)
b4.place(x=25,y=440)
b5=ttk.Button(window,text="Exit",command=window.destroy)
b5.place(x=180,y=440)
b6=ttk.Button(window,text="PDFs",command=pfd)
b6.place(x=330,y=410)
b7=ttk.Button(window,text="Medicines",command=medicine)
b7.place(x=330,y=450)
intro_frame = Frame(window)
intro_frame.place(x=0,y=0,height=500,width=500)
intro_label = Label(intro_frame,text="Welcome! Click Here to Continue ",bd=0,font=("Cooper Black",18))
intro_label.place(x=80,y=150)
intro_button = ttk.Button(intro_frame,text="Click me",command=intro_frame.destroy)
intro_button.place(x=150,y=200)
window.mainloop()