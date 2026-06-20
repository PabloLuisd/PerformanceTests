FROM python:3.13-slim

WORKDIR /mnt/locust

COPY requirements.txt .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["locust", "-f", "locustfile.py"]



