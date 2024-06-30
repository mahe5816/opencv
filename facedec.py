import cv2 as cv
import numpy as np
fac=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv.imread('koh.jpg')
img=cv.resize(img,(800,600),interpolation=cv.INTER_AREA)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces=fac.detectMultiScale(gray,1.1,5)
print(len(faces))
for x,y,w,h in faces:
    img2=cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('img2',img2)
cv.waitKey(0)