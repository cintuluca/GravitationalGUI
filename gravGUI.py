#!/usr/bin/env python3

import sys
import tkinter as tk
# custom libraries
from lib import globalv
from lib import gui

if __name__== '__main__': 
    root=tk.Tk()
    root.title("Gravitational GUI")
    globalv.init()
    globalv.trace(root)
    gui=gui.Gui(root)
    root.mainloop()
