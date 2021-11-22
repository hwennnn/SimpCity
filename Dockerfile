FROM robd003/python3.10:latest

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
