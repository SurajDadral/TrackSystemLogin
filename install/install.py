# Import library to detect OS
import platform
from subprocess import call

linuxName = ""
# If OS is Linux
if platform.system() == 'Linux':
    # Check if the linux is debian
    with open("/etc/os-release") as file:
        linuxName = (file.readline()).strip()
    if (linuxName == "NAME=Fedora"):
        pass

    elif (linuxName == "NAME=Ubuntu" or linuxName == "NAME=Debian"):
        pass
