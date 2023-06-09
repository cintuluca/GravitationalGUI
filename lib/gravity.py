import numpy as np

G = 6.67e-11

def G_acc(m, x, y):
    d = np.sqrt(x**2 + y**2)
    g = -G*m/d**2
    gx = g*x/d
    gy = g*y/d
    return gx, gy

#***********#
class object:
#***********#
    def __init__(self, m, ax, ay, vx, vy, x, y):
        self.m = m
        self.ax = ax
        self.ay = ay
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.gx = 0
        self.gy = 0
        
    def evolve(self, t):
        vx_new = self.vx + (self.ax+self.gx)*t
        vy_new = self.vy + (self.ay+self.gy)*t
        x_new = self.x + self.vx*t + 0.5*(self.ax+self.gx)*t**2
        y_new = self.y + self.vy*t + 0.5*(self.ay+self.gy)*t**2
        self.vx = vx_new
        self.vy = vy_new
        self.x = x_new
        self.y = y_new
        
    def force(self, gx, gy):
        self.gx = gx
        self.gy = gy
        
# END CLASS object #
