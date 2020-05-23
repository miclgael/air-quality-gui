from tkinter import *
from tkinter import Tk, ttk

## TK Setup
root = Tk()
root.title('AQI GUI')
root.columnconfigure(0, weight=1) # for each pixel, increase frame by 1
root.rowconfigure(0, weight=1) # for each pixel, increase frame size by 1
root.geometry("960x230")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)
frame.configure(borderwidth=2)

frame['relief'] = 'groove'

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
o_label = ttk.Label(frame, background='yellow')
o_label.grid(column=1,row=1, sticky='E')

s_label = ttk.Label(frame, background='red')
s_label.grid(column=1, row=2, sticky='E')

p_label = ttk.Label(frame, background='blue')
p_label.grid(column=1, row=3, sticky='E')

o_label['text'] = "Ozone: "
s_label['text'] = "Sulfur Dioxide: "
p_label['text'] = "Particles less than 2.5 micrometer diameter: "


## Column 2 Items
o_var = StringVar()
o_entry = ttk.Entry(frame,textvariable=o_var)
o_entry.grid(column=2, row=1)

s_var = StringVar()
s_entry = ttk.Entry(frame,textvariable=s_var)
s_entry.grid(row=2, column=2)

p_var = StringVar()
p_entry = ttk.Entry(frame,textvariable=p_var)
p_entry.grid(column=2, row=3)

c_button = ttk.Button(frame, text = "Calculate AQI", command=calculate_AQI)
c_button.grid(column=2, row=4)

### Status label
st_label = ttk.Label(frame, text=" ", foreground="red", width=45)
st_label.grid(column=2, row=5, sticky='N,S,E,W')

r_label = ttk.Label(frame, text="AQI: ")
r_label.grid(column=2, row=6) 

## Column 3 Items

o_after_label = ttk.Label(frame)
o_after_label.grid(column=3,row=1, sticky='W')

s_after_label = ttk.Label(frame)
s_after_label.grid(column=3,row=2, sticky='W')

p_after_label = ttk.Label(frame)
p_after_label.grid(column=3,row=3, sticky='W')

o_after_label['text'] = "parts per hundred million"
s_after_label['text'] = "parts per hundred million"
p_after_label['text'] = "micrograms per cubic metre"



o_entry.focus()

# Add space between cells
for child in frame.winfo_children():
    child.grid_configure(padx=5,pady=5)

# Make elastic col/rows
for i in range(1, 3):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i + i, weight=1)

##################################################
root.bind('<Return>',calculate_AQI)



def window_size(e):
    print(e.width)

    o_label['text'] = "O\u2083  " if e.width <= 600 else "Ozone: "
    s_label['text'] = "SO\u2082 " if e.width <= 600 else "Sulfur Dioxide: "
    p_label['text'] = "Particles < 2.5μm: " if e.width <= 600 else "Particles less than 2.5 micrometer diameter: "


    o_after_label['text'] = "parts per 100m" if e.width <= 600 else "parts per hundred million"
    s_after_label['text'] = "parts per 100m" if e.width <= 600 else "parts per hundred million"
    p_after_label['text'] = "μg per M\u00b3" if e.width <= 600 else  "micrograms per cubic metre"
 


print("O\u2083")
print("SO\u2082") 

frame.bind('<Configure>', window_size)


root.mainloop()
