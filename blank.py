import cv2 as cv
import numpy as np
arr=np.zeros((500,500,3),dtype='uint8')
cv.imshow('bl',arr)
arr[:]=0,255,0
cv.imshow('gr',arr)
arr[:]=255,0,0
cv.imshow('bl',arr)
arr[:]=0,0,255
cv.imshow('red',arr)
arr=np.zeros((500,500,3),dtype='uint8')
arr[200:300,300:400]=0,0,255
cv.imshow('jii',arr)
cv.waitKey(0)