from tkinter import *
from tkinter import ttk


root_window = Tk()
frame = ttk.Frame(root_window, height=550, width=550, padding=50)

# frame['padding'] = (10,7,10,7)
frame['borderwidth'] = 15
frame['relief'] = 'sunken'
frame.grid()

label = ttk.Label(frame)# text == 'textvariable' ttk.Label(frame, text='Full name:')
label.grid()

resultsContents = StringVar()
label['textvariable'] = resultsContents
resultsContents.set('New value to display')



root_window.mainloop()