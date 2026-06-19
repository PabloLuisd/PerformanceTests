FROM locustio/locust:latest

WORKDIR /mnt/locust

COPY . .

CMD ["-f", "locustfile.py"]