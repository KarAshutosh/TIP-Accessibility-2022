# Documentation

## Overview
This script is designed to capture images containing QR codes, detect QR codes and their boundaries, draw arrows pointing downwards from the center of QR codes, and extract color information from specified regions of interest (ROI) around the arrows. Additionally, it provides audio feedback based on the detected colors.

## Requirements
Python 3
Raspberry Pi with Raspberry Pi Camera Module 

## Usage

### Running the Script
Clone or download the script from the repository.
Navigate to the directory containing the script.
Run the script using Python:

```
python 10_voice.py
```

### Parameters

* `image_path`: Path to the image file where QR codes will be detected.
sysOS: Operating system environment. Choose either `Windows` or `RasPi` (Raspberry Pi). Default is `Windows`.

* `distanceFromCenter`: Distance multiplier for drawing the arrow from the center of the QR code. Default is `1.2`.

* `areaPoint`: Size of the area around the arrow to detect color. Default is `10`.

* `visual`: Flag to display intermediate images during processing. Default is `True`.

* `duration`: Duration (in seconds) for which the script will run. Default is `10`.

### Functions

* `rpiPhoto()`: Capture an image using the Raspberry Pi camera.

* `play_mp3(file_path)`: Play an MP3 file.

* `detect_and_draw_qr_boundary(image_path)`: Detect QR codes and draw boundaries.

* `draw_arrow_down(image_path, vertices, colourPoint, areaPoint)`: Draw an arrow downwards from the center of the QR code.

* `get_color_in_area(image_path, points, visual)`: Extract color information from a specified area.

* `takeImage(sysOS)`: Capture an image based on the operating system.

* `simplified(image_path, distanceFromCenter, areaPoint, visual, sysOS)`: Simplified interface for QR code detection and color extraction.

* `output_data(data)`: Process detected color data and provide audio feedback.

Here's a tree diagram illustrating how the functions in the script are interconnected:

```
simplified()
├── takeImage()
│   └── rpiPhoto()
├── detect_and_draw_qr_boundary()
├── get_color_in_area()
└── draw_arrow_down()

output_data()
└── play_mp3()
```

### Notes
For Raspberry Pi, ensure the rpicam-still command is installed.
MP3 files for audio feedback should be placed in the audio directory.

### ToDo
Play audio in Pi
