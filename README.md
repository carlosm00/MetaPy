# MetaPy
Simple pythonic service for image metadata deletion. 
This solution includes Dockerfile to build the image for the solution.

# Required libraries
- Pillow (PIL fork)
- Flask

# Features
- Open Source
- Python-based
- Dockerized

# How to use
## Setup
Setting up the service is as simple and clonning the repo, building the image and running the service, exposing port 5000:
```
git clone https://github.com/carlosm00/MetaPy.git
cd MetaPy
docker build -t metapy .
docker run -d -p 5000:5000 metapy
```
## Call to service
For using the service, we simply need to call to '/remove-metadata' method providing the file path and output:
```
~/MetaPy/sources$ curl -X POST http://localhost:5000/remove-metadata -F "file=@positive_no_meta.jpg" -o output_image.jpg
```

# Tests and 'Source' folder
For testing purposes, we created a 'Source' folder containing three files to test with:

| File		       | Type   | Description                  | Test result                                           |
| :--------------- | :----- | :--------------------------- | :---------------------------------------------------- |
| full_negative    | `png`  | Corrupted file               | Error: Invalid file                                   |
| positive_no_meta | `jpg`  | Plain image without metadata | Only size and mode                                    |
| full_positive    | `jpg`  | Phone-taken camera           | Full metadata output and duplication without metadata |


---
# Possible Improvements
All possible improvements are listed below to keep track of them:
* Dockerize
* Logging
* Improve Exceptions: image and other files validation
* call for metadata collection
* TBD


# Extra notes
## Why Pillow?
Pillow as the successor of PIL offers faster data-accessing methods and powerful optimized processing capabilities, with a continued contribution as a live project.
Reference:

	- https://python-pillow.org/
	- https://pillow.readthedocs.io/en/stable/index.html
	- https://github.com/python-pillow/Pillow

## Flask
[needs completion]

<!-- Contributing -->

## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/your_feature`)
3. Commit your Changes (`git commit -m 'Added x feature'`)
4. Push to the Branch (`git push origin feature/your_feature`)
5. Open a Pull Request