import sys, os
from tkinter import *
from tkinter import ttk
from random import choice
root = Tk()

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

class Menu:
    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master)
        self.master.title("Invoker")
        self.iconphoto = root.iconphoto(True, PhotoImage(file=os.path.join(sys.path[0], "icon.png")))
        self.logo = PhotoImage(file="icon.png")
        self.label = Label(self.master, image=self.logo)
        self.label.pack()
        self.button_frame = Frame(self.master)
        self.button_frame.pack(fill=X, side=BOTTOM)
        self.ez_button = Button(self.button_frame, text="Ez mode", command = lambda: self.mode("ez"))
        self.hc_button = Button(self.button_frame, text="Hc mode (timed)", command = lambda: self.mode("hc"))
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.ez_button.grid(row=1, column=0, sticky=W+E)
        self.hc_button.grid(row=1, column=1, sticky=W+E)
    
    def mode(self, mode):
        self.newWindow = Toplevel(self.master)
        self.app = Main(self.newWindow, mode)

class Main:
    def __init__(self, master, mode):
        self.master = master
        self.frame = ttk.Frame(self.master)
        self.master.focus_force()
        self.mode = mode
        self.spell_stack = [TÜHI, TÜHI, TÜHI]
        self.stack = [TÜHI, TÜHI, TÜHI]
        self.uuendaStacki()
        self.spell_stack[0] = self.annaUusSpell()
        self.spell_stack[1] = self.annaUusSpell()
        self.spell_stack[2] = self.annaUusSpell()
        self.uuendaSpelliStacki()
        self.master.bind("<Key>", self.keyboardHändler)
        self.skoor = 0
        if self.mode == "hc":
            self.aeg = 60
            self.timer()
    
    def uuendaSpelliStacki(self):
        global SPELLI_PILDID
        self.l1_spell = Label(self.frame, image=SPELLI_PILDID[self.spell_stack[0]], padx=20)
        self.l2_spell = Label(self.frame, image=SPELLI_PILDID[self.spell_stack[1]], padx=20)
        self.l3_spell = Label(self.frame, image=SPELLI_PILDID[self.spell_stack[2]], padx=20)
        self.l1_spell.grid(row=2, column=0)
        self.l2_spell.grid(row=2, column=1)
        self.l3_spell.grid(row=2, column=2)
        self.frame.pack()
    
    def uuendaStacki(self):
        self.l1_stack = Label(self.frame, image=PILDID[self.stack[0]], padx=20)
        self.l2_stack = Label(self.frame, image=PILDID[self.stack[1]], padx=20)
        self.l3_stack = Label(self.frame, image=PILDID[self.stack[2]], padx=20)
        self.l1_stack.grid(row=1, column=0)
        self.l2_stack.grid(row=1, column=1)
        self.l3_stack.grid(row=1, column=2)
        self.frame.pack()
    
    def annaUusSpell(self):
        while True:
            spell = "".join(sorted(choice("qwe") + choice("qwe") + choice("qwe")))
            if not spell in self.spell_stack:
                return spell
    
    def kontrolliSpelli(self):
        spell = "".join(sorted(self.stack))
        if spell == self.spell_stack[0]:
            self.spell_stack[0], self.spell_stack[1] = self.spell_stack[1], self.spell_stack[2]
            self.spell_stack[2] = self.annaUusSpell()
            self.uuendaSpelliStacki()
            self.skoor += 1
    
    def keyboardHändler(self, event):
        if event.char in "qwe":
            self.stack[0], self.stack[1] = self.stack[1], self.stack[2]
            self.stack[2] = event.char
            self.uuendaStacki()
        elif event.char == "r":
            self.kontrolliSpelli()
    
    def timer(self):
        self.aeg -= 1
        if self.aeg != 0:
            self.l1 = Label(self.frame, text="Skoor: %i\nAega veel %is" % (self.skoor, self.aeg))
            self.master.after(1000, self.timer)
        else:
            self.l1 = Label(self.frame, text="MÄNG LÄBI!\nSaid %i punkti!" % self.skoor)
        self.l1.grid(row=0, column=1)
        self.frame.pack()

app = Menu(root)
root.mainloop()
