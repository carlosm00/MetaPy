"""

METAPY

CLI python application for image metadata collection and optional deletion
 with two log levels (info and debug) verted into two different files.
Not valid for images contained on byte streams.

Needed libraries:

- Sys
- Logging
- PIL (Pillow, needed of download)


Library importation
"""
import sys
import logging
import os
from os import listdir
from os.path import exists, isfile, join
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


# Creating both loggers
logger1 = logging.getLogger('user_log')
logger2 = logging.getLogger('dev_log')
logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.DEBUG)

# Preparing log format
# formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Setting INFO / USER log handler to lower level
handler1 = logging.FileHandler('.\\metapy.log')
stream_handler1 = logging.StreamHandler()
stream_handler1.setLevel(level=logging.INFO)
# stream_handler1.setFormatter(formatter)
logger1.addHandler(handler1)

# Setting DEBUG / DEV log handler to debug
handler2 = logging.FileHandler('.\\debug-metapy.log')
stream_handler2 = logging.StreamHandler()
stream_handler2.setLevel(level=logging.DEBUG)
# stream_handler2.setFormatter(formatter)
logger2.addHandler(handler2)


"""
OpenImage class for image-related functions.

image_read() -> Image opening and metadata collection on tags,
    listed as key-value

image_copy() -> Preselected image copy on 'origin' folder

image_del() -> Preselected image metadata deletion after copy

"""


class OpenImage:
    def __init__(self, path):
        self.image = Image.open(path)
        self.exifdata = (self.image.getexif())

    def image_read(self):
        exit = self.exifdata
        img = self.image
        items = exit.items()

        # Checking exif data stored as Tags
        if exit:
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
                logger2.debug("Raw metada: %s", exit)
            # Raise InvalidExifData
            exif_data['format'] = img.format
            print("Meta data: ", exif_data,"\n")
            logger1.info("Meta data: %s", exif_data)
            logger1.info("")
            logger2.info("Meta data: %s", exif_data)
            logger2.info("")
        else:
            # Printing only image info
            no_exif = ("Sorry, image has no exif data... Stored data: Mode - ", img.mode, ' Size - ', img.size)
            print(no_exif,"\n")
            logger1.info(no_exif)
            logger1.info("")
            logger2.debug(no_exif)
            logger2.info("")


# MetaPy

def meta_py(route):
    # Printing route on log
    print("Executing for ", route)
    logger1.info("Executing for %s", route)
    logger2.info("Executing for %s", route)
    try:
        # print("The file is a valid image")
        f1 = OpenImage(route)
        f1.image_read()
        # img_del(img)
    except IOError:
        # File is not a recognizable image
        print(route, " is not a recognizable image... \n")
        logger1.error("%s is not a recognizable image...", route)
        logger1.info("")
        logger2.error("%s file is not a recognizable image...", route)
        logger2.info("")


# Main script applied for provided path
def main(route):
    # Conditional structure to check if provided arg is a file or directory
    # and consequently exec metapy
    if (os.path.isfile(route)):
        # If arg is a file, it will single-execute
        print(route, "is a file and exists")
        logger1.info("%s is a file and exists", route)
        meta_py(route)
    elif(os.path.exists(route)):
        # If arg is a directory, each file is extracted
        my_files = [f for f in listdir(route) if isfile(join(route, f))]
        for file in my_files:
            file = route + "\\" + file
            meta_py(file)
    else:
        print(route, "is not a valid route or file \n")
        logger1.error("%s is not a valid route or file", route)
        logger1.info("")
        logger2.error("%s is not a valid route or file", route)
        logger2.info("")


# meta_py('C:\\Users\\CM\\source\\repos\\MetaPy\\MetaPy\\sources\\dos.jpg')

# negativo
main('C:\\Users\\CM\\source\\repos\\MetaPy\\MetaPy\\sourcess')

# positivo full _fichero_
# main('C:\\Users\\CM\\source\\repos\\MetaPy\\MetaPy\\sources\\dos.jpg')

# positivo directorio
main('C:\\Users\\CM\\source\\repos\\MetaPy\\MetaPy\\sources')
