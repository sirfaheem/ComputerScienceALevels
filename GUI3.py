from tkinter import *

root=Tk()   #root is like our main form or activity

Button1=Button(None, text= "Click Me!",fg="Blue") #Button widget/control initialize
Button1.pack()

Button2=Button(None, text = "Hello!", fg="Red")
Button2.pack()

Button3=Button(None, text = "No Click me",fg = "Green")
Button3.pack(fill=X) #fill the space horizontally when resizing

Button4=Button(None, text = "Hello to you too", fg="Brown")
Button4.pack(side=RIGHT, fill=Y) #fill the entire vertical space
root.mainloop()
