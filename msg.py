import tkinter as tk
import sys

arg=sys.argv
if '-w' in arg:
    w1 = arg.index('-w')
    mes = arg[w1+1] 

else:
    mes='Это сообщение'
   
def kill():
    root.destroy()
root = tk.Tk()    
root.after(5000,kill)
lb = tk.Label(text = mes, font = ('Courier', '22'))
lb.pack()
root.mainloop()
