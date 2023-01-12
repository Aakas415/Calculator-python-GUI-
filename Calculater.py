from calendar import c
import math
from multiprocessing.sharedctypes import Value
from tkinter import *
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

import click

root = Tk()
root.title("Calcy :)")


def clear():
    e.delete(0,END)

def click(number):
    # e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def add():
    fnum = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(fnum)
    e.delete(0,END)

def sub():
    fnum = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(fnum)
    e.delete(0,END)


def mul():
    fnum = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(fnum)
    e.delete(0,END)


def div():
    fnum = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(fnum)
    e.delete(0,END)


def equal():
    snum = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0,f_num + int(snum))
        
    if math == "substraction":
        e.insert(0,f_num - int(snum))
    
    if math == "multiplication":
        e.insert(0,f_num * int(snum))

    if math == "division":
        e.insert(0,f_num / int(snum))

e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

button1 = Button(root,text="1", padx=40, pady=20,command=lambda: click(1))
button2 = Button(root,text="2", padx=40, pady=20,command=lambda: click(2))
button3 = Button(root,text="3", padx=40, pady=20,command=lambda: click(3))

button4 = Button(root,text="4", padx=40, pady=20,command=lambda: click(4))
button5 = Button(root,text="5", padx=40, pady=20,command=lambda: click(5))
button6 = Button(root,text="6", padx=40, pady=20,command=lambda: click(6))

button7 = Button(root,text="7", padx=40, pady=20,command=lambda: click(7))
button8 = Button(root,text="8", padx=40, pady=20,command=lambda: click(8))
button9 = Button(root,text="9", padx=40, pady=20,command=lambda: click(9))

button0 = Button(root,text="0", padx=40, pady=20,command=lambda: click(0))

buttonadd= Button(root,text="+",padx=39,pady=20,command=add)
button = Button(root,text="=",padx=91,pady=20,command=equal)
buttonclr = Button(root,text="Clear",padx=79,pady=20,command=clear)


buttonsub= Button(root,text="-",padx=41,pady=20,command=sub)
buttonmul = Button(root,text="*",padx=40,pady=20,command=mul)
buttondiv = Button(root,text="/",padx=40,pady=20,command=div)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)

buttonclr.grid(row=4,column=1,columnspan=2)
buttonadd.grid(row=5,column=0)
button.grid(row=5,column=1,columnspan=2)

buttonsub.grid(row=6,column=0)
buttonmul.grid(row=6,column=1)
buttondiv.grid(row=6,column=2)

root.mainloop()