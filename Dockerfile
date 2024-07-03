FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY metapy.py metapy.py

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "metapy.py"]
