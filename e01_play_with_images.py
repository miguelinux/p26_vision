#!/usr/bin/env python3
import cv2 as cv
import numpy as np

# Se lee la imagen
img = cv.imread("baboon.png")

# Se muestra la imagen
cv.imshow("Baboon", img)

# Obtenemos su forma
fil, col, ch = img.shape

# Separamos por canales
img_B, img_G, img_R = cv.split(img)

cv.imshow("Baboon Red (Grayscale)", img_R)

g_img = np.zeros(shape=(fil,col,ch), dtype='uint8')
g_img[:,:,2] = img_R

cv.imshow("Baboon Red", g_img)

# https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html#color_convert_rgb_gray
#img_gray = np.zeros(shape=(fil,col))
#img_gray = np.dot(0.2989, img_R) + np.dot(0.5870, img_G) + np.dot(0.1140, img_B)
img_gray = 0.2989 * img_R + 0.5870 * img_G + 0.1140 * img_B
img_gray = img_gray.astype('uint8')

cv.imshow("Baboon Grayscale", img_gray)

# OpenCV converts an image from one color space to another.
ocv_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Baboon Grayscale OpenCV", ocv_gray)

#diff = cv.absdiff(img_gray, ocv_gray)
#cv.imshow("Diff", diff)

while True:
    # Leemos del teclado
    key = cv.waitKey(1000)
    # Verificamos si la ventana es visible
    win =  cv.getWindowProperty('Baboon', cv.WND_PROP_VISIBLE)

    # si se preciona la tecla ESC
    if key == 27 or win < 1.0:
        break

cv.destroyAllWindows()
