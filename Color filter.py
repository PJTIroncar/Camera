# -*- coding: utf-8 -*-

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#[hue, saturation,value]    

    lower = np.array([0,0,0])
    upper = np.array([150,50,255])
    
#☼    lower = np.array([10,,])
#    upper = np.array([255,255,255])
    
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame,frame, mask= mask)

#    bilateral = cv2.bilateralFilter(res,15,75,75)
    
    median = cv2.medianBlur(res,15)
    
    kernel = np.ones((5,5),np.uint8)
    
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#    cv2.imshow('hsv',hsv)
#    cv2.imshow('mask',mask)
#    cv2.imshow('res',res)
#    cv2.imshow('bilateral Blur',bilateral)
    cv2.imshow('Median Blur',median)
    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()