#!/usr/bin/env python3

import cv2 as cv
import numpy as np

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara.")
    exit(1)


# Rango bajo (rojos anaranjados)
bajo_rojo1 = np.array([0, 100, 100])
alto_rojo1 = np.array([10, 255, 255])
    
# Rango alto (rojos violáceos)
bajo_rojo2 = np.array([160, 100, 100])
alto_rojo2 = np.array([179, 255, 255])


while True:
    # Leeo la imagen de la camara
    retorno, imagen = camara.read()

    if not retorno:
        print("No puedo capturar la imagen de la camara")
        break

    hsv = cv.cvtColor(imagen, cv.COLOR_BGR2HSV)
        
    mascara1 = cv.inRange(hsv, bajo_rojo1, alto_rojo1)
    mascara2 = cv.inRange(hsv, bajo_rojo2, alto_rojo2)
    
    mascara_final = cv.add(mascara1, mascara2)


    mascara_final2 = cv.inRange(hsv, np.array([144, 76, 0]),
                                 np.array([179,255,255]))

    resultado = cv.bitwise_and(imagen, imagen, mask=mascara_final)
    resultado2 = cv.bitwise_and(imagen, imagen, mask=mascara_final2)

    cv.imshow("Camara", imagen)
    cv.imshow("Rojo", resultado)
    cv.imshow("Rojo 2", resultado2)

    # Salgo del programa oprimiendo la tecla ESC
    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()
