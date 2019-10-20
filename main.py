from time import sleep
import socket
from capture_image import captureImage
from config import *

# Capture image
image_files = captureImage(config["IMAGE_DIR"])

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

if config["SEND_EMAIL"]:
    # Send email
    from send_mail import sendMail

    sendMail(
        config["FROM_EMAIL_ADDRESS"],
        config["PASSWORD_OF_FROM_EMAIL_ADDRESS"],
        config["TO_EMAIL_ADDRESS"],
        config["EMAIL_SUBJECT"],
        config["EMAIL_BODY"],
        config["SMTP_SERVER_ADDRESS"],
        config["SMTP_SSL_PORT"],
        image_files,
    )

if config["GIT_COMMIT"]:
    # Create git commit
    from git_commit import gitCommit

    if (
        config["GITHUB_USERNAME_OR_API_TOKEN"]
        and config["GITHUB_USER_PASSWORD"]
    ):
        gitCommit(
            config["GITHUB_REPOSITORY"],
            image_files,
            config["GIT_COMMIT_MESSAGE"],
            config["GITHUB_USERNAME_OR_API_TOKEN"],
            config["GITHUB_USER_PASSWORD"],
        )
    elif config["GITHUB_USERNAME_OR_API_TOKEN"]:
        gitCommit(
            config["GITHUB_REPOSITORY"],
            image_files,
            config["GIT_COMMIT_MESSAGE"],
            config["GITHUB_USERNAME_OR_API_TOKEN"],
        )
