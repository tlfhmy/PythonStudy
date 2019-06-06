from tkinter import *

win = Tk()
win.title("Cellular automata")
win.geometry("800x800")
win.resizable(0,0)

drwaArea = Canvas(
    win,
    width = 800-8*2, height=800-24,
    bg="white"
)

drwaArea.place(anchor="nw", x=8, y=24)

res = [[0,0],[0,1],[0,2],\
[1,0],[1,1],[1,2],\
[2,0],[2,1],[2,2]]
#n = 50
for i in (0,8):
    drwaArea.create_rectangle(
        (res[i][0]*600/3,res[i][1]*600/3),((res[i][0]+1)*600/3,(res[i][1]+1)*600/3),
        fill="gray", width=3
    )

win.mainloop()