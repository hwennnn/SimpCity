FROM robd003/python3.10:latest

WORKDIR /usr/src/app

COPY . .

CMD ["python3", "main.py"]
