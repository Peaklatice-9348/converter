from tkinter import *
import tkinter.font as font

def convert_temp():
    c = value.get()
    if c.replace('.','',1).isdigit():
        f = (float(c) * 4.5) + 32
        message.config(text='↓ ferenhiet(f°) ↓\n'+str(f),bg = 'green')
    else:
        message.config(text='Error\nvalue not found',bg = 'red')        
gui = Tk()
gui.title('celcius →  farenhiet')
gui.configure(bg='light blue')
description = Label(text='celcius → → farenhiet',font=font.Font(family='impact',size = 20),fg='black',bg='grey')
description.pack()
frame = Frame(gui,bg='light blue')
frame.pack(padx=20,pady=10)
message = Label(frame,text='enter temp in C°',font=font.Font(family='impact',size = 20),fg='black',bg='grey')
message.grid(row=1,column=1)
value = Entry(frame,bg='blue',fg='white')
value.grid(row=2,column=1)
convert = Button(frame,text='Enter',font=font.Font(family='impact',size = 20),fg='black',bg='grey',command=convert_temp)
convert.grid(row=4,column=1)
gui.mainloop()