# This is a python ptoject for metadata deletion on (initially) images
## Library importation
import os, sys
import logging
from PIL import Image, ExifTags
from __all__ import *

## Main script applied for provided path
metaPy('.\\sources\\dos.jpg')