"""

METAPYTHON

CLI python application for image metadata collection and deletion

"""
# Library importation
# import os
import sys
import logging
from PIL import Image
from PIL.ExifTags import TAGS

"""
 Log Setup:

 1. USER log
 Every informational output will be verted into the metapy.log file,
 located on the same folder where the program is run.

 2. DEV log
 Every debugging-level output will be verted into the debug-metapy.log file,
 located on the same folder where the program is run.

 """

# Creating loggers
logger1 = logging.getLogger('user_log')
logger2 = logging.getLogger('dev_log')
logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.DEBUG)

# Preparing log format
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Setting INFO / USER log handler to lower level
handler1 = logging.FileHandler('.\\metapy.log')
stream_handler1 = logging.StreamHandler()
stream_handler1.setLevel(level=logging.INFO)
stream_handler1.setFormatter(formatter)
logger1.addHandler(handler1)

# Setting DEBUG / DEV log handler to only debug
handler2 = logging.FileHandler('.\\debug-metapy.log')
stream_handler2 = logging.StreamHandler()
stream_handler2.setLevel(level=logging.DEBUG)
stream_handler2.setFormatter(formatter)
logger2.addHandler(handler2)

# Image opening and tags listing


class OpenImage:
    def __init__(self, path):
        self.image = Image.open(path)
        self.exifdata = (self.image.getexif())

    def image_read(self):
        print("The file exists...")
        exit = self.exifdata
        img = self.image
        items = exit.items()

        # Checking exif data stored as Tags
        if exit:
            print("Has metadata:")
            try:
                # Use TAGS module to make EXIF data human readable
                exif_data = {
                    TAGS[key]: value
                    for key, value in items
                    if key in TAGS
                }
            except AttributeError:
                logger2.error('Error found on attributes')
            finally:
                logger2.debug(exit)

            # Raise InvalidExifData
            exif_data['format'] = img.format
            print(exif_data)
            logger1.info("Meta data: %s", exif_data)
        else:
            # Printing only image info
            no_exif = ("Sorry, image has no exif data...",
                'Stored data: Mode - ', img.mode, ' Size - ', img.size)
            print(no_exif)
            logger1.info(no_exif)
            logger2.info(no_exif)


# MetaPy

def meta_py(route):
    # Printing route
    print(route)
    logger1.info("Exec for %s", route)
    try:
        # print("The file is a valid image")
        f1 = OpenImage(route)
        f1.image_read()
        # img_del(img)
    except IOError:
        # File is not a recognizable image
        print("The file is not a recognizable image...")
        logger1.error("The file is not a recognizable image...")
        logger2.error("The file is not a recognizable image...")

    # else:
    # print("The file does not exists. Please, check that the " \
    # " value provided is indeed a correct path for the image...")


# Main script applied for provided path
meta_py('C:\\Users\\CM\\source\\repos\\MetaPy\\MetaPy\\sources\\dos.jpg')
