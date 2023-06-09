import tkinter as tk

# global variables for GUI execution

def init():
    global dt
    dt = 0.1

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
