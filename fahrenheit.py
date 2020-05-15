from tkinter import * 
from tkinter import ttk

### The * means any number of arguments
def calculate(*args):
    try:
        value = float(fahrenheit.get()) # fh will be the text box
        celsius.set((value - 32) * (5/9)) # celcius will be a result box i assume
    except ValueError:
        print('nah bitch, type a number.')
        pass # Ignore for now

root = Tk()
root.title("Fahrenheit to Celsius")
####

frame = ttk.Frame(root, padding='3 3 12 12')
frame.grid(column=0, row=0, sticky=(N,S,E,W))
root.columnconfigure(0, weight=1) # for each pixel, increase frame by 1
root.rowconfigure(0, weight=1) # for each pixel, increase frame size by 1

for col in range(1, 4):
    frame.columnconfigure(col, weight=1)
    
for row in range(1, 4):
    frame.rowconfigure(row, weight=1)



fahrenheit = StringVar()
celsius = StringVar()

f_entry = Entry(frame, width=7, textvariable=fahrenheit)
f_entry.grid(column=2, row=1, sticky=(W,E))

c_label = ttk.Label(frame, textvariable=celsius)
c_label.grid(column=2, row=2, sticky=(W,E))

g_button = ttk.Button(frame, text="Go", command=calculate)
g_button.grid(column=3, row=3, sticky=(W))

f_label = ttk.Label(frame, text="degrees F")
f_label.grid(column=3, row=1, sticky=(W))

e_label = ttk.Label(frame, text="is equivalent to")
e_label.grid(column=1, row=2, sticky=(E))

d_label = ttk.Label(frame, text="degrees C")
d_label.grid(column=3, row=2, sticky=(W))

for child in frame.winfo_children():
    child.grid_configure(padx=5,pady=5)

f_entry.focus()
root.bind("<Return>", calculate)

####
root.mainloop()
