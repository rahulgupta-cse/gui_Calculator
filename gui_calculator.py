# starting my calculator project using tkinter
from tkinter import Tk, Entry, Button, StringVar

# creating calculator class
class Calculator:
    def __init__(self,master):
        master.title("Calculator")

        # setting window size and position with background color
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False,False)

        # storing equation
        self.equation = StringVar()
        self.entry_value = ''

        # display
        Entry(master, width=17, bg='#dcdcdc',font=('Arial Bold', 28),textvariable=self.equation).place(x=0, y=0)
        
        # adding bracket buttons
        Button(width=11,height=4,text='(',relief='flat',bg='white',command=lambda:self.show('(')).place(x=0 ,y=50)
        Button(width=11,height=4,text=')',relief='flat',bg='white',command=lambda:self.show(')')).place(x=90 ,y=50)

        # adding percentage button
        Button(width=11,height=4,text='%',relief='flat',bg='white',command=lambda:self.show('%')).place(x=180 ,y=50)

        # adding number buttons (7,8,9)
        Button(width=11,height=4,text='7',relief='flat',bg='white',command=lambda:self.show(7)).place(x=0 ,y=125)
        Button(width=11,height=4,text='8',relief='flat',bg='white',command=lambda:self.show(8)).place(x=90 ,y=125)
        Button(width=11,height=4,text='9',relief='flat',bg='white',command=lambda:self.show(9)).place(x=180 ,y=125)