from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Laikrodukas")

label = Label(root, font=("Arial", 90), background="black", foreground="red")
label.pack(anchor="center")

def time():
    string = strftime(" Time: %H:%M:%S \n Date: %Y %b %d")
    label.config(text=string)
    label.after(1000, time)

time()

mainloop()
