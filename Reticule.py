import cv2
 
# setup video capture
cap = cv2.VideoCapture(0)

 
while True:
     
    ret,im = cap.read()
    height, width = im.shape[:2]
    # trait horizontal
    for i in range(width):
        im[height/2][i] = [0,0,0]
 
    # trait vertical
    for i in range(height):
        im[i][width/2] = [0,0,0]
 
    cv2.imshow('video test',im)
    
    # Lorsqu'on appuis sur "q" ca ferme la fenetre camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Tout fermer
cap.release()
cv2.destroyAllWindows()