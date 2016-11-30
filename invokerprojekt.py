import sys, os
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Invoker")
#ikoonipilt
program_directory=sys.path[0]
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "icon.png")))
#suurpilt
logo = PhotoImage(file="icon.png")
label = Label(root, image=logo)
label.pack()
#menüü
button_frame = Frame(root)
button_frame.pack(fill=X, side=BOTTOM)
#ez mode
def ezMode():
    print("Siin hakkaks ezmode pihta")
ez_button = Button(button_frame, text='Ez mode', command = ezMode)

#hc mode
def hcMode():
    print("Siin hakkaks hcmode pihta")
hc_button = Button(button_frame, text='Hc mode', command = hcMode)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

ez_button.grid(row=1, column=0, sticky=W+E)
hc_button.grid(row=1, column=1, sticky=W+E)


root.mainloop() 