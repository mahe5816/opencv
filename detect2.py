#import pandas as pd
import numpy as np
#import cv2 as cv
#people=['Shubman_Gill', 'Virat_Kohli','Mahendra']
#face_cas=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
#img=cv.imread(r'C:\Users\Mahendra Reddy\image_clf\Virat_Kohli\th_id=OIP (13).jpg')
#feat=np.load('feat.npy',allow_pickle=True)
#label=np.load('label.npy',allow_pickle=True)
#face_rec=cv.face.LBPHFaceRecognizer_create()
#face_rec.read('face_trained.yml')
#gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#cv.imshow("gray",gray)
import cv2 as cv

# Load the cascade classifier for face detection
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the trained face recognition model
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# Define the list of people's names
people = ['Shubman_Gill', 'Virat_Kohli', 'Mahendra','Manikanta']

# Open the video capture device (webcam)
video = cv.VideoCapture(0)

while True:
    # Read a frame from the video
    check, frame = video.read()
    
    img=cv.resize(frame,(800,600),interpolation=cv.INTER_AREA)
    # Convert the frame to grayscale for face detection
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #gray=cv.resize(gray,(800,600),interpolation=cv.INTER_LINEAR)
    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Iterate through detected faces
    for x, y, w, h in faces:
        # Extract the region of interest (ROI) for face recognition
        face_roi = gray[y:y+h, x:x+w]

        # Recognize the face using the trained model
        label, confidence = face_recognizer.predict(face_roi)

        # Print the label and confidence level
        print(f'Label: {label}, Confidence: {confidence}')

        # Draw a rectangle around the detected face
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

        # Put text label on the frame indicating the recognized person
        cv.putText(img, people[label], (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame with rectangles and labels
    cv.imshow("Face Recognition", img)

    # Check for key press 'q' to exit the loop
    key = cv.waitKey(1)
    if key == ord('q'):
        break

# Release the video capture device and close all OpenCV windows
video.release()
cv.destroyAllWindows()
