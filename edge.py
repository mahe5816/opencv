import cv2 as cv
import numpy as np
img=cv.imread('cat.jpg')
img=cv.resize(img,(800,600),interpolation=cv.INTER_AREA)
cv.imshow('cat',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('lap',lap)
#sobel
sobx=cv.Sobel(gray,cv.CV_64F,1,0)
soby=cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow('sobx',sobx)
cv.imshow('soby',soby)
com=cv.bitwise_or(sobx,soby)
cv.imshow("com",com)
cv.waitKey(0)