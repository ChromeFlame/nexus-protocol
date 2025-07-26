import tkinter as tk

from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title("Nexus")
root.geometry("800x600")

frm = ttk.Frame(root, padding=10)
frm.grid()

# DPad
dpad = ttk.Frame(root, padding = 10)
dpad.grid()
ttk.Button(dpad, text="NW").grid(column = 0, row = 0)
ttk.Button(dpad, text="N").grid(column = 1, row = 0)
ttk.Button(dpad, text="NE").grid(column = 2, row = 0)
ttk.Button(dpad, text="Up").grid(column = 3, row = 0)
ttk.Button(dpad, text="W").grid(column = 0, row = 1)
ttk.Button(dpad, text="Look").grid(column = 1, row = 1)
ttk.Button(dpad, text="E").grid(column = 2, row = 1)
ttk.Button(dpad, text="Wait").grid(column = 3, row = 1)
ttk.Button(dpad, text="SW").grid(column = 0, row = 2)
ttk.Button(dpad, text="S").grid(column = 1, row = 2)
ttk.Button(dpad, text="SE").grid(column = 2, row = 2)
ttk.Button(dpad, text="Down").grid(column = 3, row = 2)

def displayStat(parent, subject, attribute):
    ttk.Label(parent, text = subject.attribute).grid(column = 0, row = 0)
    ttk.Label(parent, text = subject.attribute).grid(column = 1, row = 0)
    ttk.Label(parent, text = subject.attribute).grid(column = 2, row = 0)
    
# Stats
statscreen = ttk.Frame(root, padding = 10)
statscreen.grid()
ttk.Label(statscreen, text = "Strength").grid(column = 0, row = 0)
ttk.Label(statscreen, text = "0").grid(column = 1, row = 0)
ttk.Label(statscreen, text = "[|||||]").grid(column = 2, row = 0)
ttk.Label(statscreen, text = "Wisdom").grid(column = 0, row = 1)
ttk.Label(statscreen, text = "0").grid(column = 1, row = 1)
ttk.Label(statscreen, text = "[|||||]").grid(column = 2, row = 1)
ttk.Label(statscreen, text = "Dexterity").grid(column = 0, row = 2)
ttk.Label(statscreen, text = "0").grid(column = 1, row = 2)
ttk.Label(statscreen, text = "[|||||]").grid(column = 2, row = 2)
ttk.Label(statscreen, text = "Health").grid(column = 0, row = 3)
ttk.Label(statscreen, text = "0").grid(column = 1, row = 3)
ttk.Label(statscreen, text = "[|||||]").grid(column = 2, row = 3)
ttk.Label(statscreen, text = "Armor").grid(column = 0, row = 4)
ttk.Label(statscreen, text = "0").grid(column = 1, row = 4)
ttk.Label(statscreen, text = "[|||||]").grid(column = 2, row = 4)
ttk.Label(statscreen, text = "Fatigue").grid(column = 0, row = 5)
ttk.Label(statscreen, text = "0").grid(column = 1, row = 5)
ttk.Label(statscreen, text = "[|||||]").grid(column = 2, row = 5)

# Menubar
menubar = Menu(root)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = file)
file.add_command(label = "New Game")
file.add_command(label = "Load Game")
file.add_command(label = "Save")
file.add_command(label = "Save as")
file.add_command(label = "Exit", command = root.destroy)

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
entry = ttk.Entry(frm,).grid(column = 0, row = 2)

root.config(menu = menubar)
root.mainloop()
