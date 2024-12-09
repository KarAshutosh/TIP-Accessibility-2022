import os
import cv2
import qrcode
import numpy as np
import time
import subprocess


# Example usage:
image_path = 'test2.jpg'
sysOS = "RasPi"
distanceFromCenter = 1.2 # 1.2x QR code width from center
areaPoint = 10 # Shows how large the box is : 10 pixel square
visual = True # Shows the bounding box used for color detection
duration = 1 # Number of times it takes the photo

for i in range(duration):
    colour = simplified(image_path, distanceFromCenter, areaPoint, visual, sysOS)
    print(colour)
    # time.sleep(1)


# Command executed by rpiPhoto():  rpicam-still --timeout 100000 --width 640 --height 480 --output test2.jpg --timelapse 500 

def rpiPhoto():
    # Define the command: Takes a photo for 10 seconds
    command = [
        "rpicam-still",
        "--timeout", "10000",
        "--width", "640",
        "--height", "480",
        "--output", "test2.jpg",
        "--timelapse", "1000",
            ]

    # Run the command
    process = subprocess.Popen(command)

    # Wait for the process to finish (this will run indefinitely until manually terminated)
    try:
        process.wait()
    except KeyboardInterrupt:
        # Terminate the process if Ctrl+C is pressed
        process.terminate()

## QR CODE code. This code detects the QR png and draws an arrow down to where the detection should take place. This code exists
## so that if we use an instrument with this QR code it detects color there instead of at the center of the whole image (which is default behaviour)

def detect_and_draw_qr_boundary(image_path):
    # Load the image containing the QR code
    image = cv2.imread(image_path)

    # Initialize the QRCode detector
    detector = cv2.QRCodeDetector()

    # Detect and decode QR code
    data, vertices, _ = detector.detectAndDecode(image)

    qr_boundary_image = np.copy(image)  # Create a copy to draw the boundary

    return qr_boundary_image, vertices

def draw_arrow_down(image_path, vertices, colourPoint, areaPoint):

    image = cv2.imread(image_path)
    if len(vertices) == 1 and len(vertices[0]) >= 4:
        # Find the top and bottom vertices
        top_left = tuple(vertices[0][0])
        top_right = tuple(vertices[0][1])
        bottom_right = tuple(vertices[0][2])
        bottom_left = tuple(vertices[0][3])

        # Calculate the center of the QR code
        center_x = int((top_left[0] + top_right[0] + bottom_right[0] + bottom_left[0]) / 4)
        center_y = int((top_left[1] + top_right[1] + bottom_right[1] + bottom_left[1]) / 4)

        #######
        # arrow_points = np.array([[center_x, center_y], top_left, top_right], np.int32)
        
        # # Draw the arrow
        # cv2.drawContours(image, [arrow_points], 0, (0, 0, 255), -1)

        #######

        detect_x = int(center_x - (top_right[0] - bottom_right[0])*colourPoint)
        detect_y = int(center_y - (top_right[1] - bottom_right[1])*colourPoint)
        
        detection_points_arr = [
            [detect_x-areaPoint, detect_y+areaPoint], # top_left
            [detect_x+areaPoint, detect_y+areaPoint], # top_right
            [detect_x+areaPoint, detect_y-areaPoint], # bottom_left            
            [detect_x-areaPoint, detect_y-areaPoint], # bottom_right
            ]

        return detection_points_arr
    else:
        print("Error: Insufficient vertices to draw arrow.")
## QR code section ends 
def get_color_in_area(image_path, points, visual):
    # Load the image
    image = cv2.imread(image_path)
    # Centre coordinates of image
    center_x = image.shape[1] // 2
    center_y = image.shape[0] // 2
    # width is the width of the box in pixels at the center of the image
    width =10 # width default value is 10
    top_left_x = center_x - width // 2
    top_left_y = center_y - width // 2
    bottom_right_x = center_x + width // 2
    bottom_right_y = center_y + width // 2

    # Convert BGR image to HSV
    hsv_unprocessed = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Crop the image to the bounding box
    hsv_cropped = hsv_unprocessed[top_left_y:bottom_right_y, top_left_x:bottom_right_x, :]
    hsv_average=np.mean(hsv_cropped, axis=(0,1))
    print("Cropped hsv:",hsv_cropped)

    # Define color ranges
    color_ranges = {

         'red': [(0, 15, 100), (15, 255, 255)],
         'green': [(50, 100, 100), (70, 255, 255)],
         'blue': [(102, 25, 100), (130, 255, 255)],
         'pink' : [(111,11,189),(179,255,255)],

        # Add more color ranges as needed
    }
    # detected_colors dictionary. can later be exported to JSON   
    detected_colors = {}

    # Check for each color
    for color_name, (lower, upper) in color_ranges.items():
        lower_color = np.array(lower, dtype=np.uint8)
        upper_color = np.array(upper, dtype=np.uint8)
        # Check if color in range, add to dict if it is in range
        if (np.all(hsv_average<= upper_color)) and (np.all(hsv_average >= lower_color)):
            detected_colors[color_name] = hsv_average
        else: # Which value failed?
            print("Average hsv: ",hsv_average)
# TODO: Modify this code to make more sense
    if visual == True:
        detection_points = np.array(points, np.int32)

        # cv2.drawContours(image, [detection_points], 0, (0, 0, 255), -1)
        cv2.polylines(image, [detection_points], isClosed=True, color=(0, 0, 255), thickness=2)

        # Display the image with arrow
        cv2.imshow('Colour Detection', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    print(detected_colors) 
    return detected_colors


# ====================================================================

def takeImage(sysOS):
    if sysOS == "RasPi":
        rpiPhoto()
        # os.system("rpicam-still -t 1 -o test2.jpg --vflip --hflip")
        # # rpicam-still --timeout 100000 --width 640 --height 480 --output test2.jpg --timelapse 500 --vflip --hflip
        # os.system("convert test2.jpg -resize 640x480! test2.jpg")
# ====================================================================

def simplified(image_path, distanceFromCenter, areaPoint, visual, sysOS):
    
    takeImage(sysOS)

    qr_image_with_boundary, qr_boundary_vertices = detect_and_draw_qr_boundary(image_path)

    try:
        if len(qr_boundary_vertices) == 1:
            points = draw_arrow_down(image_path, qr_boundary_vertices, distanceFromCenter, areaPoint)
            print(points)
            colour = get_color_in_area(image_path, points, visual)
            return colour    
    except:
        points = [[316, 279], [336, 279], [336, 259], [316, 259]]
        colour = get_color_in_area(image_path, points, visual)
        return colour
