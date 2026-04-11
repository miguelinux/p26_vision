#!/usr/bin/env python3
import cv2 as cv
import numpy as np

def otsu_threshold(image):
    # 1. Calcular el histograma y las probabilidades
    # Suponemos una imagen de 8 bits (256 niveles de gris)
    hist = cv.calcHist([image], [0], None, [256], [0, 256]).ravel()
    prob = hist / np.sum(hist)

    # Inicializar variables
    max_variance = -1
    threshold = 0

    # 2. Iterar sobre todos los posibles umbrales (0 a 255)
    for t in range(256):
        # Clase 1: Fondo (Background) - de 0 a t
        # Clase 2: Objeto (Foreground) - de t+1 a 255

        w0 = np.sum(prob[:t])      # Peso de la clase 1
        w1 = np.sum(prob[t:])      # Peso de la clase 2

        if w0 == 0 or w1 == 0:
            continue

        # Medias de las clases
        mu0 = np.sum(np.arange(t) * prob[:t]) / w0
        mu1 = np.sum(np.arange(t, 256) * prob[t:]) / w1

        # 3. Calcular la varianza entre clases (Between-class variance)
        # Fórmula: σb² = w0 * w1 * (mu0 - mu1)²
        variance = w0 * w1 * ((mu0 - mu1) ** 2)

        # 4. Maximizar la varianza
        if variance > max_variance:
            max_variance = variance
            threshold = t

    return threshold


# Cargar imagen en escala de grises
img = cv.imread('img/monedas.jpg', cv.IMREAD_GRAYSCALE)

# Calcular umbral manualmente con nuestra función
umbral_otsu = otsu_threshold(img)
print(f"El umbral óptimo calculado es: {umbral_otsu}")

# Aplicar el umbral a la imagen
img_bin = np.zeros(img.shape).astype("uint8")

img_bin[img > umbral_otsu] = 255
#_, img_bin = cv.threshold(img, umbral_otsu, 255, cv.THRESH_BINARY)

# Versión ultra rápida de OpenCV
#valor_umbral, img_otsu = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

cv.imshow("Original", img)
cv.imshow("Binaria", img_bin)

while True:
    # Leemos del teclado
    key = cv.waitKey(1000)
    # Verificamos si la ventana es visible
    win =  cv.getWindowProperty('Original', cv.WND_PROP_VISIBLE)

    # si se preciona la tecla ESC
    if key == 27 or key == ord("q") or win < 1.0:
        break

cv.destroyAllWindows()
