import subprocess

# Define the command and arguments
command = [
    "rpicam-still",
    "--timeout",
    "100000",
    "--width",
    "640",
    "--height",
    "480",
    "--output",
    "test2.jpg",
    "--timelapse",
    "500",
    "--vflip",
    "--hflip"
]

# Run the command
subprocess.run(command)
