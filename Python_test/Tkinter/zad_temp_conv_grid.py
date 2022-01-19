from tkinter import *
from tkinter import ttk


def celsius_to_fahrenheit(celsius):
	return celsius*1.8 + 32


def out():
	output_label['text'] = f'{celsius_to_fahrenheit(float(celsius_input.get()))}'


root_window = Tk()
root_window.title('Temperature converter')
root_window.resizable(False, False)

celsius_input = StringVar()



# input_frame = ttk.Frame(root_window, padding=(20,10,10,0))
# input_frame.grid()

celsius_label = ttk.Label(root_window, text = 'Celsius')
celsius_label.grid(sticky=W, pady=10, padx=5)

celsius_entry = ttk.Entry(root_window, width = 20, textvariable=celsius_input)
celsius_entry.grid(column=1, row=0, pady=10, padx=5)
celsius_entry.focus()
root_window.bind('<Return>', lambda e: out())

# output_frame = ttk.Frame(root_window, padding=(20,10,10,0))
# output_frame.grid()

output_label = ttk.Label(root_window, text='Temperature in fahrenheits')
output_label.grid(column=1, row=1, pady=10, padx=5)

fahrenheit_label = ttk.Label(root_window, text='Farenheit')
fahrenheit_label.grid(column=0, row=1, sticky=W, pady=10, padx=5)

# buttons_frame = ttk.Frame(root_window, padding=(10,10,10,20))
# buttons_frame.grid()

fahrenheit_button = Button(root_window, text= 'Convert', command=out)
fahrenheit_button.grid(row=2, columnspan=2, pady=10, padx=5)


root_window.mainloop()
