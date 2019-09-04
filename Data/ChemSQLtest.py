from ChemSQLMan import *
import tkinter
from tkinter import ttk


Chl = ChemLib("localhost","root","981722694","pdb","conver")
#Chl.ShowAll(100)
#Chl.ShowTables()
#Chl.ShowRows()
#Chl.Command()
#Chl.Insert("测试","Test","C=C","0.0")

root = tkinter.Tk()
root.title("MySQL Manage")
root.geometry("800x600")




cmb = ttk.Combobox(root)
cmb.pack()
cmb['value'] = ("one","two")
cmb.grid(column=1, row=1)


root.mainloop()
