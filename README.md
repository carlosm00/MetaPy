# MetaPy
Simple pythonic CLI application for image metadata collection and (optionally) delete it.
Run on Windows and Unix-based OS.

# Required libreries
- Pillow (PIL fork)

# Features
- Open Source
- Python-based full CLI application
- Logging on:
	- User level (info)
	- Developper level (debug, error)

# How to use
## Clone repository
	```
	git clone https://github.com/carlosm00/MetaPy.git
	```

## Run CLI application
Run through terminal providing absolute rute file or source.

	```
	python metapy.py C:\example\folder
	```

# Tests and 'Source' folder
For testing purposes we created a 'Source' folder containing the following files:

| File		       | Type   | Decription                   | Test result                                           |
| :--------------- | :----- | :--------------------------- | :---------------------------------------------------- |
| full_negative    | `png`  | Corrupted file               | Error: Invlid file                                    |
| positive_no_meta | `jpg`  | Plain image without metadata | Only size and mode                                    |
| full_positive    | `jpg`  | Phone-taken camera           | Full metadata output and duplication without metadata |


---

# Extra notes
## Why Pillow?
Pillow as the successor of PIL offers faster data-accessing methods and powerful optimized processing capabilities, with a continued contribution as a live project.
Reference: 
	- https://python-pillow.org/
	- https://pillow.readthedocs.io/en/stable/index.html
	- https://github.com/python-pillow/Pillow

## Logging
For logging capabilities we use the built-in 'Logging' facility.
Reference and documentation: 
	- https://docs.python.org/3/library/logging.html

## imghdr for image validator
imghdr builtin module is not used as it gets deprecated on 3.11. Opening the window for future versions.
Reference: 
	- https://docs.python.org/3/library/imghdr.html
	- https://peps.python.org/pep-0594/
