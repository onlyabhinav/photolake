
from tkinter import *

root = Tk()

myLabel1 = Label(root, text= "Hello World")
myLabel2 = Label(root, text= "This is Abhinav")

#myLabel1.pack()
#myLabel2.pack()

myLabel1.grid(row=0,column=1)
myLabel2.grid(row=1,column=2)
myLabel1.grid(row=3,column=6)
myLabel2.grid(row=1,column=4)




root.mainloop()