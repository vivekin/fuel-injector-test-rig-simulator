#!/usr/bin/python
import serial
#import syslog
import time
from tkinter import *
import tkinter as ttk
import csv

#The following line is for serial over GPIO
port = 'COM3' 
ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino
ard.flush()

#list of options
list1=[]
with open('F:\Pydir\cars.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        list1.append(row[0])
        

root = Tk()
root.title("Serial TxRx Menu")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = StringVar(root)
carsel = StringVar()
sersnd = StringVar()
carsel.set("<nothing selectcted>")
# set the default option
tkvar.set('<Select>')

#serial send function
def sendser():
        data=carsel.get()
        data1=sersnd.get()
        if data1!="1":
            data1="2"
        print("Sending serial data: "+data)
        ard.write(data1.encode())
        
popupMenu = OptionMenu(mainframe, tkvar, *list1)

Label(mainframe, text="Choose a row").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)
Label(mainframe, textvariable = carsel).grid(row = 3, column = 1)
Button(mainframe, text ="Send", command = sendser).grid(row = 4, column = 1)



# on change dropdown value
def change_dropdown(*args):
    #print( tkvar.get() )
    with open('F:\Pydir\cars.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0]==tkvar.get():
                #print(row)
                carsel.set(row)
                sersnd.set(row[4])
                
              


# link function to change dropdown
tkvar.trace('w', change_dropdown)



root.mainloop()
