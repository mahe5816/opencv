import cv2 as cv
import numpy as np
img=cv.imread('cat.jpg')
img=cv.resize(img,(800,500),interpolation=cv.INTER_AREA)
cv.imshow("ori",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cann=cv.Canny(gray,125,175)
cv.imshow("canny",cann)
counter,thresh=cv.findContours(cann,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(counter))
#using threshold
ret,thresh=cv.threshold(gray,125,225,cv.THRESH_BINARY)
cv.imshow("thresh",thresh)
#using findcounters
blank=np.zeros(img.shape,dtype='uint8')
pp=cv.drawContours(blank,counter,-1,(0,0,255),1)
cv.imshow("own",pp)
cv.waitKey(0)