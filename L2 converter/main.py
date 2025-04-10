from tkinter import *
import tkinter.font as font
gui = Tk()
gui.title('celcius <=> farenhiet')
description = Label(text='celcius --> farenhiet',font=font.Font(family='impact',size = 20),fg='black',bg='grey')
description.pack()
frame = Frame(gui)
frame.pack(padx=200,pady=100)
message = Label(frame,text='enter temp in C°',font=font.Font(family='impact',size = 20),fg='black',bg='grey')
message.grid(row=1,column=1)


gui.mainloop()