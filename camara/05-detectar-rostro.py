#!/usr/bin/env python3

import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara.")
    exit(1)

detector = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    # Leeo la imagen de la camara
    retorno, imagen = camara.read()

    if not retorno:
        print("No puedo capturar la imagen de la camara")
        break

    grises = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    caras  = detector.detectMultiScale(grises, 1.1, 4)

    for (x,y, w,h) in caras:
        cv.rectangle(imagen, (x,y), (x+w,y+h), (255,0,0), 2)

    cv.imshow("Camara", imagen)

    # Salgo del programa oprimiendo la tecla ESC
    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()
