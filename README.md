# TODO
- [ ] Make code work with PiCamera2
- [ ] Make documentation
- [ ] Move this repo and TIP-Accessibility-2022 to Organisation
- [ ] Merge Volume detection code if possible
- [ ] Test the code with experiments in real time
- [ ] Merge relevant changes upstream to TIP-Accessibility
# DONE

# System information
- Debian 12 Bookworm
- RasPi Camera module v1.3

# Documentation links 
## PiCamera documentation
 - IMPORTANT: DO NOT USE PICAMERA IF YOU ARE ON A 64-BIT SYSTEM. USE PICAMERA2 INSTEAD.   
 - https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/PiCamera2-User-Guide/
 - https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
 - 
## Camera Module datasheetS
- https://datasheets.raspberrypi.com/camera/raspberry-pi-camera-guide.pdf
  - Contains general info about all the camera modules. Relevant sections : v1   
## Extra links that may be relevant
- https://libcamera.org/
  - libcamera is the userspace camera stack used by PiCamera 2     
- https://docs.kernel.org/userspace-api/media/v4l/colorspaces-defs.html
  - v4l2 is the kernel driver used to interface with the camera   
