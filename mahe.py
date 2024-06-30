import cv2 as cv
img=cv.imread("koh.jpg")
def res(frame,sc=0.2):
    wid=int(frame.shape[1]*sc)
    he=int(frame.shape[0]*sc)
    dim=(wid,he)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)
cv.imshow('kohli',res(img))
#cv.waitKey(0)
import numpy as np
arr=np.zeros((500,500),dtype='uint8')
cv.imshow('bl',arr)
cv.waitKey(0)