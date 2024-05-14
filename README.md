# TODO
- [ ] Make code work with PiCamera2
- [ ] Make documentation
- [ ] Move this repo and TIP-Accessibility-2022 to Organisation
- [ ] Merge Volume detection code if possible
- [ ] Test the code with experiments in real time
- [X] Merge relevant changes upstream to TIP-Accessibility
- [ ] Implement voice output on the RasPi
# DONE

# System information
- Raspberry Pi Model 3B+
- Debian 12 Bookworm
- RasPi Camera module v1.3 (OV5647, 5MP, <resolution>)

# Documentation links 
## RasPi Model 3B+ datasheet
- https://datasheets.raspberrypi.com/rpi3/raspberry-pi-3-b-plus-product-brief.pdf
## PiCamera documentation
 - IMPORTANT: DO NOT USE PICAMERA IF YOU ARE ON A 64-BIT SYSTEM. USE PICAMERA2 INSTEAD.   
 - https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/PiCamera2-User-Guide/
 - https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
 - 
## Camera Module datasheets
- https://datasheets.raspberrypi.com/camera/raspberry-pi-camera-guide.pdf
  - Contains general info about all the camera modules. Relevant sections : v1
- https://www.raspberrypi.com/documentation/accessories/camera.html
-  https://docs.rs-online.com/2888/0900766b8127db0a.pdf
  - This contains the specifications for the camera module currently being used: the v1.3
- 
## Extra links that may be relevant
- https://libcamera.org/
  - libcamera is the userspace camera stack used by PiCamera2. Note: openCV has not got builtin support for the libcamera stack, which includes the RasPi camera modules, so openCV's Video.Capture(0) will bring up an error.
  - rpicam is an extension of libcamera made by the Raspberry Pi team      
- https://docs.kernel.org/userspace-api/media/v4l/colorspaces-defs.html
  - v4l2 is the kernel driver used to interface with the camera
- [SSH into RasPi](https://www.makeuseof.com/how-to-ssh-into-raspberry-pi-remote/)

- [OpenCV documentation of the implementation of the color spaces (C++)](https://docs.opencv.org/4.x/d8/d01/group__imgproc__color__conversions.html)
- [MicroPython: Running Python on the ESP32 ](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html) 
- https://dangitgit.com/
- https://picamera.readthedocs.io/en/release-1.13/fov.html
	- How the camera hardware works under the hood


## Notes/Common Errors
- Error: `error: externally-managed-environment`
  - When installing a package, use `--break-system-packages` or `venv`
  - Find the source [here](https://stackoverflow.com/questions/75602063/pip-install-r-requirements-txt-is-failing-this-environment-is-externally-mana)
- Literally any Makefile errors
  - 90% of Makefile errors are errors of whitespace. (tabs, spaces, trailing spaces, etc)
  - Make whitespace visible on your code editor
  - if you are editing your Makefile on GitHub (Highly not recommended):
  	- Change indent rules to use Tab in the text editor
   		- 1 Tab = 4 Spaces
     - Use your code editor instead and push changes from there.
## Contact
- Ashutosh Karanam
  - e-mail: f20201441@goa.bits-pilani.ac.in (BITS), ashutoshdeveloping@gmail.com (personal) 
- Govind Nambiar
  - e-mail: f20211527@goa.bits-pilani.ac.in

