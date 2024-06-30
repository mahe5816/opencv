import cv2 as cv
import numpy as np
img=cv.imread('koh.jpg')
img=cv.resize(img,(1000,800))
cv.imshow('ori',img)
def tr(img,x,y):
    tm=np.float32([[1,0,x],[0,1,y]])
    dim=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,tm,dim)
# +x right , -x left
# +y down  , -y up
cv.imshow("tra",tr(img,100,100))
# rotating an image
def rot(img,ang,point=None):
    he,we=img.shape[:2]
    if point==None:
        point=(we//2,he//2)
    mat=cv.getRotationMatrix2D(point,ang,1.0)
    return cv.warpAffine(img,mat,(we,he))
cv.imshow("rot",rot(img,45))
cv.imshow("rott",rot(img,90))
# fliping an image
# 0 up down , 1 side side
flp=cv.flip(img,0)
cv.imshow("flip",flp)
flpp=cv.flip(img,-1)
cv.imshow("flipp",flpp)
cv.waitKey(0)