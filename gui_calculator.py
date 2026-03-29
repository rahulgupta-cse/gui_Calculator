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