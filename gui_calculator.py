# starting my calculator project using tkinter
from tkinter import Tk

# creating main window
root = Tk()

# setting window title
root.title("Calculator")

# setting window size and position
root.geometry('357x420+0+0')

# disabling resize for fixed layout
root.resizable(False, False)

# setting background color
root.config(bg='gray')

# importing remaining tkinter components
from tkinter import Entry, Button, StringVar

# creating calculator class for better structure
class Calculator:
    def __init__(self, master):
        self.master = master
        # creating variable to store equation
        self.equation = StringVar()
        self.entry_value = ''
        
        # creating display screen
        Entry(master, width=17, bg='#dcdcdc', font=('Arial Bold', 28),textvariable=self.equation).place(x=0, y=0)
        # adding bracket buttons
        Button(master, text='(', width=11, height=4,command=lambda: self.show('(')).place(x=0, y=50)
        Button(master, text=')', width=11, height=4,command=lambda: self.show(')')).place(x=90, y=50)
        # adding percentage button
        Button(master, text='%', width=11, height=4,command=lambda: self.show('%')).place(x=180, y=50)
        # adding number buttons (7,8,9)
        Button(master, text='7', width=11, height=4,command=lambda: self.show(7)).place(x=0, y=125)
        Button(master, text='8', width=11, height=4,command=lambda: self.show(8)).place(x=90, y=125)
        Button(master, text='9', width=11, height=4,command=lambda: self.show(9)).place(x=180, y=125)
        # adding number buttons (4,5,6)
        Button(master, text='4', width=11, height=4,command=lambda: self.show(4)).place(x=0, y=200)
        Button(master, text='5', width=11, height=4,command=lambda: self.show(5)).place(x=90, y=200)
        Button(master, text='6', width=11, heightcommand=lambda: self.show(6)).place(x=180, y=200)

        # adding number buttons (1,2,3)
        Button(master, text='1', width=11, height=4,command=lambda: self.show(1)).place(x=0, y=275)
        Button(master, text='2', width=11, height=4,command=lambda: self.show(2)).place(x=90, y=275)
        Button(master, text='3', width=11, height=4,command=lambda: self.show(3)).place(x=180, y=275)

        # adding 0 and decimal button
        Button(master, text='0', width=11, height=4,command=lambda: self.show(0)).place(x=90, y=350)
        Button(master, text='.', width=11, height=4,command=lambda: self.show('.')).place(x=180, y=350)

        # adding operator buttons
        Button(master, text='+', width=11, height=4,command=lambda: self.show('+')).place(x=270, y=275)
        Button(master, text='-', width=11, height=4,command=lambda: self.show('-')).place(x=270, y=200)
        Button(master, text='/', width=11, height=4,command=lambda: self.show('/')).place(x=270, y=50)
        Button(master, text='x', width=11, height=4,command=lambda: self.show('*')).place(x=270, y=125)

        # adding equal button
        Button(master, text='=', width=11, height=4,bg='lightgray', command=self.solve).place(x=270, y=350)

        # adding clear button
        Button(master, text='C', width=11, height=4,command=self.clear).place(x=0, y=350)

# function to show input on screen
def show(self, value):
    self.entry_value += str(value)
    self.equation.set(self.entry_value)