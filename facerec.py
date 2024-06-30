import cv2 as cv
import numpy as np
import os
dir=r'C:\Users\Mahendra Reddy\image_clf'
face_cas=cv.CascadeClassifier('haarcascade_frontalface_default.xml')

p=[]
for file in os.listdir(dir):
    p.append(file)
print(p)
label=[]
feat=[]
def fac_tra():
    for per in p:
        path=os.path.join(dir,per)
        lab=p.index(per)
        for img in os.listdir(path):
            imgpath=os.path.join(path,img)
            image=cv.imread(imgpath)
            image=cv.resize(image,(800,600),interpolation=cv.INTER_AREA)
            gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
            face=face_cas.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
            for x,y,w,h in face:
                face_roi=gray[y:y+h,x:x+w]
                feat.append(face_roi)
                label.append(lab)
fac_tra()
print(len(feat))
print(len(label))
print("traing done------------->")
feat=np.array(feat,dtype='object')
label=np.array(label)
face_rec=cv.face.LBPHFaceRecognizer_create()
face_rec.train(feat,label)
face_rec.save('face_trained.yml')
np.save('feat.npy',feat)
np.save('label.npy',label)