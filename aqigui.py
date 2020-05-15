from tkinter import *
from tkinter import ttk

## TK Setup
root = Tk()
root.title('AQI GUI')
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

##################################################
## App Start!

## Functions

def calculate_aqi():
    return

AQI = 125.00

## Column 1 Items

o_label=ttk.Label(frame, text="Ozone: ")
o_label.grid(column=1,row=1, sticky=(E))

s_label=ttk.Label(frame, text="Sulfur dioxide: ")
s_label.grid(column=1,row=2, sticky=(E))

p_label=ttk.Label(frame, text="Particles less than 2.5 micrometer diameter: ")
p_label.grid(column=1,row=3, sticky=(E))


## Column 2 Items


o_label=ttk.Entry(frame)
o_label.grid(column=2,row=1, sticky=(W))

s_label=ttk.Entry(frame)
s_label.grid(column=2,row=2, sticky=(W))
 
p_label=ttk.Entry(frame)
p_label.grid(column=2,row=3, sticky=(W))

c_button=ttk.Button(frame,text="Calculate AQI",command=calculate_aqi)
c_button.grid(column=2,row=4)

 
## Status label
s_label=ttk.Label(frame,text="Error: nothing entered",foreground="red")
s_label.grid(column=2,row=5, sticky=(N,E,S,W))

r_label=ttk.Label(frame, text="AQI: {}".format(AQI))
r_label.grid(column=2,row=6)

## Column 3 Items

o_after_label=ttk.Label(frame, text="parts per hundred million")
o_after_label.grid(column=3,row=1, sticky=(E))

s_after_label=ttk.Label(frame, text="parts per hundred million")
s_after_label.grid(column=3,row=2, sticky=(E))

p_after_label=ttk.Label(frame, text="micrograms per cubic metre")
p_after_label.grid(column=3,row=3, sticky=(E))





##################################################
root.mainloop()