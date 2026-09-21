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

rowsel=[]
list1=[]

#list of options
with open('F:\Pydir\load.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        list1.append(row[0])
        
#remove heading line from dropdown list
list1.pop(0)       


#set selection data empty, to clear values of previous selection
def setempty():
    part.set("")
    us.set("")
    freq.set("")
    volt.set("")
    curr.set("")
    press.set("")
    volu.set("")


#load el data,enable start button
def loadel():
    part.set("part "+rowsel[0])
    us.set("us "+rowsel[1])
    freq.set("freq "+rowsel[2])
    volt.set("volt "+rowsel[3])
    curr.set("current "+rowsel[4])
    press.set("pressure "+rowsel[5])
    volu.set("volume "+rowsel[6])
    sb["state"] = NORMAL

#load tl data,enable start button
def loadtl():
    part.set("part "+rowsel[0])
    us.set("us "+rowsel[7])
    freq.set("freq "+rowsel[8])
    volt.set("volt "+rowsel[9])
    curr.set("current "+rowsel[10])
    press.set("pressure "+rowsel[11])
    volu.set("volume "+rowsel[12])
    sb["state"] = NORMAL


#load vl data,enable start button
def loadvl():
    part.set("part "+rowsel[0])
    us.set("us "+rowsel[13])
    freq.set("freq "+rowsel[14])
    volt.set("volt "+rowsel[15])
    curr.set("current "+rowsel[16])
    press.set("pressure "+rowsel[17])
    volu.set("volume "+rowsel[18])
    sb["state"] = NORMAL

#receive serial data    
def scan():
    data_raw = ard.readline()
    print(data_raw.decode())
    rxdis(data_raw.decode())
    root.after(50, scan)
    root.update_idletasks()
        
#to split received serial data
def rxdis(data):
    if ("rpm"in data and "pressure"in data and "temp"in data):
        rpmdis.set(data.split(',')[0]+" rpm")
        predis.set(data.split(',')[1]+" bar")
        temdis.set(data.split(',')[2].strip()+" °C")
    
        
#serial send start function
def sendstart():
        data=part.get()+","+us.get()+","+freq.get()+","+volt.get()+","+curr.get()+","+press.get()+","+volu.get()
        #remove this if-else, and uncomment last ard.write
        if ("1" not in us.get()):
            data1="2"
            ard.write(data1.encode())
        else:
            data1="1"
            ard.write(data1.encode())
        print("Sending serial data: "+data)
        #ard.write(data.encode())
        
#serial send stop function
def sendstop():
        print("Sending STOP")
        stopvar="STOP"
        ard.write(stopvar.encode())

        
#tkinter GUI window 
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
tkvar = StringVar()
part = StringVar()
us = StringVar()
freq = StringVar()
volt = StringVar()
curr = StringVar()
press = StringVar()
volu = StringVar()
sersnd = StringVar()
rpmdis = StringVar()
predis = StringVar()
temdis = StringVar()
# set the default option
tkvar.set('<Select>')

popupMenu = OptionMenu(mainframe, tkvar, *list1)

Label(mainframe, text="Select option",font="none 10 bold",bg="black",fg="white").grid(row = 1, column = 2)
popupMenu.grid(row = 2, column =2)
Label(mainframe, textvariable = part,bg="black",fg="white").grid(row = 3, column = 2)
Label(mainframe, textvariable = us,bg="black",fg="white").grid(row = 4, column = 2)
Label(mainframe, textvariable = freq,bg="black",fg="white").grid(row = 5, column = 2)
Label(mainframe, textvariable = volt,bg="black",fg="white").grid(row = 6, column = 2)
Label(mainframe, textvariable = curr,bg="black",fg="white").grid(row = 7, column = 2)
Label(mainframe, textvariable = press,bg="black",fg="white").grid(row = 8, column = 2)
Label(mainframe, textvariable = volu,bg="black",fg="white").grid(row = 9, column = 2)
#load,strat,stop buttons
Button(mainframe, text ="Load EL", command = loadel,bg="white",fg="black").grid(row = 3, column = 1)
Button(mainframe, text ="Load TL", command = loadtl,bg="white",fg="black").grid(row = 4, column = 1)
Button(mainframe, text ="Load VL", command = loadvl,bg="white",fg="black").grid(row = 5, column = 1)
sb=Button(mainframe, text ="START" ,command = sendstart,bg="white",fg="black",state=DISABLED)
sb.grid(row = 6, column = 1)
Button(mainframe, text ="STOP", command = sendstop,bg="white",fg="black").grid(row = 7, column = 1)

#rx values
Label(mainframe, textvariable = rpmdis,bg="black",fg="white").grid(row = 4, column = 3)
Label(mainframe, textvariable = predis, height=2,bg="black",fg="white").grid(row = 5, column = 3)
Label(mainframe, textvariable = temdis,bg="black",fg="white").grid(row = 6, column = 3)



# on change dropdown value
def change_dropdown(*args):
    #print( tkvar.get() )
    with open('F:\Pydir\load.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0]==tkvar.get():
                #print(row)
                setempty()
                sb["state"] = DISABLED
                part.set(row[0])
                global rowsel
                rowsel=row


# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.after(1000, scan)
root.mainloop()
