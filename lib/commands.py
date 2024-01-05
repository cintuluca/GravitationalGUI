from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.messagebox import showinfo
import pandas as pd
# custiom libraries
from lib import figures
from lib import globalv
from lib import gravity

def move(canvas, point, dt):
            x, y = point.object.x, point.object.y
            point.object.evolve(dt)
            canvas.moveto(point.circle, point.object.x-5, point.object.y-5)
            if globalv.stvar.get() == "Path":
                path = canvas.create_line(x, y, point.object.x, point.object.y, fill=point.color, tags="path")
                canvas.tag_bind(path, '<Button-1>', point.popup)
                canvas.lift('ref')
                point.path.append(path)
            
def simulate(root, canvas):
    if globalv.running:
        for obj in globalv.points:
            gx, gy = 0, 0
            for point in globalv.points:
                dx = obj.object.x - point.object.x
                dy = obj.object.y - point.object.y
                if dx != 0 or dy != 0:
                    Gx, Gy = gravity.G_acc(point.object.m, dx, dy)
                    gx = gx + Gx
                    gy = gy + Gy
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
        print(globalv.mult)
        m, x, y, vx, vy, ax, ay = float(M.get())*globalv.mult[globalv.M_unit.get()], float(X.get())*globalv.mult[globalv.X_unit.get()], float(Y.get())*globalv.mult[globalv.Y_unit.get()], float(Vx.get())*globalv.mult[globalv.Vx_unit.get()], float(Vy.get())*globalv.mult[globalv.Vy_unit.get()], float(Ax.get())*globalv.mult[globalv.Ax_unit.get()], float(Ay.get())*globalv.mult[globalv.Ay_unit.get()]
        obj = gravity.object(m, ax, ay, vx, vy, x, y)
        figures.point(obj, canvas, root, color)
                
def select_file(root, canvas):
	filetypes = (('text files', '*.txt'), ('All files', '*.*'))
	filename = fd.askopenfilename(title='Open a file', filetypes=filetypes)
	if filename == ():
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