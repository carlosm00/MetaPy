# MetaPy
Simple pythonic CLI application for image metadata collection and (optionally) delete it.
Run on Windows and Unix-based OS.

# Required libreries
* Pillow (PIL)

# How to use
Run through terminal providing absolute rute file or source.
('$python metapy.py C:\example\folder')

# Extra notes
## imghdr for image validator
imghdr builtin module is not used as it gets deprecated on 3.11.
Reference: https://docs.python.org/3/library/imghdr.html, https://peps.python.org/pep-0594/