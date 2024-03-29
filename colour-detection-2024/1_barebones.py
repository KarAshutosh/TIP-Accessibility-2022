import os
import cv2
import numpy as np

def detect_colors(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert BGR image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color ranges
    color_ranges = {
        'red': [(0, 100, 100), (10, 255, 255)],
        'green': [(50, 100, 100), (70, 255, 255)],
        'blue': [(110, 100, 100), (130, 255, 255)],
        'litmusBlue': [(95, 135, 100), (179, 255, 255)]
        # Add more color ranges as needed
    }

    detected_colors = []

    # Check for each color
    for color_name, (lower, upper) in color_ranges.items():
        lower_color = np.array(lower, dtype=np.uint8)
        upper_color = np.array(upper, dtype=np.uint8)

        # Create mask
        mask = cv2.inRange(hsv, lower_color, upper_color)

        # Count non-zero pixels
        if cv2.countNonZero(mask) > 0:
            detected_colors.append(color_name)

    return detected_colors


# ====================================================================
# Open the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not access the webcam.")
else:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the captured frame
        cv2.imshow('Webcam', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Save the image
            cv2.imwrite('test2.jpg', frame)
            print('Image saved as test2.jpg')
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
# ====================================================================

# os.system("libcamera-still -o test2.jpg --vflip --hflip")
path = r'./test2.jpg'

detected_colors = detect_colors(path)
print('Detected Colors:', detected_colors)

