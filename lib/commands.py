from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.messagebox import showinfo
# custiom libraries
from lib import figures
from lib import globalv
from lib import gravity

def move(canvas, point, dt):
            x, y = point.object.x, point.object.y
            point.object.evolve(dt)
            canvas.moveto(point.circle, point.object.x-5, point.object.y-5)
            if globalv.stvar.get() == "Path":
                canvas.create_line(x, y, point.object.x, point.object.y, fill=point.color)
            
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
            # print(dt*i, obj.x, obj.y, obj.vx, obj.vy, obj.ax, obj.ay)
            canvas.update()   
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
    canvas.delete("all")
            
def point(M, X, Y, Vx, Vy, Ax, Ay, canvas, root):
    if M.get() == '' or X.get() == '' or Y.get() == '' or Vx.get() == '' or Vy.get() == '' or Ax.get() == '' or Ay.get() == '':
        text = "No Number Inserted!"
        messagebox.showerror("Error", text)
    else:
        m, x, y, vx, vy, ax, ay = float(M.get()), float(X.get()), float(Y.get()), float(Vx.get()), float(Vy.get()), float(Ax.get()), float(Ay.get())
        obj = gravity.object(m, ax, ay, vx, vy, x, y)
        figures.point(obj, canvas, root)
                
def select_file():
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    showinfo(title='Selected File', message=filename)
