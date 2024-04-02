import cv2
import numpy as np

# Function to get average HSV values from a 10x10 pixel box in the center of the screen
def get_average_hsv_values():
    cap = cv2.VideoCapture(0)  # Open the default camera (0)

    while True:
        ret, frame = cap.read()  # Read a frame from the camera
        if not ret:
            print("Error: Unable to capture frame")
            break

        # Get the dimensions of the frame
        height, width, _ = frame.shape

        # Define the coordinates for the 10x10 pixel box in the center of the frame
        box_size = 10
        x = int(width/2 - box_size/2)
        y = int(height/2 - box_size/2)

        # Extract the 10x10 pixel box from the frame
        box = frame[y:y+box_size, x:x+box_size]

        # Convert the colors in the box to HSV
        hsv_box = cv2.cvtColor(box, cv2.COLOR_BGR2HSV)

        # Calculate the mean HSV values
        avg_hsv = np.mean(hsv_box, axis=(0, 1))

        # Display the average HSV values
        print("Average HSV values of the 10x10 pixel box in the center of the screen:")
        print(avg_hsv)

        cv2.imshow('10x10 Pixel Box', box)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Call the function to get average HSV values from the 10x10 pixel box
get_average_hsv_values()
