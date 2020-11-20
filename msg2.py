import sys
import tkinter as tk
from tkinter import messagebox as mb
arg=sys.argv
if '-t' in arg:
    n = arg.index('-t')
    x = arg[n+1]
    
else:
    mes='Это сообщение'
def kill():
    root.destroy()
root = tk.Tk()
root.after(x)
mb.showinfo(title='Это сообщение', message='Сообщение!')
root.mainloop()
