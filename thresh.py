import cv2 as cv
import numpy as np
img=cv.imread('koh.jpg')
img=cv.resize(img,(800,600),interpolation=cv.INTER_AREA)
cv.imshow('ori',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
thr,the=cv.threshold(gray,150,225,cv.THRESH_BINARY)
cv.imshow("thre",the)
thinv,theinv=cv.threshold(gray,150,225,cv.THRESH_BINARY_INV)
cv.imshow("inv",theinv)
#adaptive thresh
ada=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,13,3)
cv.imshow("ada",ada)
cv.waitKey(0)