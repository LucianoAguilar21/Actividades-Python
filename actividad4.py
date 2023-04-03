# ALUMNO : AGUILAR LUCIANO DAVID

import cv2

imagen = cv2.imread('imagenes/ruta.jpg')

imagengris= cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

bordes = cv2.Canny(imagengris[0:215,00:250],100,500)
bordes2 = cv2.Canny(imagengris[218:320,100:200],100,500)


contornos,_= cv2.findContours(bordes,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contornos2,_ = cv2.findContours(bordes2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen,contornos,-1,(0,255,0),2)
cv2.drawContours(imagen[218:320,100:200],contornos2,-1,(0,255,0),2)

texto = 'Alerta al conductor'

cv2.putText(imagen,texto,(170,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

cv2.imshow('Imagen contornos',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()