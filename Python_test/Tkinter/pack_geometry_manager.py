from tkinter import *

main_window = Tk()
# main_window.geometry('400x600+2000+70') #+X+Y 
main_window.title('Second try')

# my_label =Label(main_window, text='My text', bg = 'Black')
# my_label.pack(fill=Y, expand=1)#X, Y, BOTH - uppercase only


# red_label =Label(main_window, text='Red', bg='Red', fg='black')
# red_label.pack(fill=BOTH, expand=1, padx=10)

# yellow_label =Label(main_window, text='Yellow', bg ='Yellow', fg='green')
# yellow_label.pack(fill=BOTH, expand=1, pady=10)

# green_label =Label(main_window, text='Green', bg ='Green', fg='yellow')
# green_label.pack(fill=BOTH, expand=1, padx=10, pady=10)

# listbox = Listbox(main_window)
# listbox.pack(fill=BOTH, expand=1)

# for i in range(20):
# 	listbox.insert(END,i)# str(i)

red_label =Label(main_window, text='Red', bg='Red', fg='black')
red_label.pack(ipadx=30, side = LEFT)#RIGHT if backwards!!!

yellow_label =Label(main_window, text='Yellow', bg ='Yellow', fg='green')
yellow_label.pack(ipady=30, side = LEFT)#RIGHT if backwards!!!

green_label =Label(main_window, text='Green', bg ='Green', fg='yellow')
green_label.pack(side = LEFT)#RIGHT if backwards!!!

main_window.mainloop()