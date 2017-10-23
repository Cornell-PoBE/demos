FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential wget
COPY app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
