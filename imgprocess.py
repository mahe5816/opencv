import cv2 as cv
img=cv.imread('koh.jpg')
def res(frame,sc=0.2):
    wid=int(frame.shape[1]*sc)
    he=int(frame.shape[0]*sc)
    dim=(wid,he)
    return cv.resize(frame,dim)
cv.imshow("bgr",res(img))
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",res(gray))
#blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("blur",res(blur))
#canny
cann=cv.Canny(blur,125,175)
cv.imshow("cann",res(cann))
#dilate
dilated=cv.dilate(cann,(7,7,),iterations=3)
cv.imshow("dil",res(dilated))
cv.waitKey(0)