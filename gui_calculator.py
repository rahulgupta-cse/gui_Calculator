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
        