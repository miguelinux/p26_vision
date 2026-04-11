#!/usr/bin/env python3
import cv2 as cv
import numpy as np

img = cv.imread("img/monedas.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 2. Calcular el histograma
# cv2.calcHist([images], channels, mask, histSize, ranges)
hist = cv.calcHist([img_gray], [0], None, [256], [0, 256])
hist_acu = cv.calcHist([img_gray], [0], None, [256], [0, 256], None, True)

largo, ancho = img_gray.shape
total_pixeles = largo * ancho

for T in range(256):
    Wb = sum(hist_acu(:T)) / total_pixeles # background
    Wf = sum(hist_acu(T:)) / total_pixeles # foreground
    
    ub = 0
    num_pixeles_b = 0
    for color in range(T):
        ub += color*hist[color]
        num_pixeles += hist[color]
    if num_pixeles_b == 0:
        ub = 0
    else:
        ub = ub / num_pixeles_b
        
    uf = 0
    num_pixeles_f = 0
    for color in range(T,256):
        ub += color*hist[color]
        num_pixeles += hist[color]
    if num_pixeles_b == 0:
        ub = 0
    else:
        ub = ub / num_pixeles_b    
        

cv.imshow("Original", img_gray)

while True:
    # Leemos del teclado
    key = cv.waitKey(1000)
    # Verificamos si la ventana es visible
    win =  cv.getWindowProperty('Original', cv.WND_PROP_VISIBLE)

    # si se preciona la tecla ESC
    if key == 27 or key == ord("q") or win < 1.0:
        break

cv.destroyAllWindows()

