#!/usr/bin/env python3
import cv2 as cv
import numpy as np

def rgb_to_ycbcr(image_rgb):
    # 1. Convertir a flotante para precisión en el cálculo
    img = image_rgb.astype(np.float32)
    
    # 2. Definir la matriz de transformación (Estándar BT.601)
    # Nota: Los pesos están diseñados para que Y esté en [0, 255]
    # y Cb, Cr centrados mediante el offset de 128.
    
    transform_matrix = np.array([[ 0.299,     0.587,     0.114],
                                 [-0.168736, -0.331264,  0.5],
                                 [ 0.5,      -0.418688, -0.081312]])
    
    # 3. Aplicar el producto punto (dot product) entre la imagen y la matriz
    # Usamos .dot() sobre el último eje (los canales)
    ycbcr = img.dot(transform_matrix.T)
    
    # 4. Sumar los offsets para Cb y Cr
    ycbcr[:, :, 1] += 128
    ycbcr[:, :, 2] += 128
    
    return np.uint8(np.clip(ycbcr, 0, 255))

# --- Prueba del programa ---
# Cargar imagen (OpenCV carga en BGR por defecto, la pasamos a RGB)
img_bgr = cv.imread('img/baboon.png')
img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)

img_ycbcr = rgb_to_ycbcr(img_rgb)

# Separar canales para visualizarlos
Y, Cb, Cr = cv.split(img_ycbcr)

cv.imshow('Luminancia (Y)', Y)
cv.imshow('Croma Azul (Cb)', Cb)
cv.imshow('Croma Rojo (Cr)', Cr)
cv.waitKey(0)
cv.destroyAllWindows()
