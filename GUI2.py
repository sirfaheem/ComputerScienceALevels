from tkinter import *

root=Tk()   #root is like our main form or activity

topFrame = Frame(root)   #organization layout
topFrame.pack(side=TOP)

botFrame=Frame(root)
botFrame.pack(side=BOTTOM)

Button1=Button(topFrame, text= "Click Me!",fg="Blue") #Button widget/control initialize
Button1.pack(side=LEFT)

Button2=Button(botFrame, text = "Hello!", fg="Red")
Button2.pack(side=LEFT)

Button3=Button(topFrame, text = "No Click me",fg = "Green")
Button3.pack(side=LEFT)

Button4=Button(botFrame, text = "Hello to you too", fg="Brown")
Button4.pack(side=RIGHT)

root.mainloop()
