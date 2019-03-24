import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
#win.resizable(0, 0)
aLable = ttk.Label(win, text="A Lable")
aLable.grid(column=0, row=0)

def ClickMe():
    action.configure(text="** I have been clicked! **")
    aLable.configure(foreground='red')

action = ttk.Button(win, text="Click Me!", command = ClickMe)
action.grid(column=1, row=0)


win.mainloop()
