#!/usr/bin/env python3
import cv2
import numpy as np

# 1. Cargar la imagen
imagen = cv2.imread('img/ball_red.png')

if imagen is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta.")
else:
    # 2. Convertir de BGR (formato nativo de OpenCV) a HSV
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    # 3. Definir los rangos del color ROJO
    # Nota: El rojo es especial porque está en ambos extremos del
    #       espectro Hue (0 y 180)
    
    # Rango bajo (rojos anaranjados)
    bajo_rojo1 = np.array([0, 100, 100])
    alto_rojo1 = np.array([10, 255, 255])
    
    # Rango alto (rojos violáceos)
    bajo_rojo2 = np.array([160, 100, 100])
    alto_rojo2 = np.array([179, 255, 255])

    # 4. Crear las máscaras
    mascara1 = cv2.inRange(hsv, bajo_rojo1, alto_rojo1)
    mascara2 = cv2.inRange(hsv, bajo_rojo2, alto_rojo2)
    
    # Unir ambas máscaras para captar todo el espectro del rojo
    mascara_final = cv2.add(mascara1, mascara2)

    mascara_final2 = cv2.inRange(hsv, np.array([144, 76, 0]),
                                 np.array([179,255,255]))

    # 5x5 kernel de unos
    kernel = np.ones((5,5), np.uint8)

    dilatacion = cv2.dilate(mascara_final2, kernel, iterations=1)


    # 5. Aplicar la máscara a la imagen original (Bitwise AND)
    resultado = cv2.bitwise_and(imagen, imagen, mask=mascara_final)
    resultado2 = cv2.bitwise_and(imagen, imagen, mask=mascara_final2)
    resultado3 = cv2.bitwise_and(imagen, imagen, mask=dilatacion)

    # 6. Mostrar los resultados
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Mascara (Blanco y Negro)', mascara_final)
    cv2.imshow('Segmentacion Roja', resultado)
    cv2.imshow('Segmentacion Roja 2', resultado2)
    cv2.imshow('Segmentacion Roja 3', resultado3)

    # Esperar a que se presione una tecla y cerrar ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()
