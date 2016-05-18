import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def przeszukiwanie(currentDir, iletab):

    iletab += 1
    for entry in os.listdir(currentDir):
        currentEntry = entry
        entry = os.path.join(currentDir, entry)
        if os.path.isdir(entry):
            for i in range(iletab):
                plik.write("  ")
            plik.write(currentEntry + "\n")  # + " is directory"
            przeszukiwanie(entry, iletab + 1)
        elif os.path.isfile(entry):
            for i in range(iletab):
                plik.write("  ")
            plik.write(currentEntry + "\n")

plik = open("./lab3/plik.txt", "w")
przeszukiwanie("/home/piotr/Documents", 0)
plik.close()

x = np.linspace(0,np.pi, 100)

fig = plt.figure()

line,  = plt.plot(x, np.zeros_like(x))

plt.xlim([0, np.pi])
plt.ylim([-1, 1])

def update_plot(frame):
    a  = float(frame)/100
    line.set_ydata(np.sin(a*x))

anim = FuncAnimation(fig, update_plot, frames=300, interval=1, repeat=False)

plt.show()
