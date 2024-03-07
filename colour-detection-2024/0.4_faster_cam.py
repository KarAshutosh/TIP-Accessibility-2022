# pip install picamera
import picamera

# Create a Picamera instance
with picamera.PiCamera() as camera:
    # Adjust camera settings if needed
    camera.vflip = True  # Vertical flip
    camera.hflip = True  # Horizontal flip
    
    # Capture an image quickly (with minimal delay)
    camera.capture('test2.jpg')


# sudo apt install --reinstall libraspberrypi0 libraspberrypi-dev libraspberrypi-doc libraspberrypi-bin
