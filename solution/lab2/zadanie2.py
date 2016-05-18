import numpy as np
from numpy.linalg import norm
from scipy.integrate import odeint

import matplotlib.pyplot as plt
from matplotlib import animation


m, l, k = [10, 10, 10]
x1 = [0, 0]
x2 = [-l, 0]
u1 = [0, 50]
u2 = [-30, 30]
endTime=10
nSteps=500
nFrames=100

def equation(Y, t):
    '''
    Equations of motion
    dr = x2 - x1
    m a1 = dr k (1 - l/|dr|)
    m a2 = - dr k (1 - l/|dr|)
    '''
    x1 = Y[:2]
    u1 = Y[2:4]
    x2 = Y[4:6]
    u2 = Y[6:]

    dr = x2-x1

    dY = np.zeros(8)

    if x1[1] < 0 or x2[1] <0:
        return dY

    dY[2:4] = dr*k/m*(1-l/norm(dr))
    dY[3] -= 9.81
    dY[6:] = -dr*k/m*(1-l/norm(dr))
    dY[7] -= 9.81
    dY[:2] = u1
    dY[4:6] = u2

    return dY


Y0 = np.array([x1,u1,x2,u2]).reshape(8)


Y = odeint(equation, Y0, np.linspace(0, endTime, nSteps) )

fig = plt.figure()

plt.plot(Y[:,0], Y[:,1])
plt.plot(Y[:,4], Y[:,5])
p1, = plt.plot(Y0[0],Y0[1], '.', markersize=10, color="blue")
p2, = plt.plot(Y0[4],Y0[5], '.', markersize=10, color="green")
spring, = plt.plot(Y0[4],Y0[5], '-', markersize=10, color="red")


plt.axes().set_aspect('equal', 'datalim')
plt.axes().grid(True)



def anim(frame):
    t = int(len(Y)*float(frame)/nFrames)
    x1 = Y[t,:2]
    x2 = Y[t,4:6]

    p1.set_data(x1)
    p2.set_data(x2)
    spring.set_data([x1[0],x2[0]], [x1[1], x2[1]])



a = animation.FuncAnimation(fig, anim, frames=nFrames, interval=10, repeat=False)


# fig.set_size_inches(3, 3, forward=True)
# a.save('/home/wgryglas/Documents/dydaktyka/courses/figures/python_inst03/mass10.gif', writer='imagemagick', fps=100)

plt.show()

