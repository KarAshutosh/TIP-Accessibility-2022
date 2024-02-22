import cv2

def main():
    # Open the default camera (usually the webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the captured frame
        cv2.imshow('Webcam', frame)

        # Wait for the 'q' key to be pressed to exit
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            # Save the last captured frame as a picture
            cv2.imwrite('captured_image.jpg', frame)
            print("Image saved as 'captured_image.jpg'")
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
