import cv2 as cv
import numpy as np
arr=np.zeros((500,500,3),dtype='uint8')
img=cv.rectangle(arr,(0,0),(250,500),(0,255,0),thickness=5)
cv.imshow('rec',img)
img=cv.rectangle(arr,(0,0),(250,500),(0,255,0),thickness=cv.FILLED)
cv.imshow('recfil',img)
pp=cv.circle(arr,(250,250),40,(0,0,255),thickness=-1)
cv.imshow("cir",pp)
arr=np.zeros((500,500,3),dtype='uint8')
cv.putText(arr,"Hello",(0,100),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
cv.imshow("tex",arr)
cv.waitKey(0)