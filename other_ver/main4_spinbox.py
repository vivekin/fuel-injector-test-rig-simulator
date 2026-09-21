#!/usr/bin/python
import serial
#import syslog
import time
from tkinter import *
import tkinter as ttk
import csv
from datetime import datetime

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
    T1.delete("0", END)
    T2.delete("0", END)
    T3.delete("0", END)
    T4.delete("0", END)
    T5.delete("0", END)
    T6.delete("0", END)



#load el data,enable start button
def loadel():
    part.set("part "+rowsel[0])
    setempty()
    T1.insert(END,rowsel[1])
    T2.insert(END,rowsel[2])
    T3.insert(END,rowsel[3])
    T4.insert(END,rowsel[4])
    T5.insert(END,rowsel[5])
    T6.insert(END,rowsel[6])    
    sb["state"] = NORMAL

#load tl data,enable start button
def loadtl():
    part.set("part "+rowsel[0])
    setempty()
    T1.insert(END,rowsel[7])
    T2.insert(END,rowsel[8])
    T3.insert(END,rowsel[9])
    T4.insert(END,rowsel[10])
    T5.insert(END,rowsel[11])
    T6.insert(END,rowsel[12])
    sb["state"] = NORMAL


#load vl data,enable start button
def loadvl():
    part.set("part "+rowsel[0])
    setempty()
    T1.insert(END,rowsel[13])
    T2.insert(END,rowsel[14])
    T3.insert(END,rowsel[15])
    T4.insert(END,rowsel[16])
    T5.insert(END,rowsel[17])
    T6.insert(END,rowsel[18])
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
    if ("rpm"in data and "pressure"in data and "temp"in data and "status"in data):
        rpmdis.set(data.split(',')[0]+" rpm")
        predis.set(data.split(',')[1]+" bar")
        temdis.set(data.split(',')[2].strip()+" °C")
        stadis.set(data.split(',')[3].strip())
        if ("inactive" in data.split(',')[3]):
            cb["state"] = NORMAL
            T7["state"] = NORMAL
            compare1.set("Enter volume here")
        else:
            cb["state"] = DISABLED
            T7["state"] = DISABLED
            compare1.set("")
    
        
#serial send start function
def sendstart():
        data=part.get()+",time="+T1.get("1.0", "end-1c")+",fre="+T2.get("1.0", "end-1c")+",volt="+T3.get("1.0", "end-1c")+",curr="+T4.get("1.0", "end-1c")+",press="+T5.get("1.0", "end-1c")+",volu="+T6.get("1.0", "end-1c")
        #remove this if-else, and uncomment last ard.write
        if ("1" not in T1.get("1.0", "end-1c")):
            data1="2"
            ard.write(data1.encode())
        else:
            data1="1"
            ard.write(data1.encode())
        print("Sending serial data: "+data)
        #ard.write(data.encode())
        
#serial send stop function
def compare():
    # datetime object containing current date and time
    now = datetime.now()     
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    res=""

    #compare T6.get("1.0", "end-1c") and T7.get("1.0", "end-1c")
    if int(T6.get("1.0", "end-1c"))==int(T7.get("1.0", "end-1c")):
        res=" Entered volume "+T7.get("1.0", "end-1c")+" is equal to "+T6.get("1.0", "end-1c")
    elif int(T6.get("1.0", "end-1c")) > int(T7.get("1.0", "end-1c")):
        res=" Entered volume "+T7.get("1.0", "end-1c")+" is lesser than "+T6.get("1.0", "end-1c")
    else:
        res=" Entered volume "+T7.get("1.0", "end-1c")+" is greater than "+T6.get("1.0", "end-1c")
    compare2.set(res)    
    print("Writing to log :", dt_string+res)
    f = open('F:\Pydir\\vol_logger.txt', "a")
    f.write(dt_string+ "\n")
    f.close()


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
compare1 = StringVar()
compare2 = StringVar()
rpmdis = StringVar()
predis = StringVar()
temdis = StringVar()
stadis = StringVar()
# set the default option
tkvar.set('<Select>')

popupMenu = OptionMenu(mainframe, tkvar, *list1)

Label(mainframe, text="Select option",font="none 10 bold",bg="black",fg="white").grid(row = 2, column = 2)
popupMenu.grid(row = 2, column =3)
Label(mainframe, textvariable = part,bg="black",fg="white").grid(row = 3, column = 2)
Label(mainframe, text = "Time(us)",bg="black",fg="white").grid(row = 4, column = 2)
Label(mainframe, text = "Freq (Hz)",bg="black",fg="white").grid(row = 5, column = 2)
Label(mainframe, text = "Volt (V)",bg="black",fg="white").grid(row = 6, column = 2)
Label(mainframe, text = "Curr (A)",bg="black",fg="white").grid(row = 7, column = 2)
Label(mainframe, text = "Press (Bar)",bg="black",fg="white").grid(row = 8, column = 2)
Label(mainframe, text = "Volu (CC)",bg="black",fg="white").grid(row = 9, column = 2)

# value Fields
T1 =Spinbox(mainframe,  width=10,increment=0.5)
T2 =Spinbox(mainframe,  width=10)
T3 =Spinbox(mainframe,  width=10)
T4 =Spinbox(mainframe,  width=10)
T5 =Spinbox(mainframe,  width=10)
T6 =Spinbox(mainframe,  width=10)
T1.grid(row = 4, column = 3)
T2.grid(row = 5, column = 3)
T3.grid(row = 6, column = 3)
T4.grid(row = 7, column = 3)
T5.grid(row = 8, column = 3)
T6.grid(row = 9, column = 3)

#load,start,stop buttons
Button(mainframe, text ="Load EL", command = loadel,bg="white",fg="black").grid(row = 4, column = 1)
Button(mainframe, text ="Load TL", command = loadtl,bg="white",fg="black").grid(row = 5, column = 1)
Button(mainframe, text ="Load VL", command = loadvl,bg="white",fg="black").grid(row = 6, column = 1)
sb=Button(mainframe, text ="START" ,command = sendstart,bg="white",fg="black",state=DISABLED)
sb.grid(row = 7, column = 1)
Button(mainframe, text ="STOP", command = sendstop,bg="white",fg="black").grid(row = 8, column = 1)

#rx values
Label(mainframe, textvariable = rpmdis,bg="black",fg="white").grid(row = 4, column = 5)
Label(mainframe, textvariable = predis,bg="black",fg="white").grid(row = 5, column = 5)
Label(mainframe, textvariable = temdis,bg="black",fg="white").grid(row = 6, column = 5)
Label(mainframe, textvariable = stadis,bg="black",fg="white").grid(row = 7, column = 5)

Label(mainframe, textvariable = compare1,bg="black",fg="white").grid(row = 8, column = 5)
T7 =Text(mainframe, height=1, width=10,state=DISABLED)
T7.grid(row = 9, column = 5)
cb=Button(mainframe, text ="COMPARE" ,command = compare,bg="white",fg="black",state=DISABLED)
cb.grid(row = 10, column = 5)
Label(mainframe, textvariable = compare2,bg="black",fg="white").grid(row = 11, column = 5)

# on change dropdown value
def change_dropdown(*args):
    #print( tkvar.get() )
    with open('F:\Pydir\load.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0]==tkvar.get():
                #print(row)
                part.set("")
                setempty()
                sb["state"] = DISABLED
                part.set(row[0])
                global rowsel
                rowsel=row


# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.after(1000, scan)
root.mainloop()
