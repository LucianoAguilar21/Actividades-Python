# ALUMNO : AGUILAR LUCIANO DAVID

import cv2

patente=[]
vehiculo = cv2.imread('imagenes/vehiculo.jpg')


# Buscar los las filas y columnas en los pixeles
vehiculoOut = vehiculo[130:160,105:180]
cv2.imshow('Vehiculo',vehiculo)
cv2.imshow('patente recordata',vehiculoOut)
cv2.imwrite('patente.png',vehiculoOut)

cv2.waitKey(0)
cv2.destroyAllWindows()