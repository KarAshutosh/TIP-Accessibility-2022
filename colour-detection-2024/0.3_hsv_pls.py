import cv2

# Function to extract HSV values from the center region of the frame
def get_center_hsv(frame):
    # Get the dimensions of the frame
    height, width, _ = frame.shape

    # Calculate the coordinates of the center region
    center_x = width // 2
    center_y = height // 2
    square_size = 10

    # Extract the center region
    center_region = frame[center_y - square_size // 2:center_y + square_size // 2,
                          center_x - square_size // 2:center_x + square_size // 2]

    # Convert the BGR pixel value to HSV
    hsv_center_region = cv2.cvtColor(center_region, cv2.COLOR_BGR2HSV)

    # Compute the average HSV values
    h_avg = int(cv2.mean(hsv_center_region)[0])
    s_avg = int(cv2.mean(hsv_center_region)[1])
    v_avg = int(cv2.mean(hsv_center_region)[2])

    return h_avg, s_avg, v_avg

# Function to handle mouse click event
def get_hsv(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        h, s, v = get_center_hsv(frame)
        print("HSV values in the center region: H={}, S={}, V={}".format(h, s, v))

# Initialize webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Create a window
cv2.namedWindow("Webcam")
# Set mouse callback function for the window
cv2.setMouseCallback("Webcam", get_hsv)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Get the dimensions of the frame
    height, width, _ = frame.shape

    # Calculate the coordinates of the center region
    center_x = width // 2
    center_y = height // 2
    square_size = 10

    # Draw a rectangle around the center region
    cv2.rectangle(frame, (center_x - square_size // 2, center_y - square_size // 2),
                  (center_x + square_size // 2, center_y + square_size // 2), (0, 255, 0), 1)

    # Display the resulting frame
    cv2.imshow("Webcam", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
