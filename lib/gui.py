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

        self.canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), background='#80afd5')
        self.canvas.configure(scrollregion=(-root.winfo_screenwidth()/2+100,-root.winfo_screenheight()/2, root.winfo_screenwidth()/2-100, root.winfo_screenheight()/2))
        self.canvas.xview_moveto(.5)
        self.canvas.yview_moveto(.5)

        self.canvas.create_line(0,-5,0,5, fill="#3a3b3c", width=1, tags='ref')
        self.canvas.create_line(-5,0,5,0, fill="#3a3b3c", width=1, tags='ref')

        self.canvas.grid(row=0, column=3, rowspan=100)
        self.frame = Frame(self.root).grid(row=0, column=0, sticky="n")
        
        lwindow = options.lwindow(self.frame, self.canvas, self.root)

        self.root.after(1000, commands.simulate, self.root, self.canvas)

# END CLASS Gui #
