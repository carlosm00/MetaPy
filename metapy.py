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
 Log Setup
 Every sdtout will be verted into the logfile (metapy.log),
 located on the same folder where the program is run.
 """

logging.basicConfig(level=logging.INFO, filename='.\metapy.log', format='%(asctime)s %(levelname)s - %(message)s')

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
                pass
            # Raise InvalidExifData

            exif_data['format'] = img.format
            print(exif_data)
            logging.info(exif_data)

        else:
            # Printing only image info
            print('Sorry, image has no exif data...')
            print('Stored data: Mode - ', img.mode, ' Size - ', img.size)
            logging('Stored data: Mode - ', img.mode, ' Size - ', img.size)


# MetaPy

def meta_py(route):
    # Printing route 
    print(route)
    try:
        # print("The file is a valid image")
        f1 = OpenImage(route)
        f1.image_read()
        # img_del(img)
    except IOError:
        # File is not a recognizable image
        print("The file is not a recognizable image...")
        logging.error("The file is not a recognizable image...")

    # else:
    # print("The file does not exists. Please, check that the " \
    # " value provided is indeed a correct path for the image...")


# Main script applied for provided path
meta_py('C:\\Users\\CM\\source\\repos\\MetaPy\\MetaPy\\sources\\dos.jpg')
