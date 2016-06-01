import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


g = 9.81
r1, r2 = 0.05, 0.2
m1, m2 = 1, 2

def norm(x):
    temp = np.sqrt(x[1]*x[1] + x[0]*x[0])
    return temp

def funkcja_prawych_stron(y, t0):
    dy = np.zeros(8)
    w1 = y[[0,1]]
    w2 = y[[4,5]]
    a = w1 - w2
    sin_alfa = a[1]/norm(a)
    cos_alfa = a[0]/norm(a)

    if norm(a) <= (r1 + r2)+ 0.0001:
        R = np.array([cos_alfa*sin_alfa, sin_alfa*sin_alfa - 1])*g
    else:
        R = np.array([0, -1.0])

    dy[[0, 1]] = y[[2, 3]]
    dy[[2, 3]] = R/m1
    if y[1] < r1:
        # print "haha"
        dy[1] = 0
        temp = True
    dy[[4, 5]] = y[[6, 7]]
    dy[[6, 7]] = np.array([-R[0]/m2, 0])

    return dy



fram = 300
tk = 6


t = np.linspace(0,tk, fram + 1)
y0 = np.array([0.500001, 2*r2 + r1, 0, 0, 0.5, r2, 0, 0])

Y  = odeint(funkcja_prawych_stron, y0, t)

x1 = Y[:, 0]
y1 = Y[:, 1]
x2 = Y[:, 4]
y2 = Y[:, 5]


fig=plt.figure(1)
plt.axis([0,400,0,400])
ax=fig.add_subplot(1,1,1)
circ1=plt.Circle((x1[0],y1[0]), radius=r1, color='g', fill=False,transform=ax.transAxes)
circ2=plt.Circle((x2[0],y2[0]), radius=r2, color='r', fill=False,transform=ax.transAxes)
ax.add_patch(circ1)
ax.add_patch(circ2)
plt.plot(x1*400, y1*400)
plt.plot(x2*400, y2*400)

def update_plot(frame):
    circ1.center = [x1[frame], y1[frame]]
    circ2.center = [x2[frame], y2[frame]]

anim = FuncAnimation(fig, update_plot, frames=fram, interval=1, repeat=False)

plt.show()

