import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the captured frame
    cv2.imshow('Press q to capture', frame)

    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        # Save the captured frame to a file
        cv2.imwrite('litmus_paper_image.jpg', frame)
        print("Image saved as captured_image.jpg")
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
