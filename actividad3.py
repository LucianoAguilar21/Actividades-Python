# ALUMNO : AGUILAR LUCIANO DAVID

import cv2
import numpy as np

cubo = cv2.imread('imagenes/cubo.jpg')

cuboHSV = cv2.cvtColor(cubo,cv2.COLOR_BGR2HSV)

azulBajo1 = np.array([100,50,50],np.uint8)
azulAlto1 = np.array([119,255,255],np.uint8)
azulBajo2 = np.array([120,100,20],np.uint8)
azulAlto2 = np.array([130,255,255],np.uint8)

maskAzul1 = cv2.inRange(cuboHSV,azulBajo1,azulAlto1)
maskAzul2 = cv2.inRange(cuboHSV,azulBajo2,azulAlto2)

maskAzul = cv2.add(maskAzul1,maskAzul2)

maskAzulvis = cv2.bitwise_and(cubo,cubo,mask=maskAzul)


cv2.imshow('original',cubo)
cv2.imshow('maskAzul',maskAzul)
cv2.imshow('maskAzulvis',maskAzulvis)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()