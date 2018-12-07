import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, im = cap.read()
    
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(im,5)

    ret,th1 = cv2.threshold(gray,254,255,cv2.THRESH_BINARY)
    ret,th2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    ret,th3 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
    ret,th4 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
    ret,th5 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO_INV)
    th6 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    th7 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    # Display the resulting frame
    cv2.imshow('im',im)
    cv2.imshow('img',img)
    cv2.imshow('gray',gray)
    
    cv2.imshow('th1',th1)
    cv2.imshow('th2',th2)
    cv2.imshow('th3',th3)
    cv2.imshow('th4',th4)
    cv2.imshow('th5',th5)
    cv2.imshow('th6',th6)
    cv2.imshow('th7',th7)
    
    # Lorsqu'on appuis sur "q" ca ferme la fenetre camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Tout fermer
cap.release()
cv2.destroyAllWindows()