import cv2 as cv
import numpy as np
height,width=720,1280
vid=cv.VideoCapture(0)
vid.set(3,width)
vid.set(4,height)
path="pho"
import os
photos=os.listdir(path)
print(photos)
imgno=0
hs,wa=int(120*1),int(213*1)
from cvzone.HandTrackingModule import HandDetector
det=HandDetector(detectionCon=.8,maxHands=5)
ges=300
next=False
nextno=0
delay=10
points=[[]]
anns=False
annno=-1
while True:
    che,img=vid.read()
    img=cv.flip(img,1)
    
    #key=cv.waitKey(1)
    imgpath=os.path.join(path,photos[imgno])
    curimg=cv.imread(imgpath)
    ppp=cv.resize(curimg,(1280,720))
    hand,img=det.findHands(img,flipType=False)
    h,w,_=ppp.shape

    cv.line(img,(0,ges),(width,ges),(0,255,0),10)
    if hand and next is False:
        han=hand[0]
        lmst=han['lmList']
        index=lmst[8][0],lmst[8][1]
        hh=det.fingersUp(han)
        cx,cy=han['center']
        xval=int(np.interp(index[0],(width//2,w),(0,width)))
        yval=int(np.interp(index[1],(150,height-150),(0,height)))
        indexx=xval,yval
        #print(hh)
        if cy:
            #anns=False
            if hh==[0,0,0,0,0]:
                next=True
                anns=False
                if imgno>0:
                    points=[[]]
                    
                    annno=-1
                    imgno-=1
            if hh==[1,0,0,0,1]:
                next=True
                anns=False
                if imgno<len(photos)-1:
                    points=[[]]
                    
                    annno=-1
                    imgno+=1
            if hh==[1,1,1,0,0]:
                anns=False
                cv.circle(ppp,index,12,(0,0,255),cv.FILLED)
                #cv.circle(img,index,12,(0,0,255),cv.FILLED)
            if hh==[1,1,0,0,0]:
                if anns is False:
                    anns=True
                    annno+=1
                    points.append([])
                cv.circle(ppp,index,12,(0,0,255),-1)
                points[annno].append(index)
            else:
                anns=False
            if hh==[1,1,1,1,0]:
                if points:
                    points.pop(-1)
                    annno-=1
                    anns=True
        else:
            anns=False
           # if hh==[1,1,1,1,0]:
            #    points.pop()

    if next:
        nextno+=1
        if nextno>delay:
            nextno=0
            next=False
    for i in range(len(points)):
        for j in range(len(points[i])):
          if j!=0:
            cv.line(ppp,points[i][j-1],points[i][j],(0,255,255),10)
    imgsmall=cv.resize(img,(wa,hs))
    
    ppp[0:hs,w-wa:w]=imgsmall
    cv.imshow("normal",img)
    cv.imshow("cur",ppp)
    key=cv.waitKey(1)
    #key = cv.waitKey(1)
    if key == ord('q'):
        break
#cv.release()
vid.release()
cv.destroyAllWindows()