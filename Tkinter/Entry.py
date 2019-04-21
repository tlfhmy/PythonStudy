import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("800x600")
win.title("Entry")

win.resizable(0, 0)

aLable = ttk.Label(win, text="A Lable")
aLable.grid(column=0, row=0)

def clickMe():
    #action.configure(text="** I have been Clicked! **")
    #aLable.configure(foreground='red')
    action.configure(text='Hello ' + name.get())

action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=0)
#action.configure(state='disable')

ttk.Label(win, text="Enter a name: ").grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()

ttk.Label(win, text="Choose a number:").grid(column=2, row=0)
win.mainloop()