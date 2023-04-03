# ALUMNO : AGUILAR LUCIANO DAVID

import cv2

# Opcion 0 para utilizar la camara de la notebook
video = cv2.VideoCapture(0)

while (video.isOpened()):
    ret , frame = video.read()

    if ret == True:
        cv2.putText(frame,"En vivo:",(5,30),1,1.5,(0,0,255),1)
        cv2.imshow('En vivo',frame)
        if cv2.waitKey(50) == ord('s'):
            break
    else: break

video.release()
cv2.destroyAllWindows()