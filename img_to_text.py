
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as colors
import numpy as np
import Image
from scipy.ndimage.interpolation import zoom

out = "/home/wgryglas/Desktop/dog.txt"
#infile ='resources/dog.png'
infile ='resources/lion.png'

img=mpimg.imread(infile)


#remove transparency
if img.shape[2] > 3:
    img[np.where(img[:,:,3] == 0),:3] = 1
    img = np.array(img[:,:,:3])

# R = zoom(img[:,:,0],0.25, order=1)
# G = zoom(img[:,:,1],0.25, order=1)
# B = zoom(img[:,:,2],0.25, order=1)
# img = np.zeros((R.shape[0],R.shape[1],3))
# img[:,:,0]=R
# img[:,:,1]=G
# img[:,:,2]=B



img[np.where(img[:,:,0] ==0)]=1

#
# clearIds = np.where(A == 0)
# img[clearIds,:] = 1

# img = Image.open(infile)
# img = img.resize((150, 210))
# img = np.asarray(img)


hsvimg = colors.rgb_to_hsv(img)
# hsvimg[:,:,2] =  hsvimg[:,:,2] / 255

g_hsvimg = np.copy(hsvimg)
g_hsvimg[:, :, 1] = 0

# dark = np.zeros((img.shape[0], img.shape[1]), dtype=bool)
# light = np.copy(dark)

clip = [(i+1)*0.1 for i in range(10)]

for i in range(g_hsvimg.shape[0]):
    for j in range(g_hsvimg.shape[1]):
        for s in clip:
            if g_hsvimg[i,j,2] < s:
                g_hsvimg[i,j,2] = s-0.1

#
#         dark[i,j] = g_hsvimg[i,j, 2] > 0.6
#         light[i,j] = g_hsvimg[i,j, 2] > 0.2


gimg = colors.hsv_to_rgb(g_hsvimg)

_,(a1, a2) = plt.subplots(1,2)
imgplt = a1.imshow(img)
imgplt = a2.imshow(gimg)
plt.show()


# with open(out,'w') as f:
#     for l in locsmall:
#         line = np.array(["  "]*locsmall.shape[1])
#         line[l] = "+ "
#         f.write("".join(line))
#         f.write("\n")
