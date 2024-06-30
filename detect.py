#import pandas as pd
import numpy as np
import cv2 as cv
people=['Shubman_Gill', 'Virat_Kohli','Mahendra']
face_cas=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv.imread(r'C:\Users\Mahendra Reddy\image_clf\Mahendra\WhatsApp Image 2024-05-04 at 22.13.35_5879a044.jpg')
feat=np.load('feat.npy',allow_pickle=True)
label=np.load('label.npy',allow_pickle=True)
face_rec=cv.face.LBPHFaceRecognizer_create()
face_rec.read('face_trained.yml')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
face=face_cas.detectMultiScale(gray,1.1,4)
cv.imshow("gray",gray)
for x,y,w,h in face:
    face_roi=gray[y:y+h,x:x+w]
    lab,con=face_rec.predict(face_roi)
    print(f'label={lab} with confi {con}')
    cv.putText(img,str(people[lab]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),3)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv.imshow("after",img)
cv.waitKey(0)