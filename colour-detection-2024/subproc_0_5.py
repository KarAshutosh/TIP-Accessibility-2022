import cv2
import threading
import time

def capture_images():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return
    
    end_time = time.time() + 10  # Capture images for 10 seconds
    while time.time() < end_time:
        # Capture frame-by-frame
        ret, frame = cap.read()

        frame = cv2.resize(frame, (640, 480))

        # Save the image
        cv2.imwrite('test2.jpg', frame)
        print('Image saved as test2.jpg')

        # Sleep for 500 milliseconds
        time.sleep(0.5)

    # Release the webcam
    cap.release()

if __name__ == "__main__":
    # Create and start the thread for capturing images
    capture_thread = threading.Thread(target=capture_images)
    capture_thread.start()
