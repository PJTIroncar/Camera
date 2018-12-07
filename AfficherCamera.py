import cv2

cap = cv2.VideoCapture(0)

while True :
    ret,img = cap.read()

    cv2.imshow("Je suis la camera de l'ordinateur d'Etienne",img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
