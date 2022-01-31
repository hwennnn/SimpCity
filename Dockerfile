FROM robd003/python3.10:latest

WORKDIR /usr/src/app

# Install necessary python libraries
COPY requirements.txt .

RUN pip3 install -r requirements.txt

# Copy only necessary files
COPY main.py .
COPY ./models/ ./models

CMD ["python3", "main.py"]
