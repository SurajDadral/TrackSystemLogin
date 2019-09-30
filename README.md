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

# Path of image storage directory
IMAGE_DIR = "/var/TrackSystemLogin/captures/"

# Path of log files
LOGS_DIR = "/var/TrackSystemLogin/logs/"

# SMTP server address
SMTP_SERVER_ADDRESS = "smtp.gmail.com"

# SMTP server port
SMTP_SSL_PORT = 465

# Email address used to send emails
FROM_EMAIL_ADDRESS = ""

# Email address used to recieve emails on each login
TO_EMAIL_ADDRESS = ""

# Password of FROM_EMAIL_ADDRESS
PASSWORD_OF_FROM_EMAIL_ADDRESS = ""

# Subject of email
EMAIL_SUBJECT = "System blank@noip powered on at " + str(
    datetime.now().strftime("%b %d, %Y %H:%M:%S")
)

# Body of email
EMAIL_BODY = """\
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)