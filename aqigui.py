from tkinter import Tk, Label, Button, PhotoImage

## TK Setup
root = Tk()
root.title('AQIGUI')
img = PhotoImage(file='FrameIcon.png') # Set window icon
root.tk.call('wm', 'iconphoto', root._w, img)
##################################################
## App Start!

myLabel = Label(root, text='test')
myLabel.grid(row=0, column=0)






##################################################
root.mainloop()