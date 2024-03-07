import os

image_directory = "/var/lib/motion"

def get_latest_image():
    image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]
    if image_files:
        return max(image_files, key=os.path.getctime)
    else:
        return None

if __name__ == "__main__":
    latest_image = get_latest_image()
    if latest_image:
        print("Latest image:", latest_image)
    else:
        print("No images found in the directory")
