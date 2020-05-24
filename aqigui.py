from tkinter import *
from tkinter import Tk, ttk
import operator

## TK Setup
root = Tk()
root.title('AQI GUI')
root.columnconfigure(0, weight=1) # for each pixel, increase frame by 1
root.rowconfigure(0, weight=1) # for each pixel, increase frame size by 1
# root.geometry('900x400')
root.config(bg='#f3fcf0')

# https://coolors.co/540d6e-ee4266-ffd23f-f3fcf0-1f271b

# s = ttk.Style()
# s.configure('bg.TFrame', background='#1F271B'), style='bg.TFrame'

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0)
frame.configure(borderwidth=2)

frame['relief'] = 'groove'

def frame_size(e):
    if e.width <= 650:
        # print('FS', e.width, 550, '<=') ## <- Debug!
        responsive_labels(e, 550, operator.lt)
 
def window_size(e):
    if e.width > 650:
        # print('WS', e.width, 550, '<=') ## <- Debug!
        responsive_labels(e, 550, operator.lt)

def responsive_labels(e, breakpoint, relate):
    bp = relate(e.width, breakpoint)
    # print(bp)
    ## Before Labels
    o_label['text'] = "O\u2083  " if bp else "Ozone: "
    s_label['text'] = "SO\u2082 " if bp else "Sulfur Dioxide: "
    p_label['text'] = "Particles < 2.5μm: " if bp else "Particles less than 2.5 micrometer diameter: "

    ## After Labels
    o_after_label['text'] = "parts/100m" if bp else "parts per hundred million"
    s_after_label['text'] = "parts/100m" if bp else "parts per hundred million"
    p_after_label['text'] = "μg per M\u00b3" if bp else "micrograms per cubic metre"

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
        st_label['text'] = '' # Clear the error label (no error!)
    except ValueError:
        st_label['text'] = 'Please check input values!'
        r_label['text'] = 'AQI: Error!'

## Column 1 Items
o_label = ttk.Label(frame, background='#FFD23F', foreground="#1F271B")
o_label.grid(column=1, row=1, sticky='E')

s_label = ttk.Label(frame, background='#EE4266', foreground="#F3FCF0")
s_label.grid(column=1, row=2, sticky='E')

p_label = Message(frame, background='#540D6E', foreground="#F3FCF0", width=200)
p_label.grid(column=1, row=3, sticky='E')

o_label['text'] = "Ozone: "
s_label['text'] = "Sulfur Dioxide: "
p_label['text'] = "Particles less than 2.5 micrometer diameter: "


## Column 2 Items
o_var = StringVar()
o_entry = ttk.Entry(frame, textvariable=o_var)
o_entry.grid(column=2, row=1, sticky='N,S,E,W')

s_var = StringVar()
s_entry = ttk.Entry(frame, textvariable=s_var)
s_entry.grid(column=2, row=2, sticky='N,S,E,W')

p_var = StringVar()
p_entry = ttk.Entry(frame, textvariable=p_var)
p_entry.grid(column=2, row=3, sticky='N,S,E,W')

## Button
c_button = ttk.Button(frame, text = "Calculate AQI", command=calculate_AQI)
c_button.grid(column=2, row=4, sticky="N,S,E,W")

### Status label
st_label = ttk.Label(frame, text=" ", foreground="#EE4266", anchor='center')
st_label.grid(column=2, row=5, sticky='N,S,E,W')

## Result Label
r_label = ttk.Label(frame, text="AQI: ", anchor='center')
r_label.grid(column=2, row=6, sticky="N,S,E,W") 

## Column 3 Items
o_after_label = ttk.Label(frame)
o_after_label.grid(column=3, row=1, sticky='N,S,E,W')

s_after_label = ttk.Label(frame)
s_after_label.grid(column=3, row=2, sticky='N,S,E,W')

p_after_label = ttk.Label(frame)
p_after_label.grid(column=3, row=3)

## Spacer Item
o_after_label['text'] = "parts per hundred million"
s_after_label['text'] = "parts per hundred million"
p_after_label['text'] = "micrograms per cubic metre"

o_entry.focus()

# Add space between cells
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Make elastic col/rows
for col in range(1, 3):
    frame.columnconfigure(col, weight=1) #, minsize=225

for row in range(1, 6):
    frame.rowconfigure(row, weight=1)

##################################################
frame.bind('<Configure>', frame_size)
root.bind('<Configure>', window_size)
root.bind('<Return>', calculate_AQI)

root.mainloop()
