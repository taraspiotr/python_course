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
import matplotlib.image as mpimg
import matplotlib.colors as colors
import numpy as np
import Image
from scipy.ndimage.interpolation import zoom

out = "/home/wojtek/banner.txt"
#infile ='resources/dog.png'
infile ='resources/meil.png'
# infile ='resources/lion.png'

img = mpimg.imread(infile)

# #remove transparency
# if img.shape[2] > 3:
#     img[np.where(img[:, :, 3] == 0), :3] = 1
#     img = np.array(img[:, :, :3])

R = zoom(img[:,:,0],0.1, order=1)
G = zoom(img[:,:,1],0.1, order=1)
B = zoom(img[:,:,2],0.1, order=1)
img = np.zeros((R.shape[0],R.shape[1],3))
img[:,:,0]=R
img[:,:,1]=G
img[:,:,2]=B

#img[np.where(img[:,:,0] ==0)]=1

#
# clearIds = np.where(A == 0)
# img[clearIds,:] = 1

# img = Image.open(infile)
# img = np.asarray(img.resize((50, 50)))


hsvimg = colors.rgb_to_hsv(img)
# hsvimg[:,:,2] =  hsvimg[:,:,2] / 255

g_hsvimg = np.copy(hsvimg)
g_hsvimg[:, :, 1] = 0

dark = np.zeros((img.shape[0], img.shape[1]), dtype=bool)
light = np.copy(dark)

clip = [(i+1)*0.1 for i in range(10)]

for i in range(g_hsvimg.shape[0]):
    for j in range(g_hsvimg.shape[1]):
        for s in clip:
            if g_hsvimg[i, j, 2] < 0.3:
                g_hsvimg[i, j, 2] = 0
                dark[i, j] = True
            elif g_hsvimg[i, j, 2] < 0.6:
                g_hsvimg[i, j, 2] = .3
                light[i, j] = True
            else:
                g_hsvimg[i, j, 2] = 1

gimg = colors.hsv_to_rgb(g_hsvimg)

_, (a1, a2) = plt.subplots(1, 2)
imgplt = a1.imshow(img)
imgplt = a2.imshow(gimg)
plt.show()

with open(out, 'w') as f:
    for d, l in zip(dark, light):
        line = np.array(["  "]*dark.shape[1])
        line[d] = "||"
        line[l] = "- "
        f.write("".join(line))
        f.write("\n")
