# importing everything from tkinter 
from tkinter import *

# create gui window 
Main_window = Tk() 

# set the configuration 
# of the window 
Main_window.geometry("220x100") 

# define a function 
# for setting the new text 
def java(): 
	my_string_var.set("You must go with Java") 

# define a function 
# for setting the new text 
def python(): 
	my_string_var.set("You must go with Python") 



# create a Button widget and attached 
# with java function 
btn_1 = Button(Main_window, 
			text = "I love Android", 
			command = java) 

# create a Button widget and attached 
# with python function 
btn_2 = Button(Main_window, 
			text = "I love Machine Learning", 
			command = python) 

# create a StringVar class 
my_string_var = StringVar() 

# set the text 
my_string_var.set("What should I learn") 

# create a label widget 
my_label = Label(Main_window, 
				textvariable = my_string_var) 


# place widgets into 
# the gui window 
btn_1.pack() 
btn_2.pack() 
my_label.pack() 

# Start the GUI 
Main_window.mainloop()
