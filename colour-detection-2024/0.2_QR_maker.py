# pip install qrcode

import qrcode

# Text to encode in the QR code
data = "5a11y-AK-2014"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("5a11y-AK-2014_QR.png")

print("QR Code generated successfully!")
