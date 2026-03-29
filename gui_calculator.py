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

        # adding number buttons (4,5,6)
        Button(width=11,height=4,text='4',relief='flat',bg='white',command=lambda:self.show(4)).place(x=0 ,y=200)
        Button(width=11,height=4,text='5',relief='flat',bg='white',command=lambda:self.show(5)).place(x=90 ,y=200)
        Button(width=11,height=4,text='6',relief='flat',bg='white',command=lambda:self.show(6)).place(x=180 ,y=200)

        # adding number buttons (1,2,3)
        Button(width=11,height=4,text='1',relief='flat',bg='white',command=lambda:self.show(1)).place(x=0 ,y=275)
        Button(width=11,height=4,text='3',relief='flat',bg='white',command=lambda:self.show(3)).place(x=180 ,y=275)
        Button(width=11,height=4,text='2',relief='flat',bg='white',command=lambda:self.show(2)).place(x=90 ,y=275)

        # adding 0 and decimal button
        Button(width=11,height=4,text='0',relief='flat',bg='white',command=lambda:self.show(0)).place(x=90 ,y=350)
        Button(width=11,height=4,text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=180 ,y=350)

        # adding operator buttons
        Button(width=11,height=4,text='+',relief='flat',bg='white',command=lambda:self.show('+')).place(x=270 ,y=275)
        Button(width=11,height=4,text='-',relief='flat',bg='white',command=lambda:self.show('-')).place(x=270 ,y=200)
        Button(width=11,height=4,text='/',relief='flat',bg='white',command=lambda:self.show('/')).place(x=270 ,y=50)
        Button(width=11,height=4,text='x',relief='flat',bg='white',command=lambda:self.show('*')).place(x=270 ,y=125)

        # adding equal button
        Button(width=11,height=4,text='=',relief='flat',bg='lightgray',command=self.solve).place(x=270 ,y=350)

        # adding clear button
        Button(width=11,height=4,text='C',relief='flat',bg='white',command=self.clear).place(x=0 ,y=350)

        #  correct placement
    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)