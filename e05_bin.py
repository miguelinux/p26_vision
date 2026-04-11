#!/usr/bin/env python3
import cv2 as cv
import numpy as np

#img = cv.imread("img/monedas.jpg")
img = cv.imread("img/coins_mexico.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold = 130

img_bin = np.zeros(img_gray.shape).astype("uint8")
#img_bin = img_gray.copy()   # 2

img_bin[img_gray > threshold] = 255
#img_bin[img_gray < threshold] = 255  # 1

cv.imshow("Original", img_gray)
cv.imshow("Binary", img_bin)

while True:
    # Leemos del teclado
    key = cv.waitKey(1000)
    # Verificamos si la ventana es visible
    win =  cv.getWindowProperty('Original', cv.WND_PROP_VISIBLE)

    # si se preciona la tecla ESC
    if key == 27 or key == ord("q") or win < 1.0:
        break

cv.destroyAllWindows()

