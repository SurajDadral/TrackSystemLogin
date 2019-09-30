# Install required packages
sudo apt install python3 python3-opencv cron sed -y

# Start and enable crontab to schedule jobs at system boot
sudo systemctl start cron
sudo systemctl enable cron

# Create directories to store captured images and logs
sudo mkdir -p /var/TrackSystemLogin/captures /var/TrackSystemLogin/logs

# Copy source code to /opt/TrackSystemLogin/ directory
sudo mkdir -p /opt/TrackSystemLogin/
sudo cp -r $(dirname "$0")/* /opt/TrackSystemLogin/

# Setup crontab job to execute script at startup
sudo mkdir -p /var/spool/cron/crontabs/
sudo touch /var/spool/cron/crontabs/root
if ! grep -Fxq "@reboot python3 /opt/TrackSystemLogin/main.py" /var/spool/cron/crontabs/root
then
	sudo echo "@reboot python3 /opt/TrackSystemLogin/main.py" >> /var/spool/cron/crontabs/root
fi
sudo crontab /var/spool/cron/crontabs/root
