from tkinter import *
from tkinter import ttk

form1 = Tk()
form1.title("Calc2")
form1.geometry("260x250")
form1.resizable(False, False)

da = 0
x = 0
y = 0
g = " "
c = 0

def check0(x, y, da):
    if y == 0:
        if da == 0:
            entr.delete(0, END)
            tex["text"] = ""
        return "Ошибка деления на 0"
    else:
        if da == 0:
            entr.delete(0, END)
            tex["text"] = f"{x} : {y} ="
            g = str(x // y)
            entr.insert(0, g)
        return x // y

def make1():
    global c, x
    g = entr.get()
    if g.isdigit():
        x = int(g)
        c = 1
        tex["text"] = f"{x} +"
        entr.delete(0, END)
        return True
    else:
        return False

def make2():
    global c, x
    g = entr.get()
    if g.isdigit():
        x = int(g)
        c = 2
        tex["text"] = f"{x} -"
        entr.delete(0, END)
        return True
    else:
        return False

def make3():
    global c, x
    g = entr.get()
    if g.isdigit():
        x = int(g)
        c = 3
        tex["text"] = f"{x} x"
        entr.delete(0, END)
        return True
    else:
        return False

def make4():
    global c, x
    g = entr.get()
    if g.isdigit():
        x = int(g)
        c = 4
        tex["text"] = f"{x} :"
        entr.delete(0, END)
        return True
    else:
        return False

def makeq():
    global x, c
    g = entr.get()
    if not g.isdigit() or c == 0:
        entr.delete(0, END)
        tex["text"] = ""
        return
    y = int(g)
    if c == 1:
        tex["text"] = f"{x} + {y} ="
        x += y
    elif c == 2:
        tex["text"] = f"{x} - {y} ="
        x -= y
    elif c == 3:
        tex["text"] = f"{x} x {y} ="
        x *= y
    elif c == 4:
        x = check0(x, y, da)
    entr.delete(0, END)
    entr.insert(0, str(x))
    c = 0

def makec():
    global x, y, c
    x = 0
    y = 0
    c = 0
    entr.delete(0, END)
    tex["text"] = ""

tex = ttk.Label(form1)
entr = ttk.Entry(form1)
bpl = ttk.Button(form1, text="+", command=make1)
bmin = ttk.Button(form1, text="-", command=make2)
bmul = ttk.Button(form1, text="x", command=make3)
bdiv = ttk.Button(form1, text=":", command=make4)
beq = ttk.Button(form1, text="=", command=makeq)
bcl = ttk.Button(form1, text="CE", command=makec)

tex.pack()
entr.pack()
bpl.pack()
bmin.pack()
bmul.pack()
bdiv.pack()
beq.pack()
bcl.pack()

form1.mainloop()
