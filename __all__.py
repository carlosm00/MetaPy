### Own function library
import os, sys
import logging
from PIL import Image, ExifTags

### Image opening
def img_read(img):
    exifdata = img.getexif()
    # Checking exif data stored as Tags
    if exifdata:
        for key, val in exifdata.items():
            print("Has metadata:")
            # Print Data as Tags
            if key in ExifTags.TAGS:
                print(f'{ExifTags.TAGS[key]}:{val}')
    else:
    # Printing only image info
        print('Sorry, image has no exif data...')
        print('Stored data: Mode - ', img.mode, ' Size - ', img.size)

### Log Setup
"""             - YET TO DEFINE A WAY TO OUTPUT BOTH STDOUT AND LOG FILE
def logger():
    a_logger = logging.getLogger()
    a_logger.setLevel(logging.DEBUG)

    output_file_handler = logging.FileHandler(".\\metapy.log")
    stdout_handler = logging.StreamHandler(sys.stdout)

    a_logger.addHandler(output_file_handler)
    a_logger.addHandler(stdout_handler)
"""

### MetaPy
# Check if file exists
def metaPy(path):
    # Setup log file
    #logger()
    print(path)
    # Checking if the file exists
    if os.path.isfile(path):
        print("The file exists...")
        # try-except block to handle non-image files
        try:
            img=Image.open(path)
            print("The file is a valid image")
            img_read(img)
            #img_del(img)
        except IOError:
            # File is not a recognizable image
            print("The file is not a recognizable image...")
    else:
        print("The file does not exists. Please, check that the value provided is indeed a correct path for the image...")