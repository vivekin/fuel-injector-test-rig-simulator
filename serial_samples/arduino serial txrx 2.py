#!/usr/bin/python
import serial
#import syslog
import time
from tkinter import *
import tkinter as ttk


#The following line is for serial over GPIO
port = 'COM3' 
ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino
ard.flush()

root = Tk()
root.title("Serial TxRx Menu")
root.configure(background="black")

# Add a grid
mainframe = Frame(root)
mainframe.configure(background="black")
#mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
#mainframe.columnconfigure(0, weight = 1)
#mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = StringVar(root)
carsel = StringVar()
sersnd = StringVar()
serrx = StringVar()
#carsel.set("<enter value>")
# set the default option
tkvar.set('<Select>')

#serial send function
def sendser():
        data=carsel.get()
        if data!="1":
            data="2"
        print("Sending serial data: "+data)
        ard.write(data.encode())
        
def scan():
    data_raw = ard.readline()
    print(data_raw.decode())
    serrx.set(data_raw.decode())
    root.after(50, scan)
    root.update_idletasks()

Label(mainframe, text="Select option",font="none 10 bold",bg="black",fg="white").grid(row = 1, column = 1)
Entry(mainframe, textvariable = carsel,bg="black",fg="white").grid(row = 2, column = 1)
Label(mainframe, textvariable = carsel,bg="black",fg="white").grid(row = 3, column = 1)
Button(mainframe, text ="Send", command = sendser,bg="white",fg="black").grid(row = 4, column = 1)
Label(mainframe, textvariable = serrx,bg="black",fg="white").grid(row = 6, column = 1,sticky=S)
              
              
    
root.after(1000, scan)
root.mainloop()
