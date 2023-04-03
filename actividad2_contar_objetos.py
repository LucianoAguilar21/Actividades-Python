# ALUMNO : AGUILAR LUCIANO DAVID

import cv2


imagen = cv2.imread('imagenes/monedas2.jpg')



imagengris= cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)


bordes = cv2.Canny(imagengris,100,200)

bordes = cv2.dilate(bordes,None,iterations=1)
bordes = cv2.erode(bordes,None,iterations=1)


contornos,jerarquia = cv2.findContours(bordes,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)



cv2.drawContours(imagen,contornos,-1,(0,0,255),2)

texto = 'contornos encontrados: ' + str(len(contornos))
cv2.putText(imagen,texto,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
cv2.imshow('imagen',imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()