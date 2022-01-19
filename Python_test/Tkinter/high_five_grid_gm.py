import tkinter
from tkinter import ttk


def greeting():
	print(f'Hi Five!!! {user_name.get()}') # don't forget to cast '.get()'!!!



root_window = tkinter.Tk()
root_window.title('First true!')
root_window.columnconfigure(0, weight=1)
user_name = tkinter.StringVar()

input_frame = ttk.Frame(root_window, padding=(10,5,10,0))
input_frame.grid(sticky='EW')# 0 0
input_frame.columnconfigure(0, weight=1)

user_name_label = ttk.Label(input_frame, text='Name:')
user_name_label.grid(padx=(5,10))

user_name_entry = ttk.Entry(input_frame, width=20, textvariable=user_name)
user_name_entry.grid(column=1, row=0, padx=(5,5))
user_name_entry.focus()

buttons_frame = ttk.Frame(root_window, padding=(5,5))
buttons_frame.grid(column=0, row=1, sticky='EW')
buttons_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(1, weight=1)

greeting_button = ttk.Button(buttons_frame, text='Hello!', command=greeting)
greeting_button.grid(row=0, column=0, sticky='EW')

cancel_button = ttk.Button(buttons_frame, text= 'Cancel', command=root_window.destroy)
cancel_button.grid(row=0, column=1, sticky='EW')

tkinter.mainloop()
