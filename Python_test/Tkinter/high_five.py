import tkinter
from tkinter import ttk


def greeting():
	print(f'Hi Five!!! {user_name.get()}') # don't forget to cast '.get()'!!!



root_window = tkinter.Tk()
user_name = tkinter.StringVar()

input_frame = ttk.Frame(root_window, padding=(10,5,10,0))
input_frame.pack(fill='both')

user_name_label = ttk.Label(input_frame, text='Name:')
user_name_label.pack(side='left', padx=(5,10))

user_name_entry = ttk.Entry(input_frame, width=20, textvariable=user_name)
user_name_entry.pack(side='left', padx=(5,15))
user_name_entry.focus()

buttons_frame = ttk.Frame(root_window, padding=(10,5))
buttons_frame.pack(fill='both', expand=True)

greeting_button = ttk.Button(buttons_frame, text='Hello!', command=greeting)
greeting_button.pack(side='left',fill='x', expand=True)

cancel_button = ttk.Button(buttons_frame, text= 'Cancel', command=root_window.destroy)
cancel_button.pack(side='right',fill='x', expand=True)

tkinter.mainloop()
