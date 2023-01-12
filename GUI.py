from tkinter import Button, Entry, Label, Tk 

app_window = Tk() 
app_window.title("GUI APP") 
app_window.geometry("420x150") 
app_window.resizable(1,1)

e = Entry(app_window,width=20)
e.insert(0,"Enter Name: ")
e.pack()

def myfun():
    hellow = "Hello " + e.get()
    myLabel1 = Label(app_window,text=hellow)
    myLabel1.pack()

button1 = Button(app_window,text="click me!",command=myfun)
button1.pack()
app_window.mainloop()
