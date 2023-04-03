# ALUMNO : AGUILAR LUCIANO DAVID

import cv2
import time
video = cv2.VideoCapture('video/video.mp4')

fps_s_t = 0
fps = 0

while (video.isOpened()):
    ret , frame = video.read()

    fps_en_t = time.time()
    fps = 1/(fps_en_t - fps_s_t)
    fps_s_t = fps_en_t

    
    #fps_text = "FPS : {:.2f}".format(fps)
    fps = "FPS: {:.2f}".format(fps)
    if ret :
        #cv2.putText(frame,fps_text,(80,60),1,1.5,(0,255,0),2)
        cv2.putText(frame,fps,(5,30),1,1.5,(0,0,0),1)
        cv2.putText(frame,"Ancho: "+str(video.get(3)),(5,60),1,1.5,(0,0,0),1)
        cv2.putText(frame,"Alto: "+str(video.get(4)),(5,90),1,1.5,(0,0,0),1)
        cv2.imshow('Propiedades',frame)
        
        if cv2.waitKey(50) == ord('s'):
            break
    else: break

video.release()
cv2.destroyAllWindows()