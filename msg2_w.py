import tkinter as tk
from tkinter import messagebox as mb
import sys
from time import sleep
arg=sys.argv
root = tk.Tk()
if '-w' or '-t' in arg:
    w1 = arg.index('-w') 
    mb.showinfo(title='Это сообщение', message=arg[w1+1])
    n = arg.index('-t')
    x = arg[n+1]
       
    
def kill():
    root.destroy()



root.mainloop()




    

