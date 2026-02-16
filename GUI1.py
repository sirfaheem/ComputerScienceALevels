from tkinter import *

root=Tk()   #root is like our main form or activity

label1 = Label(root, text = "Name: ") #this is a label
label1.grid(row=0, column=0)        #position of the lable
entrySpace=Entry(root)      #textbox    
entrySpace.grid(row=0, column=1)    #position of textbox

root.mainloop()
