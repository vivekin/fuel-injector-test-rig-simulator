import tkinter as tk

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

#frame = tk.Frame(root)
#root.grid(row=1, column=0, sticky='nsew')

##for i in range(3):
##    root.columnconfigure(i, weight=1)
##
##root.rowconfigure(1, weight=1)

tk.Label(root, text='Title centered').grid(row=0, column=0)
tk.Label(root, text='Top left').grid(row=0, column=0, sticky='w')
tk.Label(root, text='Top center').grid(row=0, column=1)
tk.Label(root, text='Top right').grid(row=0, column=2, sticky='e')
tk.Label(root, text='Center').grid(row=1, column=1)
tk.Label(root, text='Bottom left').grid(row=2, column=0, sticky='w')
tk.Label(root, text='Bottom center').grid(row=2, column=1)
tk.Label(root, text='Bottom right').grid(row=2, column=2, sticky='e')
tk.Label(root, text='Footer centered').grid(row=2, column=0)
root.mainloop()
