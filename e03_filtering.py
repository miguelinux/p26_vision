#!/usr/bin/env python3
import cv2 as cv
import numpy as np

# Se lee la imagen
img = cv.imread("tigre_2.jpg")

# Obtenemos su forma
fil, col, ch = img.shape

#kernel = (1/9) * np.array([[ 1.,  1., 1.],
#                           [ 1.,  1., 1.],
#                           [ 1.,  1., 1.]])

#kernel = [[ 0.,  1., 0.],
#          [ 1., -4., 1.],
#          [ 0.,  1., 0.]]

#kernel = [[ 0., -1., 0.],
#          [-1.,  5.,-1.],
#          [ 0., -1., 0.]]

kernel = [[ 0.,  0., 0.],
          [ 0.,  1., 0.],
          [ 0.,  0., 0.]]

#img_gray = 0.2989 * img_R + 0.5870 * img_G + 0.1140 * img_B
#img_gray = img_gray.astype('uint8')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_float = img_gray.astype('float')
img_filtrada = np.zeros(shape=(fil,col), dtype='float')

for m in range(1,fil-1):
    for n in range(1,col-1):
        aux = 0.0
        for k in range(3):
            for l in range(3):
                aux += kernel[k][l] * img_float[m+k-1][n+l-1]
        img_filtrada[m][n] = aux

img_filtrada = img_filtrada.astype('uint8')

cv.imshow("Original", img_gray)
cv.imshow("Filtrada", img_filtrada)

while True:
    # Leemos del teclado
    key = cv.waitKey(1000)
    # Verificamos si la ventana es visible
    win =  cv.getWindowProperty('Original', cv.WND_PROP_VISIBLE)

    # si se preciona la tecla ESC
    if key == 27 or key == ord("q") or win < 1.0:
        break

cv.destroyAllWindows()

