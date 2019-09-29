from time import sleep
import socket
from capture_image import captureImage
from send_mail import sendMail
from config import *

# Capture image
image_files = captureImage(IMAGE_DIR)

# Check internet connectivity
while True:
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        break
    except:
        sleep(20)
        pass

# Send email
sendMail(
    FROM_EMAIL_ADDRESS,
    PASSWORD_OF_FROM_EMAIL_ADDRESS,
    TO_EMAIL_ADDRESS,
    EMAIL_SUBJECT,
    EMAIL_BODY,
    SMTP_SERVER_ADDRESS,
    SMTP_SSL_PORT,
    image_files,
)
