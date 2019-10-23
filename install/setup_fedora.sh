# Install required packages
sudo dnf install python3 python3-opencv crontabs
sudo python3 -m pip install PyGithub

# Start and enable crontab to schedule jobs at system boot
sudo systemctl start chronyd.service
sudo systemctl enable chronyd.service

# Get image and logs storage directory from config.py file
IMAGE_DIR=$(cat ../config.py | egrep "config\[\"IMAGE_DIR\"\]" | sed -e "s/^\(.*\)= //g")
LOGS_DIR=$(cat ../config.py | egrep "config\[\"LOGS_DIR\"\]" | sed -e "s/^\(.*\)= //g")

sudo mkdir -p $IMAGE_DIR $LOGS_DIR

# Copy source code to /opt/TrackSystemLogin/ directory
sudo mkdir -p /opt/TrackSystemLogin/
sudo cp -r $(dirname "$0")/* /opt/TrackSystemLogin/

# Setup crontab job to execute script at startup
sudo mkdir -p /var/spool/cron/crontabs/
sudo touch /var/spool/cron/crontabs/root
if ! sudo grep -Fxq "@reboot python3 /opt/TrackSystemLogin/main.py" /var/spool/cron/crontabs/root
then
	    sudo bash -c 'echo "@reboot python3 /opt/TrackSystemLogin/main.py" >> /var/spool/cron/crontabs/root'
fi
sudo crontab /var/spool/cron/crontabs/root
