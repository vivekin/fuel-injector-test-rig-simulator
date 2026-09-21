from tkinter import *

yourData = "My text here"

root = Tk()
frame = Frame(root, width=100, height=100)
frame.pack()

lab = Label(frame,text=yourData)
lab.pack()

root.mainloop()
