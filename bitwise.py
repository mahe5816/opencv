import numpy as np
import cv2 as cv
blank=np.zeros((400,400),dtype='uint8')
rec=cv.rectangle(blank.copy(),(30,30),(350,350),255,-1)
cir=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('rec',rec)
cv.imshow('cir',cir)
bit_and=cv.bitwise_and(rec,cir)
cv.imshow('and',bit_and)
bit_or=cv.bitwise_or(rec,cir)
cv.imshow('or',bit_or)
cv.waitKey(0)