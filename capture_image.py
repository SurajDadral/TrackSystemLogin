import os
from datetime import date
from time import sleep
from cv2 import VideoCapture, imwrite
from config import *

img_files_count = len([name for name in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, name))])

for i in range(0, 3):
    camera = VideoCapture(0)
    if not camera.isOpened():
        with open(LOGS_DIR + "error.log", "a") as f:
            f.write(
                "[Error "
                + str(date.ctime(date.today()))
                + "] Could not open video device\n"
            )
    return_value, image = camera.read()
    camera.release()
    if not return_value:
        continue
    img_file = date.today().strftime(
        IMAGE_DIR + "/image_%d%b%y-" + str(img_files_count) + ".jpg"
    )
    imwrite(img_file, image)
    img_files_count += 1
    sleep(3)
