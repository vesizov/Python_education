from tkinter import *
from tkinter import font

root_window = Tk()

root_window.geometry('500x500')
root_window.title('Hello World!')


# Create widget (Label in this case)
hello_label = Label(root_window, text='Hello my friend, i\'ve been waiting for a long time!', font=('Verdana', 17, 'italic'))#, bg='#10a0bc', fg='#12ebd2',
	# relief='groove') #solid, flat, raised, sunken, ridge, groove

# print(font.families())
# Put the widget on the root window
hello_label.pack()

version_label = Label(root_window, text=f'Tk version is {TkVersion}')
version_label.place(x=390,y=475)

go_button = Button(root_window, text=f'Do it!', relief=RAISED) #highlightbackground = 'darkgreen'
go_button.pack()



root_window.mainloop()

