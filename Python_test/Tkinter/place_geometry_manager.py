from tkinter import *

# Put one widget in inother
root = Tk()
root.title('Thirdone')
root.geometry('500x300+100+100')

# red_label =Label(root, text='Red', bg='Red', fg='black')
# red_label.place(x=150, y=250, width=200)

# yellow_label =Label(root, text='Yellow', bg ='Yellow', fg='green')
# yellow_label.place(x=175, y=130, width=150, height=40)

# green_label =Label(root, text='Green', bg ='Green', fg='yellow')
# green_label.place(x=100, y=135, height=30)





# red_label_rel_height =Label(root, text='Red relheight=0.3', bg='Red', fg='black')
# red_label_rel_height.place(relheight=0.3)

# yellow_label_rel_width =Label(root, text='Yellow relwidth=0.7', bg ='Yellow', fg='green')
# yellow_label_rel_width.place(relwidth=0.7)

# green_label_rel_x =Label(root, text='Green rel_x', bg ='Green', fg='yellow')
# green_label_rel_x.place(relx=0.2)

# blue_label_rel_y =Label(root, text='Blue rel_y', bg ='Blue', fg='Red')
# blue_label_rel_y.place(rely=0.4)


label = Label(root, text='Some Text', bg ='Green', fg='yellow')
label.place(width=400, height=100, x=50, y=100)
button=Button(root,text='Some Button')
button.place(in_=label, relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()