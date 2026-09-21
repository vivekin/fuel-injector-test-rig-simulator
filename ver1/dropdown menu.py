from tkinter import *
import tkinter as ttk
import csv

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
carsel.set("<nothing selectcted>")
# set the default option
tkvar.set('<Select>')

def sendser():
        data=carsel.get()
        print("Sending serial data: "+data)  
        
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
                
              


# link function to change dropdown
tkvar.trace('w', change_dropdown)



root.mainloop()
