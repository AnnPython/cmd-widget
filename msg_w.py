
import tkinter as tk
import sys

 
arg=sys.argv
root = tk.Tk()
if '-w' or '-t' in arg:
    w1 = arg.index('-w')
    lb = tk.Label(text = arg[w1+1], font = ('Courier', '22'))
    lb.pack()
    n = arg.index('-t')
    x = arg[n+1]
    root.after(x)
   
def kill():
    root.destroy()
root.mainloop()
