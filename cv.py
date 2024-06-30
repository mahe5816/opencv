import cv2 as cv
v=cv.VideoCapture("wonder.mp4")
def res(frame,sc=0.2):
    wid=int(frame.shape[1]*sc)
    he=int(frame.shape[0]*sc)
    dim=(wid,he)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)
while True:
    isT,frame=v.read()
    cv.imshow('xx',frame)
    ress=res(frame)
    cv.imshow('xxx',ress)
    key=cv.waitKey(1)
    if key==ord("d"):
        break