#!/usr/bin/env python3
import cv2 as cv
import numpy as np

def rgb_to_hsv(img_rgb):
    """
    Convierte una imagen de RGB a HSV utilizando NumPy.
    La imagen de entrada debe ser uint8 [0, 255].
    La imagen de salida HSV sigue la convención de OpenCV:
    H: 0-179, S: 0-255, V: 0-255.
    """
    # 1. Normalizar los valores RGB al rango [0, 1]
    img = img_rgb.astype(np.float32) / 255.0
    
    # Separar los canales
    r = img[:,:,0]
    g = img[:,:,1]
    b = img[:,:,2]
    
    # 2. Encontrar el valor Máximo y Mínimo por píxel
    max_c = np.max(img, axis=2)
    min_c = np.min(img, axis=2)
    delta = max_c - min_c  # Diferencia (Croma)
    
    # Inicializar matrices H, S, V con ceros
    h = np.zeros_like(max_c)
    s = np.zeros_like(max_c)
    v = max_c  # El Valor es simplemente el máximo de RGB
    
    # 3. Calcular la Saturación (S)
    # Evitar división por cero donde max_c es 0 (negro puro)
    with np.errstate(invalid='ignore', divide='ignore'):
        s = np.where(max_c == 0, 0, delta / max_c)
    
    # 4. Calcular el Matiz (H)
    # El cálculo depende de qué canal es el máximo.
    
    # Caso 1: Delta es 0 (R=G=B, escala de grises), H es 0
    # Caso 2: Max es Rojo
    idx_r = (max_c == r) & (delta != 0)
    h[idx_r] = (g[idx_r] - b[idx_r]) / delta[idx_r]
    
    # Caso 3: Max es Verde
    idx_g = (max_c == g) & (delta != 0)
    h[idx_g] = 2.0 + (b[idx_g] - r[idx_g]) / delta[idx_g]
    
    # Caso 4: Max es Azul
    idx_b = (max_c == b) & (delta != 0)
    h[idx_b] = 4.0 + (r[idx_b] - g[idx_b]) / delta[idx_b]
    
    # Ajustar H para que sea positivo y convertir a grados (0-360)
    h = (h / 6.0) % 1.0  # Normalizar a [0, 1]
    
    # 5. Escalar a los rangos de OpenCV (8 bits)
    # OpenCV usa H: 0-179 (para que quepa en un byte, 360/2), S: 0-255, V: 0-255
    h_final = (h * 179).astype(np.uint8)
    s_final = (s * 255).astype(np.uint8)
    v_final = (v * 255).astype(np.uint8)
    
    # Combinar los canales
    hsv_img = cv.merge([h_final, s_final, v_final])
    
    return hsv_img

# --- Ejemplo de uso y comparación ---

# 1. Cargar imagen y convertir a RGB
img_bgr = cv.imread('img/color_wheel.png') # Usa una imagen con muchos colores
img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)

# 2. Nuestra conversión manual
hsv_manual = rgb_to_hsv(img_rgb)

# 3. La conversión oficial de OpenCV (¡mucho más rápida!)
hsv_opencv = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)

# 4. Visualización
# Separar canales para ver qué información contienen
H, S, V = cv.split(hsv_manual)

cv.imshow('Original RGB', img_bgr)
cv.imshow('Canal H (Matiz)', H)
cv.imshow('Canal S (Saturacion)', S)
cv.imshow('Canal V (Valor)', V)
cv.imshow('Resultado HSV Manual', hsv_manual)
cv.imshow('Resultado HSV OpenCV', hsv_opencv)

# Verificar si los resultados son similares
diferencia = cv.absdiff(hsv_manual, hsv_opencv)
cv.imshow('Diferencia (debe ser casi negra)', diferencia)

cv.waitKey(0)
cv.destroyAllWindows()
