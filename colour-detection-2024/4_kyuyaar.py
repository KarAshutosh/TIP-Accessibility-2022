import cv2
import qrcode
import numpy as np

import cv2
import qrcode
import numpy as np

def detect_and_draw_qr_boundary(image_path):
    # Load the image containing the QR code
    image = cv2.imread(image_path)

    # Initialize the QRCode detector
    detector = cv2.QRCodeDetector()

    # Detect and decode QR code
    data, vertices, _ = detector.detectAndDecode(image)

    qr_boundary_image = np.copy(image)  # Create a copy to draw the boundary

    if data:
        print("Decoded Data:", data)
        # Now, we'll decode the QR code using the qrcode library
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        # Display the position of QR code vertices
        print("QR Code vertices:", vertices)
        
        # Convert vertices to integers for drawing lines
        vertices = vertices.astype(int)
        
        # Draw the QR code boundary
        for i in range(len(vertices)):
            # draw bounding box around the QR code
            qr_boundary_image = cv2.line(qr_boundary_image, tuple(vertices[i][0]), tuple(vertices[(i+1) % len(vertices)][0]), color=(255, 0, 0), thickness=2)
    else:
        print("QR Code not detected")

    return qr_boundary_image, vertices

def draw_arrow_down(image, vertices):
    if len(vertices) == 1 and len(vertices[0]) >= 4:
        # Find the top and bottom vertices
        top_left = tuple(vertices[0][0])
        top_right = tuple(vertices[0][1])
        bottom_right = tuple(vertices[0][2])
        bottom_left = tuple(vertices[0][3])

        # Calculate the center of the QR code
        center_x = int((top_left[0] + top_right[0] + bottom_right[0] + bottom_left[0]) / 4)
        center_y = int((top_left[1] + top_right[1] + bottom_right[1] + bottom_left[1]) / 4)

        # Determine orientation based on the y-coordinate of top-left and bottom-left vertices
        if top_left[1] < bottom_left[1]:  # QR code is not upside down
            arrow_points = np.array([[center_x, center_y + 20],  # Top
                                      [center_x - 10, center_y + 10],  # Bottom left
                                      [center_x + 10, center_y + 10]],  # Bottom right
                                     np.int32)
        else:  # QR code is upside down
            arrow_points = np.array([[center_x, center_y - 20],  # Bottom
                                      [center_x - 10, center_y - 10],  # Top left
                                      [center_x + 10, center_y - 10]],  # Top right
                                     np.int32)

        # Draw the arrow
        cv2.drawContours(image, [arrow_points], 0, (0, 0, 255), -1)

        # Display the image with arrow
        cv2.imshow('Arrow Drawn', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Insufficient vertices to draw arrow.")


# Example usage:
image_path = 'captured_image_ulta.jpg'

qr_image_with_boundary, qr_boundary_vertices = detect_and_draw_qr_boundary(image_path)

print(qr_boundary_vertices)
# Draw an arrow facing downwards
draw_arrow_down(qr_image_with_boundary, qr_boundary_vertices)