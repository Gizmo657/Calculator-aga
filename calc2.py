from tkinter import *
from tkinter import ttk
form1 = Tk()
form1.title("Calc2")
form1.geometry("260x350")

x=0
y=0
g=" "
c=0
    
def make1():
    global c
    global x
    global y
    g=entr.get()
    if g.isdigit()==True:
        x=int(g)
        entr.delete(0, END)
        c=1
        tex["text"] = f"{x} +"
    else:
        x=0
        y=0
        entr.delete(0, END)

def make2():
    global c
    global x
    global y
    g=entr.get()
    if g.isdigit()==True:
        x=int(g)
        entr.delete(0, END)
        c=2
        tex["text"] = f"{x} -"
    else:
        x=0
        y=0
        entr.delete(0, END)

def make3():
    global c
    global x
    global y
    g=entr.get()
    if g.isdigit()==True:
        x=int(g)
        entr.delete(0, END)
        c=3
        tex["text"] = f"{x} x"
    else:
        x=0
        y=0
        entr.delete(0, END)

def make4():
    global c
    global x
    global y
    g=entr.get()
    if g.isdigit()==True:
        x=int(g)
        entr.delete(0, END)
        c=4
        tex["text"] = f"{x} :"
    else:
        x=0
        y=0
        entr.delete(0, END)

def makeq():
    global c
    global x
    global y
    g=entr.get()
    if g.isdigit()==False or c==0:
        x=0
        y=0
        entr.delete(0, END)
        c=0
    tex["text"] = f""
    if c==1:
        g=entr.get()
        y=int(g)
        entr.delete(0, END)
        tex["text"] = f"{x} + {y} ="
        x=x+y
        g=str(x)
        entr.insert(0, g)
    elif c==2:
        g=entr.get()
        y=int(g)
        entr.delete(0, END)
        tex["text"] = f"{x} - {y} ="
        x=x-y
        g=str(x)
        entr.insert(0, g)
    elif c==3:
        g=entr.get()
        y=int(g)
        entr.delete(0, END)
        tex["text"] = f"{x} x {y} ="
        x=x*y
        g=str(x)
        entr.insert(0, g)
    elif c==4:
        g=entr.get()
        y=int(g)
        check0(x,y)

def makec():
    x=0
    y=0
    entr.delete(0, END)
    c=0
    tex["text"] = f""

form1.mainloop()
