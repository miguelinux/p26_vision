#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Se lee la imagen
img = cv.imread("baboon.png")

# Obtenemos su forma
fil, col, ch = img.shape

#img_gray = 0.2989 * img_R + 0.5870 * img_G + 0.1140 * img_B
#img_gray = img_gray.astype('uint8')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Creamos vector de 256 elementos
histog = np.zeros(256, dtype='uint32')

for x in range(fil):
    for y in range(col):
        valor = img_gray[x][y]
        histog[valor] += 1

# Valores del eje x
x = [n for n in range(256)]

fig, ax = plt.subplots(1,2)
ax[0].imshow(img_gray, cmap='gray', vmin=0, vmax=255)
ax[1].bar(x,histog)
#ax[1].hist(img_gray.ravel(),256,[0,256])
plt.show()
