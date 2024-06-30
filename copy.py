import cv2 as cv
import numpy as np
from collections import deque

def setValues(x):
    pass

# Create a window for trackbars
cv.namedWindow("Color detectors")
cv.createTrackbar("upper hue", "Color detectors", 153, 180, setValues)
cv.createTrackbar("upper sat", "Color detectors", 255, 255, setValues)
cv.createTrackbar("upper value", "Color detectors", 255, 255, setValues)
cv.createTrackbar("lower hue", "Color detectors", 64, 180, setValues)
cv.createTrackbar("lower sat", "Color detectors", 72, 255, setValues)
cv.createTrackbar("lower value", "Color detectors", 49, 255, setValues)

# Create deques to store points
bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]

# Define colors for painting
col = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
b_i = 0
g_i = 0
r_i = 0
y_i = 0
ker = np.ones((5, 5), dtype='uint8')
col_i = 0

# Create a white canvas
paintwindow = np.ones((471, 636, 3), dtype=np.uint8) * 255

# Draw buttons on the canvas
paintwindow = cv.rectangle(paintwindow, (40, 1), (140, 65), (0, 0, 0), 2)
paintwindow = cv.rectangle(paintwindow, (160, 1), (255, 65), col[0], -1)
paintwindow = cv.rectangle(paintwindow, (275, 1), (370, 65), col[1], -1)
paintwindow = cv.rectangle(paintwindow, (390, 1), (485, 65), col[2], -1)
paintwindow = cv.rectangle(paintwindow, (505, 1), (600, 65), col[3], -1)

cv.namedWindow('paint', cv.WINDOW_AUTOSIZE)

cap = cv.VideoCapture(0)

while True:
    check, frame = cap.read()
    frame = cv.flip(frame, 1)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Get current positions of the trackbars
    u_hue = cv.getTrackbarPos("upper hue", "Color detectors")
    u_sat = cv.getTrackbarPos("upper sat", "Color detectors")
    u_value = cv.getTrackbarPos("upper value", "Color detectors")
    l_hue = cv.getTrackbarPos("lower hue", "Color detectors")
    l_sat = cv.getTrackbarPos("lower sat", "Color detectors")
    l_value = cv.getTrackbarPos("lower value", "Color detectors")

    upper_hsv = np.array([u_hue, u_sat, u_value])
    lower_hsv = np.array([l_hue, l_sat, l_value])

    # Draw buttons on the frame
    frame = cv.rectangle(frame, (40, 1), (140, 65), (0, 0, 0), 2)
    frame = cv.rectangle(frame, (160, 1), (255, 65), col[0], -1)
    frame = cv.rectangle(frame, (275, 1), (370, 65), col[1], -1)
    frame = cv.rectangle(frame, (390, 1), (485, 65), col[2], -1)
    frame = cv.rectangle(frame, (505, 1), (600, 65), col[3], -1)

    mask = cv.inRange(hsv, lower_hsv, upper_hsv)
    mask = cv.erode(mask, ker, iterations=1)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, ker)
    mask = cv.dilate(mask, ker, iterations=1)

    cnts, _ = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    center = None

    if len(cnts) > 0:
        cnt = sorted(cnts, key=cv.contourArea, reverse=True)[0]
        ((x, y), radius) = cv.minEnclosingCircle(cnt)
        cv.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        m = cv.moments(cnt)
        center = (int(m['m10'] / m['m00']), int(m['m01'] / m['m00']))

        if center[1] <= 65:
            if 40 <= center[0] <= 140:
                bpoints = [deque(maxlen=1024)]
                gpoints = [deque(maxlen=1024)]
                rpoints = [deque(maxlen=1024)]
                ypoints = [deque(maxlen=1024)]
                b_i = g_i = r_i = y_i = 0
                paintwindow[67:, :, :] = 255
            elif 160 <= center[0] <= 255:
                col_i = 0
            elif 275 <= center[0] <= 370:
                col_i = 1
            elif 390 <= center[0] <= 485:
                col_i = 2
            elif 505 <= center[0] <= 600:
                col_i = 3
        else:
            if col_i == 0:
                bpoints[b_i].appendleft(center)
            elif col_i == 1:
                gpoints[g_i].appendleft(center)
            elif col_i == 2:
                rpoints[r_i].appendleft(center)
            elif col_i == 3:
                ypoints[y_i].appendleft(center)
    else:
        if len(bpoints[b_i]) > 0:
            bpoints.append(deque(maxlen=1024))
            b_i += 1
        if len(gpoints[g_i]) > 0:
            gpoints.append(deque(maxlen=1024))
            g_i += 1
        if len(rpoints[r_i]) > 0:
            rpoints.append(deque(maxlen=1024))
            r_i += 1
        if len(ypoints[y_i]) > 0:
            ypoints.append(deque(maxlen=1024))
            y_i += 1

    points = [bpoints, gpoints, rpoints, ypoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv.line(frame, points[i][j][k - 1], points[i][j][k], col[i], 4)
                cv.line(paintwindow, points[i][j][k - 1], points[i][j][k], col[i], 4)

    cv.imshow("paint", frame)
    cv.imshow('mask', mask)
    cv.imshow('win', paintwindow)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
