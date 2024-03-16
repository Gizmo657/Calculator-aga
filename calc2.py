from tkinter import *
from tkinter import ttk
form1 = Tk()
form1.title("Calc2")
form1.geometry("260x350")

def check0(x, y):
    if y==0:
        x=0
        y=0
        entr.delete(0, END)
        tex["text"] = f"Ошибка: Деление на 0"
    else:
        entr.delete(0, END)
        tex["text"] = f"{x} : {y} ="
        x=x//y
        g=str(x)
        entr.insert(0, g)

tex = ttk.Label()
entr = ttk.Entry()
bpl = ttk.Button(text="+", command=make1)
bmin = ttk.Button(text="-", command=make2)
bmul = ttk.Button(text="x", command=make3)
bdiv = ttk.Button(text=":", command=make4)
beq = ttk.Button(text="=", command=makeq)
bcl = ttk.Button(text="CE", command=makec)

tex.pack()
entr.pack()
bpl.pack()
bmin.pack()
bmul.pack()
bdiv.pack()
beq.pack()
bcl.pack()

form1.mainloop()
