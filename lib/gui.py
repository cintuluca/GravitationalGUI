import tkinter as tk
from tkinter import *
# custom libraries
from lib import commands
from lib import globalv
from lib import options

#**********#
class Gui():
#**********#
    def __init__(self, root):
        self.root = root

        width, height = root.winfo_screenwidth()-250, root.winfo_screenheight()
        self.canvas = tk.Canvas(root, width=width, height=height, scrollregion=(-width,-height,width,height), background='#80afd5')
        globalv.width, globalv.height = width, height

        self.canvas.create_line(0,-5,0,5, fill="#3a3b3c", width=1, tags='ref')
        self.canvas.create_line(-5,0,5,0, fill="#3a3b3c", width=1, tags='ref')

        self.canvas.grid(row=0, column=3, rowspan=100)
        self.frame = tk.Frame(self.root).grid(row=0, column=0, sticky="n")
        
        self.HorizontalScrollBar = tk.Scrollbar(root)
        self.VerticalScrollBar = tk.Scrollbar(root)
        
        lwindow = options.lwindow(self.frame, self.canvas, self.root)

        self.root.after(1000, commands.simulate, self.root, self.canvas)

    # Sets up the Canvas, Frame, and scrollbars for scrolling
    def createScrollableContainer(self):
	    self.canvas.config(xscrollcommand=self.HorizontalScrollBar.set,yscrollcommand=self.VerticalScrollBar.set, highlightthickness=0)
	    self.HorizontalScrollBar.config(orient=tk.HORIZONTAL, command=self.canvas.xview)
	    self.VerticalScrollBar.config(orient=tk.VERTICAL, command=self.canvas.yview)

	    self.HorizontalScrollBar.grid(column=3, row=0, padx=20, sticky='we')
	    self.VerticalScrollBar.grid(column=3, row=1, rowspan=20, padx=20, sticky='w'+'ns')
	    self.canvas.create_window(0, 0, window=self.frame, anchor=tk.NW)
	    
	    self.canvas.xview_moveto(0.25)
	    self.canvas.yview_moveto(0.25)

# END CLASS Gui #
