#!/usr/bin/python
import serial
#import syslog
import time
from tkinter import *
import tkinter as ttk
import csv


#tkinter GUI window 
root = Tk()
root.title("Serial TxRx Menu")
root.configure()

# Add a grid
mainframe = Frame(root)
mainframe.configure()
#mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
#mainframe.columnconfigure(0, weight = 1)
#mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

popupMenu = OptionMenu(mainframe, "gg", ["a","b","c"])

Label(mainframe, text="Select option").grid(row = 1, column = 2)
popupMenu.grid(row = 2, column =2)
#send value

Label(mainframe, text = "part item1").grid(row = 3, column = 2)
Label(mainframe, text = "Time(us)").grid(row = 4, column = 2)
Label(mainframe, text = "Freq (Hz)").grid(row = 5, column = 2)
Label(mainframe, text = "Volt (V)").grid(row = 6, column = 2)
Label(mainframe, text = "Curr (A)").grid(row = 7, column = 2)
Label(mainframe, text = "Press (Bar)").grid(row = 8, column = 2)
Label(mainframe, text = "Volu (CC)").grid(row = 9, column = 2)

# value Fields
T1 =Text(mainframe, height=1, width=10)
T1.grid(row = 4, column = 3)
T2 =Text(mainframe, height=1, width=10).grid(row = 5, column = 3)
T3 =Text(mainframe, height=1, width=10).grid(row = 6, column = 3)
T4 =Text(mainframe, height=1, width=10).grid(row = 7, column = 3)
T5 =Text(mainframe, height=1, width=10).grid(row = 8, column = 3)
T6 =Text(mainframe, height=1, width=10).grid(row = 9, column = 3)





#adjust
#Button(mainframe, text ="usplus").grid(row = 5, column = 3)
#Button(mainframe, text ="usminus").grid(row = 6, column = 3)
#load,strat,stop buttons
Button(mainframe, text ="Load EL").grid(row = 3, column = 1)
Button(mainframe, text ="Load TL").grid(row = 4, column = 1)
Button(mainframe, text ="Load VL").grid(row = 5, column = 1)
sb=Button(mainframe, text ="START" )
sb.grid(row = 6, column = 1)
Button(mainframe, text ="STOP").grid(row = 7, column = 1)

#rx values
Label(mainframe, text = "rpmdis = 234").grid(row = 4, column = 5)
Label(mainframe, text = "predis = 3").grid(row = 5, column = 5)
Label(mainframe, text = "temdis = 24").grid(row = 6, column = 5)



T1.insert(END, "1st val") 
root.mainloop()
