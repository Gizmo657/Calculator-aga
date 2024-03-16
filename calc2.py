from tkinter import *
from tkinter import ttk
form1 = Tk()
form1.title("Calc2")
form1.geometry("260x350")

def make1():
    X=x

tex = ttk.Label()
entr = ttk.Entry()
bpl = ttk.Button(text="+", command=make1)
bmin = ttk.Button(text="-", command=make1)
bmul = ttk.Button(text="x", command=make1)
bdiv = ttk.Button(text=":", command=make1)
beq = ttk.Button(text="=", command=make1)
bcl = ttk.Button(text="CE", command=make1)

tex.pack()
entr.pack()
bpl.pack()
bmin.pack()
bmul.pack()
bdiv.pack()
beq.pack()
bcl.pack()

form1.mainloop()
