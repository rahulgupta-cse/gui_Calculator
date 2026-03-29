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