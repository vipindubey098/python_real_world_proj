#import python modules like tkinter //sudo apt-get install python3.10-tk
from tkinter import *
from time import strftime

#creating an object
root = Tk() #this will create a window to display
root.title('Digital Clock') #shows title of popup

# label = Label(root, font=("areal", 160, "bold"), bg='black', fg="white").pack(anchor="center", fill="both", expand=1) # fg = foreground color

# we can use down one too
label = Label(root, font=("areal", 160, "bold"), bg='black', fg="white")
label.pack(anchor="center", fill="both", expand=1) # fg = foreground color

def Time():
    string = strftime("%H:%M:%S P")
    label.config(text=string)
    label.after(1000, Time) #will update every 1000 milisecond

Time()
root.mainloop() #it will help to control tkinter windows. Important for tkinter