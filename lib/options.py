import tkinter as tk
from tkinter import *
# custom libraries
from lib import commands
from lib import globalv

#************#
class lwindow:
#************#
    def __init__(self, frame, canvas, root):
    
        self.path = tk.OptionMenu(frame, globalv.stvar, "Path", "No Path").grid(row=0, column=1, sticky="we")

        M = tk.StringVar()
        label1 = Label(frame, text="Mass").grid(row=1,column=0, sticky="w")
        entry1 = Entry(frame, textvariable=M).grid(row=1, column=1, sticky=E+W)
        
        X = tk.StringVar()
        label2 = Label(frame, text="X").grid(row=2,column=0, sticky="w")
        entry2 = Entry(frame, textvariable=X).grid(row=2, column=1, sticky=E+W)
        
        Y = tk.StringVar()
        label3 = Label(frame, text="Y").grid(row=3,column=0, sticky="w")
        entry3 = Entry(frame, textvariable=Y).grid(row=3, column=1, sticky=E)
        
        Vx = tk.StringVar()
        label4 = Label(frame, text="Vx").grid(row=4,column=0, sticky="w")
        entry4 = Entry(frame, textvariable=Vx).grid(row=4, column=1, sticky=E+W)
        
        Vy = tk.StringVar()
        label5 = Label(frame, text="Vy").grid(row=5,column=0, sticky="w")
        entry5 = Entry(frame, textvariable=Vy).grid(row=5, column=1, sticky=E)
        
        Ax = tk.StringVar()
        label6 = Label(frame, text="Ax").grid(row=6,column=0, sticky="w")
        entry6 = Entry(frame, textvariable=Ax).grid(row=6, column=1, sticky=E+W)
        
        Ay = tk.StringVar()
        label7 = Label(frame, text="Ay").grid(row=7,column=0, sticky="w")
        entry7 = Entry(frame, textvariable=Ay).grid(row=7, column=1, sticky=E)
        
        label8 = Label(frame, text="Color").grid(row=8,column=0, sticky="w")
        self.colors = tk.OptionMenu(frame, globalv.color, "Black", "Red", "Blue").grid(row=8, column=1, sticky="we")

        Button1 = Button(frame, text="Draw", command=lambda: commands.point(M, X, Y, Vx, Vy, Ax, Ay, canvas, root)).grid(row=9, column=1, sticky="we")
        Button2 = Button(frame, text="Clear", command=lambda: commands.clear(canvas)).grid(row=10, column=1, sticky="we")
        
        label9 = Label(frame, text="Load Configuration\t:").grid(row=11, column=1, pady=(50,0), sticky="w")
        Button3 = tk.Button(frame, text='Open File', command=commands.select_file).grid(row=12, column=1, pady=(0,50), sticky="we")
                
        Button4 = Button(frame, text="Start Simulation", command=commands.start).grid(row=13, column=1, sticky="we")
        Button5 = Button(frame, text="Stop Simulation", command=commands.stop).grid(row=14, column=1, pady=(0,50), sticky="we")
        
        self.Speed = tk.OptionMenu(frame, globalv.speed, "Speed X 0.5", "Speed X 1", "Speed X 2", "Speed X 5", "Speed X 10").grid(row=15, column=1, sticky="we")
        
# END CLASS lwindow #
