from tkinter import *

root=Tk()   #root is like our main form or activity

Button1=Button(None, text= "Click Me!",fg="Blue") #Button widget/control initialize
Button1.grid(row=0, column=0)

Button2=Button(None, text = "Hello!", fg="Red")
Button2.grid(row=0, column=1)

Button3=Button(None, text = "No Click me",fg = "Green")
Button3.grid(row=1, column=0)

Button4=Button(None, text = "Hello to you too", fg="Brown")
Button4.grid(column=1, row=1)
root.mainloop()
