# Code to create HSV values in OpenCV to compare with the litmus
import cv2
import numpy as np

# Get user input for HSV values
# h = int(input("Enter H value (0-180): "))
# s = int(input("Enter S value (0-255): "))
# v = int(input("Enter V value (0-255): "))

loop= int(input("Enter 1 if I should enter into a loop over h and v. 4 to get values:  "))

if (loop == 1): # Steps of 5
    for i in range(0,36):
        h=i*5
        print("Hue: ",h)
        for s in range(1,256):
            print("Saturation change: ", s)
            v=255
            hsv_image = np.full((100, 100, 3), (h, s, v), dtype=np.uint8)
            bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
            cv2.imshow('Color', bgr_image)
            cv2.waitKey(0)
            if (cv2.waitKey(0)==ord('q')):
                cv2.destroyAllWindows()
                break
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if (loop == 2): # Steps of 10
    for i in range(0,18):
        h=i*10
        print("Hue: ",h)
        for s in range(1,256):
            print("Saturation change: ", s)
            v=255
            hsv_image = np.full((100, 100, 3), (h, s, v), dtype=np.uint8)
            bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
            cv2.imshow('Color', bgr_image)
            cv2.waitKey(0)
            if (cv2.waitKey(0)==ord('q')):
                cv2.destroyAllWindows()
                break
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if (loop == 3): # Steps of 20
    for i in range(0,9):
        h=i*20
        print("Hue: ",h)
        for s in range(1,256):
            print("Saturation change: ", s)
            v=255
            hsv_image = np.full((100, 100, 3), (h, s, v), dtype=np.uint8)
            bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
            cv2.imshow('Color', bgr_image)
            cv2.waitKey(0)
            if (cv2.waitKey(0)==ord('q')):
                cv2.destroyAllWindows()
                break
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if (loop==4):
        h = int(input("Enter H value (0-180): "))
        s = int(input("Enter S value (0-255): "))
        v = int(input("Enter V value (0-255): "))





# Create an HSV image of the specified color
hsv_image = np.full((100, 100, 3), (h, s, v), dtype=np.uint8)

# Convert the HSV image to BGR (which is the format OpenCV uses for display)
bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# Display the color image
cv2.imshow('Color', bgr_image)

# Wait for any key to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
