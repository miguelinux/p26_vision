#!/usr/bin/env python3
import cv2 as cv
import numpy as np

def convolution_fnc(img, kernel):

    # input size
    img_rows, img_cols = img.shape

    kernel = np.flip(kernel, axis = 0)
    kernel = np.flip(kernel, axis = 1)

    # kernel size
    rows_kernel, cols_kernel = kernel.shape

    # obtener la salida
    out_cols = int(img_cols - cols_kernel + 1)
    out_rows = int(img_rows - rows_kernel + 1)

    # output img
    img_output =   np.zeros([out_rows, out_cols]).astype("float")
    img = img.astype("float")

    # index calulation
    index_rows = np.linspace(0, img_rows - rows_kernel, img_output.shape[0]).astype("int")
    index_cols = np.linspace(0, img_cols - cols_kernel, img_output.shape[1]).astype("int")

    for rows in range(out_rows):
        for cols in range(out_cols):
            img_output[rows, cols] = np.sum(
                np.sum(
                    kernel * img[index_rows[rows]:index_rows[rows] + kernel.shape[0],
                    index_cols[cols]:index_cols[cols] + kernel.shape[1]]
                )
            )

    return img_output.astype("uint8")


img = cv.imread("img/davis_hall.jpeg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sobel_x = np.array([[ -1., 0., 1.],
                    [ -2., 0., 2.],
                    [ -1., 0., 1.]])

sobel_y = sobel_x.T

img_x = convolution_fnc(img_gray, sobel_x).astype("float")
img_y = convolution_fnc(img_gray, sobel_y).astype("float")

gradient = np.sqrt(img_x * img_x + img_y * img_y)

img_edges = np.zeros(gradient.shape).astype("uint8")

img_edges[gradient > 200] = 255

img_gradient = gradient.astype("uint8")

cv.imshow("Original", img_gray)
cv.imshow("Gradient", img_gradient)
cv.imshow("Edges", img_edges)

while True:
    # Leemos del teclado
    key = cv.waitKey(1000)
    # Verificamos si la ventana es visible
    win =  cv.getWindowProperty('Original', cv.WND_PROP_VISIBLE)

    # si se preciona la tecla ESC
    if key == 27 or key == ord("q") or win < 1.0:
        break

cv.destroyAllWindows()

