import cv2
import numpy as np

def detect_litmus_paper(image_path):
    # Read the image
    image = cv2.imread(image_path)
    original_image = image.copy()
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Detect edges using Canny edge detector
    edges = cv2.Canny(blurred, 50, 150)
    
    # Find contours in the edged image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop over the contours
    detected_contours = []
    for contour in contours:
        # Find convex hull
        hull = cv2.convexHull(contour)
        
        # Approximate the convex hull
        epsilon = 0.03 * cv2.arcLength(hull, True)
        approx = cv2.approxPolyDP(hull, epsilon, True)
        
        # If the approximated contour has 4 vertices (a quadrilateral)
        if len(approx) == 4:
            detected_contours.append(approx)
    
    return original_image, detected_contours

def display_image_with_contours(image_path, contours):
    # Read the original image
    original_image = cv2.imread(image_path)
    
    # Draw the contours on the image
    image_with_contours = original_image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)
    
    # Display the image with contours
    cv2.imshow("Image with Contours", image_with_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path to the image file
image_path = "litmus_paper_image.jpg"

# Call the function to detect litmus paper-like shapes
_, detected_contours = detect_litmus_paper(image_path)

# Display the image with contours
display_image_with_contours(image_path, detected_contours)
