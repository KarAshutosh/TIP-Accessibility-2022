import cv2
import numpy as np
# the "empty" function basically does nothing
def empty(a):
    pass

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

cv2.namedWindow("Trackbars")                                    #makes a window called "Trackbars"
cv2.resizeWindow("Trackbars", 640, 240)                         #gives "Trackbars" window a size
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)       #"Hue Min" is the name (kinda like variable name), changing values of "Trackbars" window (the window it belongs to), the position on the trackbar at the beginning is 0, max value of hue is 179, function run everytime something changes in the trackbar
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)




while True:

    success, img = cap.read()

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)  #Checks both images "img" and "img". If pixels are present in both then it stores. The second "img" is the original image but with a mask called "mask" applied

    cv2.imshow("Original", img)
    cv2.imshow("Mask", mask)

    cv2.waitKey(10)

#try to keep the colours you don't want in black and the colours you want in white of the mask window

#highlighter; hsv min: 32, 49, 166; hsv max: 66, 196, 255
