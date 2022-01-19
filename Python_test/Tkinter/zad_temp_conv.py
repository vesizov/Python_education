from tkinter import *
from tkinter import ttk


def celsius_to_fahrenheit(celsius):
	return celsius*1.8 + 32


def out():
	output_label['text'] = f'{celsius_to_fahrenheit(float(celsius_input.get())):.2f}'


root_window = Tk()
root_window.title('Temperature converter')

celsius_input = StringVar()



input_frame = ttk.Frame(root_window, padding=(20,10,10,0))
input_frame.pack(fill = 'both')


celsius_label = ttk.Label(input_frame, text = 'Celsius')
celsius_label.pack(side='left', padx=(5,10))

celsius_entry = ttk.Entry(input_frame, width = 20, textvariable=celsius_input)
celsius_entry.pack(side='right', padx=(10,5))
celsius_entry.focus()
root_window.bind('<Return>', lambda e: out())

output_frame = ttk.Frame(root_window, padding=(20,10,10,0))
output_frame.pack(fill='both')

output_label = ttk.Label(output_frame, text='Temperature in fahrenheits')
output_label.pack(side='right', padx=(10,5))

fahrenheit_label = ttk.Label(output_frame, text='Farenheit')
fahrenheit_label.pack(side='left', padx=(5,10))

buttons_frame = ttk.Frame(root_window, padding=(10,10,10,20))
buttons_frame.pack(fill='both')

fahrenheit_button = Button(buttons_frame, text= 'Convert', command=out)
fahrenheit_button.pack(fill='x', side='bottom')


root_window.mainloop()