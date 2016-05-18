'''
                  - -
            - - - - - - - -
        ||- - -         - - - -
      ||||      ||||  -     - - -
    ||||    ||  ||-   ||||||    - -
    ||||  ||||  ||    ||  ||||  - -
  ||||  ||||    ||    ||    ||||  - -
  ||||  ||      ||    ||      ||  - -
  ||  - ||      ||    ||      ||    -
||||  ||||    ||||||  ||      ||||  - -
||||  ||||      ||    ||      ||||  - -
  ||    ||      ||    ||      ||    -
  ||||  ||      ||    ||      ||  - -
  ||||  ||||    ||    ||    ||-   - -
    ||||  ||||  ||    ||  ||||  - -
    ||||    ||  ||    ||||-     - -
      ||||||                ||- -
        ||||||||        ||||||-
            ||||||||||||||||
                  ||||
'''

import matplotlib.pyplot as plt
import matplotlib.image
import matplotlib.colors as colors
import numpy as np

from zadanie3 import reduce

out = "banner.txt"
infile ='../../resources/lab1/meil.png'

img = matplotlib.image.imread(infile)

nsize = 20

nonreduced = np.copy(img)

R = reduce( img[:, :, 0], (nsize, nsize))
G = reduce( img[:, :, 1], (nsize, nsize))
B = reduce( img[:, :, 2], (nsize, nsize))

# old fashion
# img = np.array( [ [ [R[i][j], G[i][j], B[i][j]] for j in range(nsize)] for i in range(nsize)] )
# or
img = np.zeros((nsize, nsize, 3))
img[:, :, 0] = R
img[:, :, 1] = G
img[:, :, 2] = B


hsvimg = colors.rgb_to_hsv(img)
hsvimg[:, :, 1] = 0

cliped = np.copy(hsvimg)

# old fashion
# dark = np.array( [ [ [False] for j in range(nsize) ] for i in range(nsize)] )
# light = np.array( [ [ [False] for j in range(nsize) ] for i in range(nsize)] )
# or
dark = np.zeros((nsize, nsize), dtype=bool)
light = np.copy(dark)

for i in range(nsize):
    for j in range(nsize):
        if hsvimg[i, j, 2] < 0.3:
            cliped[i, j, 2] = 0
            dark[i, j] = True
        elif hsvimg[i, j][2] < 0.6:
            cliped[i, j][2] = .3
            light[i, j] = True
        else:
            cliped[i, j, 2] = 1

_, (a1, a2, a3) = plt.subplots(1, 3)

print a1

exit()

a1.imshow(nonreduced)
a2.imshow(colors.hsv_to_rgb(hsvimg))
a3.imshow(colors.hsv_to_rgb(cliped))

plt.show()

with open(out, 'w') as f:
    for d, l in zip(dark, light):
        line = np.array(["  "]*nsize)
        line[d] = "||"
        line[l] = "- "
        f.write("".join(line))
        f.write("\n")