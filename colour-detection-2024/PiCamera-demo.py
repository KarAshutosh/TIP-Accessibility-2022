import picamera2 

cam= picamera2.PiCamera2()
cam.resolution= (640,480)
camera.start_preview()
camera.capture_file("demo.jpg")
camera.stop_preview()
camera.close()

