import tkinter as tk
from tkinter import *
# custom libraries
from lib import commands
from lib import options

#**********#
class Gui():
#**********#
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=1800, height=1000, background='white')
        self.canvas.grid(row=0, column=2, rowspan=100)
        self.frame = Frame(self.root).grid(row=0, column=0, sticky="n")
        
        lwindow = options.lwindow(self.frame, self.canvas, self.root)

        self.root.after(1000, commands.simulate, self.root, self.canvas)

# END CLASS Gui #
