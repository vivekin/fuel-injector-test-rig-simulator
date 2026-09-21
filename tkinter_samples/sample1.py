import tkinter
def serialSend():
   print( "Sending through Serial port...")
window = tkinter.Tk()
B = tkinter.Button(window, text ="Send", command = serialSend)
B.pack()
text = Text(window)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()
window.mainloop()


