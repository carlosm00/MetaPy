FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY metapy.py metapy.py

RUN pip install -r requirements.txt

CMD ["python", "metapy.py"]
