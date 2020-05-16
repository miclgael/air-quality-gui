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
    global s_entry, o_entry, p_entry

    try:
        readings = [
            float(o_entry.get()),
            float(s_entry.get()),
            float(p_entry.get())
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
            calculated.append((100 * readings[count]) / standards[count])           
            calculated.sort(reverse = True)  # Reorder the List from highest to lowest values

        r_label['text'] = 'AQI: {0}'.format(calculated[0])
        s_label['text'] = '' # Clear the error label (no error!)
    except ValueError:
        s_label['text'] = 'VALUE ERROR: Please ensure values are numbers!'
        r_label['text'] = 'AQI: '

## Column 1 Items
o_label = ttk.Label(frame, text="Ozone: ")
o_label.grid(column=1,row=1, sticky='E')

s_label = ttk.Label(frame, text="Sulfur dioxide: ")
s_label.grid(column=1, row=2, sticky='E')

p_label = ttk.Label(frame, text="Particles less than 2.5 micrometer diameter: ")
p_label.grid(column=1, row=3, sticky='E')


## Column 2 Items
o_var = StringVar()
o_entry = ttk.Entry(frame,textvariable=o_var)
o_entry.grid(column=2, row=1, sticky='N,S,E,W')

s_var = StringVar()
s_entry = ttk.Entry(frame,textvariable=s_var)
s_entry.grid(row=2, column=2, sticky='N,S,E,W')

p_var = StringVar()
p_entry = ttk.Entry(frame,textvariable=p_var)
p_entry.grid(column=2, row=3, sticky='N,S,E,W')

c_button = ttk.Button(frame, text = "Calculate AQI", command=calculate_AQI)
c_button.grid(column=2, row=4)

### Status label
s_label = ttk.Label(frame, text=" ", foreground="red", width=45)
s_label.grid(column=2, row=5, sticky='N,S,E,W')

r_label = ttk.Label(frame, text="AQI: ")
r_label.grid(column=2, row=6) 

## Column 3 Items

o_after_label = ttk.Label(frame, text="parts per hundred million")
o_after_label.grid(column=3,row=1, sticky='W')

s_after_label = ttk.Label(frame, text="parts per hundred million")
s_after_label.grid(column=3,row=2, sticky='W')

p_after_label = ttk.Label(frame, text="micrograms per cubic metre")
p_after_label.grid(column=3,row=3, sticky='W')


o_entry.focus()


##################################################
root.bind('<Return>',calculate_AQI)
root.mainloop()