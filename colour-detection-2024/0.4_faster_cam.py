import subprocess
import os

# Define the command
command = [
    "rpicam-still",
    "--timeout", "10800",
    "--width", "640",
    "--height", "480",
    "--output", "test2.jpg",
    "--timelapse", "1000",
    "--vflip",
    "--hflip"
]

# Redirect output to /dev/null to hide display
with open(os.devnull, 'w') as null_file:
    # Run the command, hiding the output
    process = subprocess.Popen(command, stdout=null_file, stderr=null_file)

# Wait for the process to finish (this will run indefinitely until manually terminated)
try:
    process.wait()
except KeyboardInterrupt:
    # Terminate the process if Ctrl+C is pressed
    process.terminate()
