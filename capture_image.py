import os
from datetime import datetime
from time import sleep
from cv2 import VideoCapture, imwrite


def captureImage(image_dir, number_of_images=3):
    img_files_count = len(
        [
            name
            for name in os.listdir(image_dir)
            if os.path.isfile(os.path.join(image_dir, name))
        ]
    )

    image_files = []
    for i in range(0, number_of_images):
        camera = VideoCapture(0)
        if not camera.isOpened():
            with open(LOGS_DIR + "error.log", "a") as f:
                f.write(
                    "[Error "
                    + str(datetime.now().strftime("%b %d, %Y %H:%M:%S"))
                    + "] Could not open video device\n"
                )
        return_value, image = camera.read()
        camera.release()
        if not return_value:
            continue
        img_file = datetime.now().strftime(
            image_dir + "/image_%d%b%y-" + str(img_files_count) + ".jpg"
        )
        imwrite(img_file, image)
        image_files.append(img_file)
        img_files_count += 1
        sleep(3)
    return image_files
