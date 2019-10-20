# TrackSystemLogin

Capture images during system startup and email captured images to admin

## Installation

Use the following command to install and setup TrackSystemLogin.

```bash
git clone https://github.com/SurajDadral/TrackSystemLogin
cd TrackSystemLogin
chmod +x setup.sh
./setup.sh
```

## Configurations
Edit configuration file ```config.py``` to modify default configurations.

```python
from datetime import datetime

config = {}

# Path of image storage directory
config["IMAGE_DIR"] = "/var/TrackSystemLogin/captures/"

# Path of log files
config["LOGS_DIR"] = "/var/TrackSystemLogin/logs/"

# Send email
config["SEND_EMAIL"] = True

# SMTP server address
config["SMTP_SERVER_ADDRESS"] = "smtp.gmail.com"

# SMTP server port
config["SMTP_SSL_PORT"] = 465

# Email address used to send emails
config["FROM_EMAIL_ADDRESS"] = ""

# Email address used to recieve emails on each login
config["TO_EMAIL_ADDRESS"] = ""

# Password of FROM_EMAIL_ADDRESS
config["PASSWORD_OF_FROM_EMAIL_ADDRESS"] = ""

# Subject of email
config["EMAIL_SUBJECT"] = "System blank@noip powered on at " + str(
    datetime.now().strftime("%b %d, %Y %H:%M:%S")
)

# Body of email
config[
    "EMAIL_BODY"
] = """\
Hi Sir,
Someone powered on your laptop at %s.
Please check images of person, who powered on your system, in attachment.
Don't recognize this activity?
Consider taking appropriate action.

Thank you.
Have a nice day.
""" % str(
    datetime.now().strftime("%b %d, %Y %H:%M:%S")
)

# Git commit
config["GIT_COMMIT"] = False

# Github username or API token
config["GITHUB_USERNAME_OR_API_TOKEN"] = ""

# Github user password
config["GITHUB_USER_PASSWORD"] = ""

# Github repository name
config["GITHUB_REPOSITORY"] = "TrackSystemLoginImageStorage"

# Git commit message
config["GIT_COMMIT_MESSAGE"] = "System blank@noip powered on at " + str(
    datetime.now().strftime("%b %d, %Y %H:%M:%S")
)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
