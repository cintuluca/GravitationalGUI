from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.messagebox import showinfo
import numpy as np
import pandas as pd
# custiom libraries
from lib import figures
from lib import globalv
from lib import gravity

def move(canvas, point, dt):
            x, y = point.object.x, point.object.y
            point.object.evolve(dt)
            canvas.move(point.circle, point.object.x-x, point.object.y-y)
            if globalv.stvar.get() == "Path":
                path = canvas.create_line(x, y, point.object.x, point.object.y, fill=point.color, tags="path")
                canvas.tag_bind(path, '<Button-1>', point.popup)
                canvas.lift('ref')
                point.path.append(path)

def merge(canvas, obj1, obj2):
    obj1.object.vx = (obj1.object.m*obj1.object.vx + obj2.object.m*obj2.object.vx) / (obj1.object.m + obj2.object.m)
    obj1.object.vy = (obj1.object.m*obj1.object.vy + obj2.object.m*obj2.object.vy) / (obj1.object.m + obj2.object.m)
    obj1.object.m += obj2.object.m
    obj1.dr = 2 + np.log(1 + obj1.object.m)
    canvas.delete(obj1.circle)
    obj1.circle = canvas.create_oval(obj1.object.x+obj1.dr, obj1.object.y+obj1.dr, obj1.object.x-obj1.dr, obj1.object.y-obj1.dr, width=1, fill=obj1.color, tags="point")
    canvas.lift('ref')
    canvas.tag_bind(obj1.circle, '<Button-1>', obj1.popup)
    obj2.delete()
            
def simulate(root, canvas):
    flag = True
    if globalv.running:
        for obj in globalv.points:
            gx, gy = 0, 0
            for point in globalv.points:
                dx = obj.object.x - point.object.x
                dy = obj.object.y - point.object.y
                if dx != 0 or dy != 0:
                    if dx**2 + dy**2 <= np.max([obj.dr, point.dr])/2 + 1:
                        if obj.object.m > point.object.m:
                            merge(canvas, obj, point)
                        else:
                            merge(canvas, point, obj)
                            flag = False
                    else:
                        Gx, Gy = gravity.G_acc(point.object.m, dx, dy)
                        gx = gx + Gx
                        gy = gy + Gy
            if flag:
                obj.object.force(gx, gy)
                move(canvas, obj, globalv.dt)
                canvas.update()
    if globalv.speed.get() == 'Custom':
        root.after(int(globalv.dt*1000), simulate, root, canvas)
    else:
        root.after(int(globalv.dt*1000/float(globalv.speed.get()[7:])), simulate, root, canvas)
                
def start():
    globalv.running = True
            
def stop():
    globalv.running = False
            
def clear(canvas):
    for point in globalv.points:
        if point.window is not None:
            point.window.destroy()
        del point
    globalv.points = []
    canvas.delete("point")
    canvas.delete("path")
            
def point(M, X, Y, Vx, Vy, Ax, Ay, canvas, root, color):
    if M.get() == '' or X.get() == '' or Y.get() == '' or Vx.get() == '' or Vy.get() == '' or Ax.get() == '' or Ay.get() == '':
        text = "No Number Inserted!"
        messagebox.showerror("Error", text)
    else:
        m, x, y, vx, vy, ax, ay = float(M.get())*globalv.mult[globalv.M_unit.get()], float(X.get())*globalv.mult[globalv.X_unit.get()], float(Y.get())*globalv.mult[globalv.Y_unit.get()], float(Vx.get())*globalv.mult[globalv.Vx_unit.get()], float(Vy.get())*globalv.mult[globalv.Vy_unit.get()], float(Ax.get())*globalv.mult[globalv.Ax_unit.get()], float(Ay.get())*globalv.mult[globalv.Ay_unit.get()]
        obj = gravity.object(m, ax, ay, vx, vy, x, y)
        figures.point(obj, canvas, root, color)
                
def select_file(root, canvas):
	filetypes = (('text files', '*.txt'), ('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file', filetypes=filetypes)
	if filename == () or filename == '':
		return
	df = pd.read_csv(filename, sep=',', names=['Mass','X','Y','Vx','Vy','Ax','Ay','Color'])
	for i in range(len(df)):	
		obj = gravity.object(df['Mass'][i], df['Ax'][i], df['Ay'][i], df['Vx'][i], df['Vy'][i], df['X'][i], df['Y'][i])
		point = figures.point(obj, canvas, root, color=df['Color'][i])

def select_folder(root, canvas):
	filetypes = (('text files', '*.txt'), ('All files', '*.*'))
	f = fd.asksaveasfile(title='Save file as', filetypes=filetypes, defaultextension=filetypes)
	if f is None:
		return
	for point in globalv.points:
		f.write(str(point.object.m)+','+str(point.object.x)+','+str(point.object.y)+','+str(point.object.vx)+','+str(point.object.vy)+','+str(point.object.ax)+','+str(point.object.ay)+','+str(point.color)+'\n')
	f.close()