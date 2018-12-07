# -*- coding: utf-8 -*-

import cv2

cap = cv2.VideoCapture(0)
i = 0

while(True):
    
    ret, im = cap.read()
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    cv2.imshow('im',im)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        i += 1 
        nom_im = 'C:/Users/etien/Desktop/PJT - Ironcar/Image saved/image{}.png'.format(i)
        print(nom_im)
        status = cv2.imwrite(nom_im,im)
        print("Image written to file-system : ",status)

cap.release()
cv2.destroyAllWindows()