import os

sciezka = os.path.join("/home", 'piotr', "PycharmProjects", "python_course",
                       "resources", "lab2", "klaudia.png")

import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
from zadanie3 import reduce

image = img.imread(sciezka)

(msize, nsize) = (100, 100)

nonreduced = np.copy(image)

R = reduce(image[:, :, 0], (msize, nsize))
G = reduce(image[:, :, 1], (msize, nsize))
B = reduce(image[:, :, 2], (msize, nsize))

# old fashion
# img = np.array( [ [ [R[i][j], G[i][j], B[i][j]] for j in range(nsize)] for i in range(nsize)] )
# or
image2 = np.zeros((msize, nsize, 3))
image2[:, :, 0] = R
image2[:, :, 1] = G
image2[:, :, 2] = B

# plt.subplot(3, 1, 1)
imgplot = plt.imshow(image)
# plt.subplot(3, 1, 2)
imgplot = plt.imshow(image2)

import matplotlib.colors

imer = matplotlib.colors.rgb_to_hsv(image2)
imer[:, :, 1] = 0

# plt.subplot(3, 1, 2)
imgplot = plt.imshow(matplotlib.colors.hsv_to_rgb(imer))


dark = np.zeros((nsize, nsize), dtype=bool)
light = np.copy(dark)

for i in range(msize):
        for j in range(nsize):
                if imer[i, j, 2] < 0.3:
                        dark[i, j] = True
                        imer[i, j, 2] = 0.3
                elif imer[i, j][2] < 0.8:
                        light[i, j] = True
                        imer[i, j, 2] = 0.8

plt.subplot(1, 1, 1)
imgplot = plt.imshow(matplotlib.colors.hsv_to_rgb(imer))
plt.show()

with open("obrazek.txt", 'w') as f:
        for d, l in zip(dark, light):
                line = np.array(["  "] * nsize)
                line[d] = "//"
                line[l] = "/ "
                f.write("".join(line))
                f.write("\n")
