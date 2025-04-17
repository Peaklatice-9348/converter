from tkinter import *
import tkinter.font as font

def convert_weight():
    pass

gui = Tk()
gui.title('weight converter')
gui.configure(bg='white')

message = Label(text='enter weight',font=font.Font(family='impact',size = 10),fg='black',bg='white')
message.grid(row=1,column=1)

value = Entry(bg='light grey',fg='white')
value.grid(row=1,column=2)

convert = Button(text='Enter',font=font.Font(family='impact',size = 10),fg='black',width=5,height=1,bg='light grey',command=convert_weight)
convert.grid(row=1,column=3)

gram = Label(text='gram',font=font.Font(family='impact',size = 10),fg='black',bg='white')
gram.grid(row=2,column=1)

pound = Label(text='pound',font=font.Font(family='impact',size = 10),fg='black',bg='white')
pound.grid(row=2,column=2)

ounce = Label(text='ounce',font=font.Font(family='impact',size = 10),fg='black',bg='white')
ounce.grid(row=2,column=3)

gt = Text(gui,height=1,width=20)
gt.grid(row=3,column=1)

gui.mainloop()