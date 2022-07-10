"""
    Title: metaPy
    Author: Carlos Mena
    Version: 1.0
    Description: CLI python application for image metadata collection and optional deletion
    with two log levels (info and debug) verted into two different files.
    Not valid for images contained on byte streams.
    
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

image_copy_del() -> Copy of preselected image
    without metadata on new 'no_meta' folder

"""


class OpenImage:
    def __init__(self, path):
        self.image = Image.open(path)
        self.exifdata = (self.image.getexif())

    def image_read(self):
        # Image-reading function
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
                # Rise error for attributes reading through dev log
                logger2.error('Error found on attributes')
            finally:
                # Provide raw data on debug level through dev log
                logger2.debug("Raw metada: %s", exit)
            # Preset format of exif_data into previous tags
            exif_data['format'] = img.format
            exif_data['Mode'] = img.mode
            exif_data['Size'] = img.size
            # Provide data on info level through terminal + user + dev logs
            print("Meta data: ", exif_data)
            logger1.info("Meta data: %s", exif_data)
            logger2.info("Meta data: %s", exif_data)
        else:
            # If image has not exif data,
            # we provide basics mode and size of image
            no_exif = ('Sorry, image has no exif data... Stored data: \
Mode - ' + img.mode + ' Size - ', img.size)
            print(no_exif)
            logger1.info(no_exif)
            logger2.debug(no_exif)

    def image_copy_del(self, filename, destination):
        # Image-copy of deleted-metadata image version
        # destination is given as arg
        img = self.image

        if self.exifdata:
            try:
                if (img.mode != 'RGB'):
                    # If image is not on RGB mode, we convert it
                    img = img.convert('RGB')
                data = list(img.getdata())

                # Setting new image data
                image_without_exif = Image.new(img.mode, img.size)
                image_without_exif.putdata(data)

                # Setting new image name + route
                new_file = destination + "\\" + filename

                # Saving image on new location
                image_without_exif.save(new_file)
                print("New image without metadata created: ", new_file, "\n")
                logger1.info("New image without metadata created %s", new_file)
                logger2.info("New image without metadata created %s", new_file)
                logger1.info("")
                logger2.info("")
            except OSError:
                # Leaving proof of error on logs
                logger1.info("Copy not created. See debug log for more info")
                logger1.info("")
                logger2.error("Error on creating copy without metadata")
                logger2.info("")
        else:
            print("As image has no metadata, no copy is created\n")
            logger1.info("As image has no metadata, no copy is created")
            logger1.info("")
            logger2.info("As image has no metadata, no copy is created")
            logger2.info("")


def new_directory(path, option):
    # Function to create new directory
    # option is defined either as file or directory

    if (option == 'file'):
        # When the option is file
        file_len = len(path.rsplit("\\")[-1])
        root_directory_len = (len(path) - file_len - 1)
        root_directory = (path[0:root_directory_len])
        # Setting destination directory
        directory = root_directory + '\\' + 'without_meta'
    elif(option == 'directory'):
        # When option is file
        # Setting destination directory directly
        directory = path + '\\without_meta'

    if not os.path.exists(directory):
        # If destination directoy does not exists
        # we create it + leave proof on logs
        os.makedirs(directory)
        logger1.info("Destination directory created: %s", directory)
        logger2.info("Destination directory created: %s", directory)
    else:
        # If it exists, we leave proof on logs
        logger1.info("Destination directory already existed: %s", directory)
        logger2.info("Destination directory already existed: %s", directory)

    # We return such destination route for further use
    return directory


# MetaPy

def meta_py(route, filename, destination):
    # Printing route executing on log
    print("Executing for ", route)
    logger1.info("Executing for %s", route)
    logger2.info("Executing for %s", route)
    try:
        # Opening new image-object
        f1 = OpenImage(route)
        f1.image_read()
        # Checking ask option from arg
        if (ask is True):
            logger2.debug("No force argument used")
            # No force arg, we ask if user wishes
            # to create a copy without metadata
            if (input("\nDo you wish to create a \
copy without metadata?\n") == 'yes'):
                logger2.debug("User decided to create a copy without metadata")
                f1.image_copy_del(filename, destination)
            else:
                logger2.debug("User decided NOT to \
create a copy without metadata")
                print("\nYou chose not to create a copy without metadata\n")
        else:
            logger2.debug("Force argument used without being asked")
            f1.image_copy_del(filename, destination)
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
        destination = new_directory(route, 'file')
        filename = (route.rsplit("\\")[-1])
        meta_py(route, filename, destination)
    elif(os.path.exists(route)):
        # If arg is a directory, each file is extracted
        destination = new_directory(route, 'directory')
        my_files = [f for f in listdir(route) if isfile(join(route, f))]
        for file in my_files:
            filename = file
            file = route + "\\" + file
            meta_py(file, filename, destination)
    else:
        print(route, "is not a valid route or file \n")
        logger1.error("%s is not a valid route or file", route)
        logger1.info("")
        logger2.error("%s is not a valid route or file", route)
        logger2.info("")


# Executing script with argument as route
if (len(sys.argv) == 3) and (sys.argv[2] == '-f'):
    # If second argument is '-f', we force duplication
    ask = False
    logger2.debug("Control passed")
    main(sys.argv[1])
elif (len(sys.argv) == 2):
    # If not, we ask on each
    ask = True
    logger2.debug("Control passed")
    main(sys.argv[1])
else:
    print("Script was not correctly used. Please, read the README.md")
    logger2.debug("Script not correctly used...")
