# -*- coding: utf-8 -*-

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def CdG1( mask, width, height):
    
    x,y,C = 0,0,0
    for i in range(width) :
        for j in range(height) :
            if mask[j,i] :
                x = i + x
                y = j + y
                C = C + 1
    if C :
        return x/C, y/C
    return

while(1):
    
    _, frame = cap.read()

#======FILTRE D'IMAGE==========================================================

    height, width, _ = frame.shape
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#[hue, saturation,value]    si on diminu la saturation, on devient plus selectif

    lower = np.array([0,0,150])
    upper = np.array([175,60,255])
    
    mask = cv2.inRange(hsv, lower, upper)
    
    res = cv2.bitwise_and(frame,frame, mask= mask)
    dil = cv2.dilate(res, None, iterations=5)
    ero = cv2.erode(dil, None, iterations=5)
    median = cv2.medianBlur(ero,15)
    
#=======DECOUPE DE L'IMAGE=====================================================

    #gauche à droite comme direction x et de haut en bas comme direction y
    roi = median[0:int(height), int(width)//3:int(width*2/3)]
    
#=======FILTRE BINAIRE D'IMAGE=================================================

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
#cv2.adaptiveThreshold(image, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) → dst
#dst – Destination image of the same size and the same type as src
#maxValue – Non-zero value assigned to the pixels for which the condition is satisfied. See the details below
#adaptiveMethod – Adaptive thresholding algorithm to use, ADAPTIVE_THRESH_MEAN_C or ADAPTIVE_THRESH_GAUSSIAN_C
#thresholdType – Thresholding type that must be either THRESH_BINARY or THRESH_BINARY_INV
#blockSize – Size of a pixel neighborhood that is used to calculate a threshold value for the pixel: 3, 5, 7, and so on
#C – Constant subtracted from the mean or weighted mean

#    _,th = cv2.threshold(gray,250,255,cv2.THRESH_BINARY)
    th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,11,0)
    dilth = cv2.dilate(th, None, iterations=8)
    eroth = cv2.erode(dilth, None, iterations=5)   

#======CALCUL CdG==============================================================

    h, l = th.shape
    
    try:
        x, y = CdG1(th,l,h)
#circle(image,centre,taille,[B,G,R],epaisseur)
        cv2.circle(roi,(x,y),4,(0,0,255),-1)
    except:
        pass
#======ORDRE POUR LE DEPLACEMENT===============================================
#=====> On prend que le x
    mid = int(l)/2
#variation relative du CdG par rapport au milieu
    delta = int(mid) - x
    intensity = int(abs(delta/107.*1000))
    if intensity > 1000: intensity = 1000
    if delta>0:
        print("gauche", intensity)
    elif delta<0:
        print("droite", intensity)
    else:
        pass

#=======AFFICHAGE IMAGE========================================================

#    cv2.imshow('image',frame)
#    cv2.imshow('imageROI',roi)
    cv2.imshow('filter',eroth)

#==============================================================================

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()