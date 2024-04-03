import tkinter as tk
from tkinter import *
# custiom libraries
from lib import commands
from lib import options

# global variables for GUI execution

def init():

    global width
    width = 0
    
    global height
    height = 0

    global dt
    dt = 1

    global points
    points = []
    
    global running
    running = False
    
    global stvar
    stvar = tk.StringVar()
    stvar.set("Path")
    
    global speed
    speed = tk.StringVar()
    speed.set("Speed X 1")
    
    global color
    color = tk.StringVar()
    color.set("Black")

    global M_unit
    M_unit= tk.StringVar()
    M_unit.set("Kg")

    global X_unit
    X_unit= tk.StringVar()
    X_unit.set("m")

    global Y_unit
    Y_unit= tk.StringVar()
    Y_unit.set("m")

    global Vx_unit
    Vx_unit= tk.StringVar()
    Vx_unit.set("m/s")

    global Vy_unit
    Vy_unit= tk.StringVar()
    Vy_unit.set("m/s")

    global Ax_unit
    Ax_unit= tk.StringVar()
    Ax_unit.set("m/s^2")

    global Ay_unit
    Ay_unit= tk.StringVar()
    Ay_unit.set("m/s^2")

    global mult
    mult = {'Kg': 1, 'g': 1e-3, 'm': 1, 'Km': 1e3, 'm/s': 1, 'Km/s': 1e3, 'm/s^2': 1}

#************#
class trace:
#************#
    def __init__(self, root):
        self.root = root
        self.value = tk.StringVar()
        speed.trace_add("write", callback=self.check_speed)

    def check_speed(self, var, index, mode):
        if speed.get() == "Custom":
            self.window = Toplevel(self.root)
            self.window.wm_attributes("-topmost", True)
            self.window.title("Custom Speed")
            self.window.resizable(False, False)
            M = tk.StringVar()
            text = Label(self.window, text="Insert the custom speed:	(MAX = 1000)").grid(row=0,column=0, padx=20, pady=10, sticky="we")
            entry = Entry(self.window, textvariable=self.value).grid(row=1, column=0, padx=10, pady=20, sticky="we")
            button = tk.Button(self.window, text='Confirm', command=self.custom_speed).grid(row=2, column=0, padx=20, pady=10, sticky="we")

    def custom_speed(self):
        if int(self.value.get()) > 1000:
            speed.set("Speed X 1000")
        else:
            speed.set("Speed X " + self.value.get())
        self.window.destroy()
