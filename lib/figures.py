import numpy as np
import tkinter as tk
from tkinter import *
# custiom libraries
from lib import globalv

#**********#
class point:
#**********#
    def __init__(self, obj, canvas, root, color):
        self.window = None
        self.object = obj
        self.canvas = canvas
        self.root = root
        self.color = color
        self.circle = self.canvas.create_oval(self.object.x+5, self.object.y+5, self.object.x-5, self.object.y-5, width=1, fill=self.color, tags="point")
        self.path = []
        self.canvas.lift('ref')
        self.canvas.tag_bind(self.circle, '<Button-1>', self.popup)
        globalv.points.append(self)
        
    def delete(self):
        self.canvas.delete(self.circle)
        for line in self.path:
            self.canvas.delete(line)
        self.window.destroy()
        globalv.points.remove(self)
        del self

    def delete_path(self):
        for line in self.path:
            self.canvas.delete(line)
        self.window.destroy()
        
    def info(self, cond=False):
        self.Mass.set("Mass = "+str(self.object.m)+" Kg")
        self.X.set("X = "+str(self.object.x)+" m")
        self.Y.set("Y = "+str(self.object.y)+" m")
        self.V.set("Speed = "+str(np.sqrt(self.object.vx**2 + self.object.vy**2))+" m/s")
        self.A.set("Initial Acceleration = "+str(np.sqrt(self.object.ax**2 + self.object.ay**2))+" m/s^2")
        self.AG.set("Gravitational Acceleration = "+str(np.sqrt(self.object.gx**2 + self.object.gy**2))+" m/s^2")
        self.D.set("Direction = "+str(round(np.arctan(self.object.vy/(self.object.vx+1e-10))*180/np.pi, 2))+"°")
        if cond == True:
            self.root.after(100, self.info, True)
            
    def stay_on_top(self):
        self.window.lift()
        self.window.after(100, self.stay_on_top)

    def popup(self, event):
        if self.window is not None:
            self.window.destroy()
        self.window = Toplevel(self.root)
        self.window.title("Point Info")
        self.window.resizable(False, False)
        self.Mass, self.X, self.Y, self.V, self.A, self.AG, self.D = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
        self.info()
        Label(self.window, textvariable =self.Mass).grid(row=0, column=0, padx=10, pady=10, sticky="we")
        Label(self.window, textvariable =self.X).grid(row=1, column=0, padx=10, pady=10, sticky="we")
        Label(self.window, textvariable =self.Y).grid(row=2, column=0, padx=10, pady=10, sticky="we")
        Label(self.window, textvariable =self.V).grid(row=3, column=0, padx=10, pady=10, sticky="we")
        Label(self.window, textvariable =self.A).grid(row=4, column=0, padx=10, pady=10, sticky="we")
        Label(self.window, textvariable =self.AG).grid(row=5, column=0, padx=10, pady=10, sticky="we")
        Label(self.window, textvariable =self.D).grid(row=6, column=0, padx=10, pady=10, sticky="we")
        self.info(cond=True)
        Button(self.window, text="Delete", command=self.delete).grid(row=7, column=0, padx=10, pady=10)
        Button(self.window, text="Delete Path", command=self.delete_path).grid(row=8, column=0, padx=10, pady=10)
        # the window must always stay on top
        self.window.wm_attributes("-topmost", True)
        
# END CLASS point #
