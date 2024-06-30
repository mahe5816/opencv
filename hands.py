import cv2 as cv
import mediapipe as mp
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mp_hands=mp.solutions.hands
cap=cv.VideoCapture(0)
hands=mp_hands.Hands()
while True:
    check,frame=cap.read()
    img=cv.flip(frame,1)
    res=hands.process(img)
    if res.multi_hand_landmarks:
        for hand_landmarks in res.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img,hand_landmarks,mp_hands.HAND_CONNECTIONS)
    cv.imshow("pkdo",img)
    cv.waitKey(1)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
