from tkinter import *
from tkinter import ttk

def do():
	output['text']=name.get()

main_window = Tk()

username = StringVar()
output = StringVar()
name = ttk.Entry(main_window, textvariable=username)
name.pack()

output = ttk.Label(main_window,text = username.get())
output.pack()

but = ttk.Button(main_window, text='Do it!', command=do)
but.pack()
main_window.mainloop()