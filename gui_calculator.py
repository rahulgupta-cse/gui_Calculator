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