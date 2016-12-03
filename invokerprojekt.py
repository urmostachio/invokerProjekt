import sys, os
from tkinter import *
from tkinter import ttk
from random import choice

def keyboardHändler(event):
    global stack
    if event.char in "qwe":
        stack[0], stack[1] = stack[1], stack[2]
        stack[2] = event.char
        uuendaStacki()
    elif event.char == "r":
        kontrolliSpelli()

def kontrolliSpelli():
    global spell_stack, skoor
    spell = "".join(sorted(stack))
    if spell == spell_stack[0]:
        spell_stack[0], spell_stack[1] = spell_stack[1], spell_stack[2]
        spell_stack[2] = annaUusSpell()
        uuendaSpelliStacki()
        skoor += 1

def annaUusSpell():
    global spell_stack
    while True:
        spell = "".join(sorted(choice("qwe") + choice("qwe") + choice("qwe")))
        if not spell in spell_stack:
            return spell

def uuendaStacki():
    global stack, aken
    l1 = Label(aken, image=PILDID[stack[0]], padx=20)
    l2 = Label(aken, image=PILDID[stack[1]], padx=20)
    l3 = Label(aken, image=PILDID[stack[2]], padx=20)
    l1.grid(row=1, column=0)
    l2.grid(row=1, column=1)
    l3.grid(row=1, column=2)
    aken.pack()

def uuendaSpelliStacki():
    global aken, spell_stack
    l1 = Label(aken, image=SPELLI_PILDID[spell_stack[0]], padx=20)
    l2 = Label(aken, image=SPELLI_PILDID[spell_stack[1]], padx=20)
    l3 = Label(aken, image=SPELLI_PILDID[spell_stack[2]], padx=20)
    l1.grid(row=2, column=0)
    l2.grid(row=2, column=1)
    l3.grid(row=2, column=2)
    aken.pack()

def teeMängulaud():
    global spell_stack, skoor, aeg
    skoor = 0
    label.pack_forget()
    uuendaStacki()
    spell_stack[0] = annaUusSpell()
    spell_stack[1] = annaUusSpell()
    spell_stack[2] = annaUusSpell()
    uuendaSpelliStacki()

def timer():
    global aken, aeg
    aeg -= 1
    if aeg != 0:
        l1 = Label(aken, text="Skoor: %i\nAega veel %is" % (skoor, aeg))
        root.after(1000, timer)
    else:
        l1 = Label(aken, text="MÄNG LÄBI!\nSaid %i punkti!" % skoor)
    l1.grid(row=0, column=1)
    aken.pack()
    
root = Tk()
root.title("Invoker")

TÜHI_IMG = PhotoImage(file="tyhi.png")
TÜHI = "tühi"
PILDID = {"q": PhotoImage(file="quas.png"),
              "w": PhotoImage(file="wex.png"),
              "e": PhotoImage(file="exort.png"),
              TÜHI: TÜHI_IMG}
SPELLI_PILDID = {TÜHI: TÜHI_IMG,
                 "eew": PhotoImage(file="Chaos_Meteor.png"),
                 "qqw": PhotoImage(file="Ghost_Walk.png"),
                 "www": PhotoImage(file="EMP.png"),
                 "eee": PhotoImage(file="Sun_Strike.png"),
                 "eqq": PhotoImage(file="Ice_Wall.png"),
                 "eeq": PhotoImage(file="Forge_Spirit.png"),
                 "qww": PhotoImage(file="Tornado.png"),
                 "eqw": PhotoImage(file="Deafening_Blast.png"),
                 "qqq": PhotoImage(file="Cold_Snap.png"),
                 "eww": PhotoImage(file="Alacrity.png")}
aken = Frame(root, padx=20, pady=20)

stack = [TÜHI, TÜHI, TÜHI]
spell_stack = [TÜHI, TÜHI, TÜHI]
skoor = 0
aeg = 11

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
    teeMängulaud()

ez_button = Button(button_frame, text='Ez mode', command = ezMode)

#hc mode
def hcMode():
    global aeg
    teeMängulaud()
    aeg = 60 #sekundit
    timer()
    
hc_button = Button(button_frame, text='Hc mode (timed)', command = hcMode)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

ez_button.grid(row=1, column=0, sticky=W+E)
hc_button.grid(row=1, column=1, sticky=W+E)

root.bind("<Key>", keyboardHändler)
root.mainloop()
