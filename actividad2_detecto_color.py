# ALUMNO : AGUILAR LUCIANO DAVID

import cv2
import numpy as np

# Utilizo la imagen ruta.jpg al no estar especificado en la actividad
ruta = cv2.imread('imagenes/ruta.jpg')

#ruta = cv2.imread('imagenes/cubo.jpg')

rutaHSV = cv2.cvtColor(ruta,cv2.COLOR_BGR2HSV)

yellowBajo1 = np.array([15,100,20],np.uint8)
yellowAlto1 = np.array([30,255,255],np.uint8)
yellowBajo2 = np.array([15,100,20],np.uint8)
yellowAlto2 = np.array([30,255,255],np.uint8)

maskYellow1 = cv2.inRange(rutaHSV,yellowBajo1,yellowAlto1)
maskYellow2 = cv2.inRange(rutaHSV,yellowBajo2,yellowAlto2)

maskYellow = cv2.add(maskYellow1,maskYellow2)

maskYellowvis = cv2.bitwise_and(ruta,ruta,mask=maskYellow)

cv2.imshow('original',ruta)
cv2.imshow('maskyellow',maskYellow)
cv2.imshow('maskyellowvis',maskYellowvis)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()