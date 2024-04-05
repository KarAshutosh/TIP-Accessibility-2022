Error: Unable to capture frame
Traceback (most recent call last):
  File "/home/raspi/RASPI-TESTING/RasPi-Fork/colour-detection-2024/hsv-checker.py", line 3, in <module>
    from picamera2 import Picamera2
  File "/usr/lib/python3/dist-packages/picamera2/__init__.py", line 9, in <module>
    from .picamera2 import Picamera2, Preview
  File "/usr/lib/python3/dist-packages/picamera2/picamera2.py", line 26, in <module>
    from picamera2.encoders import Encoder, H264Encoder, MJPEGEncoder, Quality
  File "/usr/lib/python3/dist-packages/picamera2/encoders/__init__.py", line 21, in <module>
    from .h264_encoder import H264Encoder
  File "/usr/lib/python3/dist-packages/picamera2/encoders/h264_encoder.py", line 3, in <module>
    from v4l2 import (V4L2_CID_MPEG_VIDEO_H264_I_PERIOD,
ImportError: cannot import name 'V4L2_CID_MPEG_VIDEO_H264_PROFILE' from 'v4l2' (/usr/lib/python3/dist-packages/v4l2.py)
