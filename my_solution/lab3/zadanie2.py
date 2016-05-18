import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


g = np.array([0, -0.581])
k = 1
l = 1
m1, m2 = 1, 1

def norm(x):
    temp = np.sqrt(x[1]*x[1] + x[0]*x[0])
    return temp

def funkcja_prawych_stron(y, t0):
    dy = np.zeros(8)
    w1 = y[[0,1]]
    w2 = y[[4,5]]

    F = k*(norm(w2-w1) - l)*(w2-w1)/norm(w2-w1)
    # print F
    # print type(w1), type(F)

    dy[[0, 1]] = y[[2, 3]]
    dy[[2, 3]] = F/m1 + g
    dy[[4, 5]] = y[[6, 7]]
    dy[[6, 7]] = -F/m2 + g

    return dy






t = np.linspace(0,15, 501)
y0 = np.array([0, 0, 0, 5, -1, 0, -3, 3])


Y  = odeint(funkcja_prawych_stron, y0, t)
x1 = Y[:, 0]
y1 = Y[:, 1]
x2 = Y[:, 4]
y2 = Y[:, 5]

fig = plt.figure()

line1,  = plt.plot(x1, np.zeros_like(x1), "b.", markersize = 20)
line2,  = plt.plot(x2, np.zeros_like(x2), "g.", markersize = 20)
line3,  = plt.plot(x2, np.zeros_like(x2), "r-", linewidth = 3)

plt.plot(x1,y1, color="blue")
plt.plot(x2, y2, color="green")

plt.xlim([-25, 1])
plt.ylim([-1==0, 20])

def update_plot(frame):
    line1.set_xdata(x1[frame])
    line1.set_ydata(y1[frame])
    line2.set_xdata(x2[frame])
    line2.set_ydata(y2[frame])

    line3.set_xdata(np.array([x1[frame], x2[frame]]))
    line3.set_ydata(np.array([y1[frame], y2[frame]]))

anim = FuncAnimation(fig, update_plot, frames=500, interval=1, repeat=False)

plt.show()