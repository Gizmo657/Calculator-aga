import unittest
from tkinter import *
from tkinter import ttk
from tkinter import END
from calc2 import check0, make1, make2, make3, make4, makeq, makec

class TestCalcFunctions(unittest.TestCase):
    global x, y, c

    def test_make1(self):
        entr = ttk.Entry()
        tex = ttk.Label()
        x = 6
        y = 5
        c = 1
        da=1
        x=makeq(c,x,y,entr,tex, da)

        self.assertEqual(x, 11)
    
    def test_make2(self):
      entr = ttk.Entry()
      tex = ttk.Label()
      x = 6
      y = 5
      c = 2
      da=1
      x=makeq(c,x,y,entr,tex, da)

      self.assertEqual(x, 1)

    def test_make3(self):
      entr = ttk.Entry()
      tex = ttk.Label()
      x = 6
      y = 5
      c = 3
      da=1
      x=makeq(c,x,y,entr,tex, da)

      self.assertEqual(x, 30)

    def test_make4(self):
      entr = ttk.Entry()
      tex = ttk.Label()
      x = 20
      y = 5
      c = 4
      da=1
      x=makeq(c,x,y,entr,tex, da)

      self.assertEqual(x, 4)

    def test_make4_1(self):
      entr = ttk.Entry()
      tex = ttk.Label()
      x = 20
      y = 0
      c = 4
      da=1
      x=makeq(c,x,y,entr,tex, da)

      self.assertEqual(x, 'Ошибка деление на нолл')

if __name__ == '__main__':
    unittest.main()
