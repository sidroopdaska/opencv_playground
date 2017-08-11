import cv2
import numpy as np

banana_cascade = cv2.CascadeClassifier('banana_classifier.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bananas = banana_cascade.detectMultiScale(gray, 2, 5)
    for (x,y,w,h) in bananas:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0, 255), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()