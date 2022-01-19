from tkinter import *

root_window=Tk()
root_window.title('Fourth')


red_label = Label(root_window, text='Red', bg='Red', fg='black', width=20, height=5)
red_label.grid(row=0, column=0)

yellow_label =Label(root_window, text='Yellow', bg ='Yellow', fg='green', width=20, height=5)
yellow_label.grid(row=1, column=1)

green_label =Label(root_window, text='Green', bg ='Green', fg='yellow', width=20, height=5)
green_label.grid(row=2, column=2)


root_window.mainloop()