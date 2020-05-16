from tkinter import *
from tkinter import Tk, ttk

## TK Setup
root = Tk()
root.title('AQI GUI')
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)
frame.configure(borderwidth=2)
# frame.configure(relief="solid")
frame['relief'] = 'groove'

##################################################
## App Start!

## Functions

def calculate_AQI(*args):
    """Returns the highest calculated result of the given List
    
    Returns:
        {float} -- Highest result _after_ calculation
    """
    global s_entry, o_entry, p_entry, AQI

    readings = [
        o_entry.get(),
        s_entry.get(),
        p_entry.get()
    ]

    # Immutable Tuple
    standards = (
        8.0,  # Ozone
        20,  # Sulfur Dioxide
        25,  # Particles
    )

    # List for storing results
    calculated = []

    for count,reading in enumerate(readings):
        print(count,reading)
        # Push calculations onto the List
        # NOTE: Algorithm provided by Dr. David Paul
        calculated.append((100 * float(readings[count])) / float(standards[count]))
    calculated.sort(reverse=True)  # Reorder the List from highest to lowest values

    AQI = calculated[0] 
    print('AQI: ', AQI)
    return calculated[0]  # Highest value    for reading in range(0, len(readings)):

AQI = 125.00

## Column 1 Items
o_label = ttk.Label(frame, text="Ozone: ")
o_label.grid(column=1,row=1, sticky='E')

s_label = ttk.Label(frame, text="Sulfur dioxide: ")
s_label.grid(column=1,row=2, sticky='E')

p_label = ttk.Label(frame, text="Particles less than 2.5 micrometer diameter: ")
p_label.grid(column=1,row=3, sticky='E')


## Column 2 Items
o_var = StringVar()
o_entry = ttk.Entry(frame,textvariable=o_var)
o_entry.grid(column=2,row=1, sticky='N,S,E,W')

s_var = StringVar()
s_entry = ttk.Entry(frame,textvariable=s_var)
s_entry.grid(row=2,column=2, sticky='N,S,E,W')

p_var = StringVar()
p_entry = ttk.Entry(frame,textvariable=p_var)
p_entry.grid(column=2,row=3, sticky='N,S,E,W')

c_button = ttk.Button(frame, text = "Calculate AQI", command=calculate_AQI)
c_button.grid(column=2,row=4)

### Status label
s_label = ttk.Label(frame,text="Error: nothing entered",foreground="red")
s_label.grid(column=2,row=5, sticky='N,S,E,W')

r_label = ttk.Label(frame, text="AQI: {}".format(calculate_AQI))
r_label.grid(column=2,row=6)

## Column 3 Items

o_after_label = ttk.Label(frame, text="parts per hundred million")
o_after_label.grid(column=3,row=1, sticky='W')

s_after_label = ttk.Label(frame, text="parts per hundred mi+llion")
s_after_label.grid(column=3,row=2, sticky='W')

p_after_label = ttk.Label(frame, text="micrograms per cubic metre")
p_after_label.grid(column=3,row=3, sticky='W')


o_label.focus()


##################################################
root.mainloop()