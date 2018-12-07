#-*- coding: utf-8 -*-
import cv2
 
# Choix du périphérique de capture. 0 pour /dev/video0.
cap = cv2.VideoCapture(0)
 
while True:
 
    # On capture l'image.
    ret,im = cap.read()
 
    # on met l'image en gris 
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # On l'affiche.
    cv2.imshow('Webcam',im)
    cv2.imshow('WebcamGray',gray)
    
 
    # Lorsqu'on appuis sur "q" ca ferme la fenetre camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Tout fermer
cap.release()
cv2.destroyAllWindows()